import keyring.backend
import platform
import ssl

'''
import lbrynet.daemon.auth
from lbrynet.daemon.auth.util import APIKey, API_KEY_NAME

def load_api_keys(path):
    key_name = API_KEY_NAME
    context = service.getApplicationContext();
    secret = lbrynet_utils.loadApiSecret(context, ks)
    # TODO: For testing. Normally, this should not be displayed.
    log.info('Loaded API Secret: %s', secret);
    return { key_name: APIKey(secret, key_name, None) }

def save_api_keys(keys, path):
    key_name = API_KEY_NAME
    if key_name in keys:
        secret = keys[key_name].secret
        # TODO: For testing. Normally, this should not be displayed.
        log.info('Saving API Secret: %s', secret)
        context = service.getApplicationContext()
        lbrynet_utils.saveApiSecret(secret, context, ks)

def initialize_api_key_file(key_path):
    context = service.getApplicationContext()
    secret = lbrynet_utils.loadApiSecret(context, ks)
    if secret is None:
        keys = {}
        new_api_key = APIKey.new(name=API_KEY_NAME)
        keys.update({new_api_key.name: new_api_key})
        save_api_keys(keys, key_path)


lbrynet.daemon.auth.util.load_api_keys = load_api_keys
lbrynet.daemon.auth.util.save_api_keys = save_api_keys
lbrynet.daemon.auth.util.initialize_api_key_file = initialize_api_key_file

# Keyring backend
class LbryAndroidKeyring(keyring.backend.KeyringBackend):
    priority = 1

    def set_password(self, servicename, username, password):
        context = service.getApplicationContext()
        lbrynet_utils.setPassword(servicename, username, password, context, ks)

    def get_password(self, servicename, username):
        context = service.getApplicationContext()
        return lbrynet_utils.getPassword(servicename, username, context, ks)

    def delete_password(self, servicename, username):
        context = service.getApplicationContext()
        lbrynet_utils.deletePassword(servicename, username, context, ks)

# set the keyring backend
keyring.set_keyring(LbryAndroidKeyring())
'''

import logging.handlers
from lbrynet.core import log_support
from twisted.internet import defer, reactor
from jsonrpc.proxy import JSONRPCProxy

from lbrynet import analytics
from lbrynet import conf
from lbrynet.core import utils, system_info
from lbrynet.daemon.auth.client import LBRYAPIClient
from lbrynet.daemon.DaemonServer import DaemonServer


# LBRY Daemon
log = logging.getLogger(__name__)

def test_internet_connection():
    return utils.check_connection()
    
def start():
    # lbry daemon
    conf.initialize_settings()

    lbrynet_log = conf.settings.get_log_filename()
    log_support.configure_logging(lbrynet_log, True, [])
    log.debug('Final Settings: %s', conf.settings.get_current_settings_dict())
    log.info("Starting lbrynet-daemon")

    if test_internet_connection():
        analytics_manager = analytics.Manager.new_instance()
        start_server_and_listen(False, analytics_manager)
        reactor.run()
    else:
        log.info("Not connected to internet, unable to start")

@defer.inlineCallbacks
def start_server_and_listen(use_auth, analytics_manager, max_tries=5):
    """The primary entry point for launching the daemon.
    Args:
        use_auth: set to true to enable http authentication
        analytics_manager: to send analytics
    """
    analytics_manager.send_server_startup()
    daemon_server = DaemonServer(analytics_manager)
    try:
        yield daemon_server.start(use_auth)
        analytics_manager.send_server_startup_success()
    except Exception as e:
        log.exception('Failed to startup')
        yield daemon_server.stop()
        analytics_manager.send_server_startup_error(str(e))
        reactor.fireSystemEvent("shutdown")


if __name__ == '__main__':
    start()

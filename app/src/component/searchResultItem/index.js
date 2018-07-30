import { connect } from 'react-redux';
import {
  doResolveUri,
  makeSelectClaimForUri,
  makeSelectMetadataForUri,
  makeSelectFileInfoForUri,
  makeSelectIsUriResolving,
} from 'lbry-redux';
import { selectShowNsfw } from '../../redux/selectors/settings';
import SearchResultItem from './view';

const select = (state, props) => ({
  claim: makeSelectClaimForUri(props.uri)(state),
  isDownloaded: !!makeSelectFileInfoForUri(props.uri)(state),
  metadata: makeSelectMetadataForUri(props.uri)(state),
  isResolvingUri: makeSelectIsUriResolving(props.uri)(state),
  obscureNsfw: !selectShowNsfw(state)
});

const perform = dispatch => ({
  resolveUri: uri => dispatch(doResolveUri(uri))
});

export default connect(select, perform)(SearchResultItem);

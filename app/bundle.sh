#!/bin/bash
react-native bundle --dev false --entry-file src/index.js --assets-dest ../lbry-ios --bundle-output ../lbry-ios/index.ios.jsbundle --platform ios

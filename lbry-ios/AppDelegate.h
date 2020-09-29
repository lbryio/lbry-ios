//
//  AppDelegate.h
//  lbry
//
//  Created by Akinwale Ariwodola on 31/05/2018.
//

#import <UIKit/UIKit.h>
#include "../../kivy-ios/build/sdl2/arm64/SDL-7cc4fc886d9e/src/video/uikit/SDL_uikitappdelegate.h"

@interface AppDelegate : SDLUIKitDelegate {
    UIWindow *window;
    UIView *view;
}

@property (strong, nonatomic, retain) UIWindow *window;
@property (nonatomic, retain) UIView *view;

@end


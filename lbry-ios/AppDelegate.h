//
//  AppDelegate.h
//  lbry
//
//  Created by Akinwale Ariwodola on 31/05/2018.
//

#import <UIKit/UIKit.h>
#include "../../kivy-ios/build/sdl2/arm64/SDL2-2.0.5/src/video/uikit/SDL_uikitappdelegate.h"

@interface AppDelegate : SDLUIKitDelegate {
    UIWindow *window;
}

@property (strong, nonatomic, retain) UIWindow *window;


@end


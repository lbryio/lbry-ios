//
//  AppDelegate.m
//  lbry
//
//  Created by Akinwale Ariwodola on 01/06/2018.
//

#import "AppDelegate.h"
#import "MainViewController.h"
#include "../../kivy-ios/dist/include/common/sdl2/SDL_main.h"
#include "../../kivy-ios/dist/include/common/sdl2/SDL_system.h"

@implementation SDLUIKitDelegate (customDelegate)

// replace SDLUIKitDelegate with our app delegate
+(NSString *)getAppDelegateClassName {
    return @"AppDelegate";
}

@end

@interface AppDelegate ()

@end

@implementation AppDelegate
@synthesize window;


- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    
    SDL_SetMainReady();
    [self performSelector:@selector(postFinishLaunch) withObject:nil afterDelay:0.0];
    
    return YES;
}

// override SDL postFinishLaunch
- (void)postFinishLaunch {
    /* run the actual application (in this case, Python main) */
    SDL_iPhoneSetEventPump(SDL_TRUE);
    SDL_main(0, nil);
    SDL_iPhoneSetEventPump(SDL_FALSE);
    
    // show main view
    MainViewController *viewController = [[MainViewController alloc] initWithNibName:@"MainView" bundle:nil];
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.rootViewController = viewController;
    [viewController release];

    [self.window makeKeyAndVisible];
}


- (void)applicationWillResignActive:(UIApplication *)application {
    // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
    // Use this method to pause ongoing tasks, disable timers, and invalidate graphics rendering callbacks. Games should use this method to pause the game.
}


- (void)applicationDidEnterBackground:(UIApplication *)application {
    // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
    // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
}


- (void)applicationWillEnterForeground:(UIApplication *)application {
    // Called as part of the transition from the background to the active state; here you can undo many of the changes made on entering the background.
}


- (void)applicationDidBecomeActive:(UIApplication *)application {
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
}


- (void)applicationWillTerminate:(UIApplication *)application {
    // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
}


@end

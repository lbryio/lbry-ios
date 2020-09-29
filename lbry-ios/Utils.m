//
//  Utils.m
//  lbry
//
//  Created by Akinwale Ariwodola on 28/09/2020.
//

#import <Foundation/Foundation.h>
#import "Utils.h"

@implementation Utils

+(NSString *) storageDirectory {
    return [[[[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask] lastObject] path];
}

@end

//
//  DevicesManagers.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

class DevicesManagers {
    
    static let shared = DevicesManagers()
    
    var devices: [Device] = []
}

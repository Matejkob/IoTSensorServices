//
//  Device.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

struct Device: Codable {
    var name = ""
    var ip = ""
    var port: Int32 = 0
    var key = ""
}

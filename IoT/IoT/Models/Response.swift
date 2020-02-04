//
//  Response.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

struct Sensor: Codable {
    var status: String
    var name: String
    var value: String
}

struct Response: Codable {
    var sensors: [Sensor]
    var timeStamp: String
    var successFlag: String
}

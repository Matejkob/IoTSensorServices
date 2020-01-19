//
//  Response.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

struct Response: Codable {
    var successFlag: Bool
    var timeStamp: Data
    var dataFromSensor: String // TODO: Chnage to correct
    var error: String
}

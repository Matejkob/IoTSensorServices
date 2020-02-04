//
//  Request.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

enum RequestAction: String {
    case get_data_from_sensor = "get_data_from_sensor"
}

struct Request: Codable {
    var action: String
}

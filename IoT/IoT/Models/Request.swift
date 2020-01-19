//
//  Request.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

enum RequestAction: String, Codable {
    case sensor_initialization
    case sensor_calibration
    case get_data_from_sensor
    case get_state_of_all_sensors
}

struct Request: Codable {
    var action: RequestAction
    var sensor_id: Int
}

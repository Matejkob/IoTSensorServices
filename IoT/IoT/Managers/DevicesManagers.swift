//
//  DevicesManagers.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import Foundation

class DeviceManager {
    
    private let key = "kDevice"
    static let shared = DeviceManager()
    
    var device: Device {
        get {
            if let savedDevice = UserDefaults.standard.object(forKey: key) as? Data {
                let decoder = JSONDecoder()
                if let loadedDevice = try? decoder.decode(Device.self, from: savedDevice) {
                    return loadedDevice
                }
            }
            return Device()
        } set {
            let encoder = JSONEncoder()
            if let encoded = try? encoder.encode(newValue) {
                let defaults = UserDefaults.standard
                defaults.set(encoded, forKey: key)
            }
        }
    }
}

//
//  DeviceDetailsViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit
import Socket

class DeviceDetailsViewController: UIViewController {
    
    var device = Device()
    private var socket: Socket?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
    }
}

extension DeviceDetailsViewController {
    private func setupView() {
        view.backgroundColor = .white
    }
    
    private func createSocket() {
        do {
            socket = try Socket.create()
        } catch {
            print("Error while create socket")
        }
    }
    
    private func connectToServer() {
        guard let socket = socket else {
            return
        }
        do {
            try socket.connect(to: "80.54.73.236", port: 7555)
        } catch {
            print("Error while connecting to server")
        }
    }
}

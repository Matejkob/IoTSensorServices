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
    
    private var socket: Socket?
    private(set) var label = UILabel()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        navigationController?.setNavigationBarHidden(false, animated: true)
        navigationController?.navigationBar.tintColor = .white
    }
}

extension DeviceDetailsViewController {
    private func setupView() {
        view.backgroundColor = .systemPink
        setupLabel()
    }
    
    private func setupLabel() {
        label.font = UIFont.systemFont(ofSize: 19.0, weight: .regular)
        label.textColor = .white
        label.numberOfLines = 0
        label.textAlignment = .center
        view.addSubview(label)
        label.snp.makeConstraints { (make) in
            make.center.equalTo(self.view)
            make.left.equalTo(self.view).offset(16)
            make.right.equalTo(self.view).offset(-16)
        }
    }
}

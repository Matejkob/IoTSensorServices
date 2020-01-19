//
//  AddDeviceViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class AddDeviceViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        navigationController?.setNavigationBarHidden(false, animated: true)
    }
}

extension AddDeviceViewController {
    private func setupView() {
        view.backgroundColor = .white
        title = "Dodaj swoje urządzenie"
        navigationItem.leftBarButtonItem = UIBarButtonItem(barButtonSystemItem: .cancel, target: self, action: #selector(dismissAction))
    }
    
    @objc private func dismissAction() {
        dismiss(animated: true)
    }
}

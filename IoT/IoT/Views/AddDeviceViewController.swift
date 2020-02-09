//
//  AddDeviceViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class AddDeviceViewController: UIViewController {
    
    var homeViewController: HomeViewController?
    
    private let ipInputTextField = InputTextField()
    private let portInputTextField = InputTextField()
    private let saveButton = SaveButton(type: .system)
    private let inputsStackView = UIStackView()
    private let spinnerViewController = SpinnerViewController()
    
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
        
        setupInputsStackView()
    }
    
    private func setupInputsStackView() {
        inputsStackView.axis = .vertical
        inputsStackView.spacing = 24.0
        inputsStackView.distribution = .equalSpacing
        
        setupIpInputTextField()
        setupPortInputTextField()
        setupSaveButton()
        
        view.addSubview(inputsStackView)
        inputsStackView.snp.makeConstraints { (make) in
            make.top.equalTo(self.view.safeAreaLayoutGuide.snp.top).offset(32)
            make.left.equalTo(self.view).offset(16)
            make.right.equalTo(self.view).offset(-16)
        }
    }
    
    private func setupIpInputTextField() {
        ipInputTextField.placeholder = "Adres IP urządzenia"
        inputsStackView.addArrangedSubview(ipInputTextField)
    }
    
    private func setupPortInputTextField() {
        portInputTextField.placeholder = "Port urządzenia"
        inputsStackView.addArrangedSubview(portInputTextField)
    }

    private func setupSaveButton() {
        saveButton.addTarget(self, action: #selector(saveButtonPressed), for: .touchUpInside)
        inputsStackView.addArrangedSubview(saveButton)
    }
    
    @objc private func dismissAction() {
        dismiss(animated: true)
    }
    
    @objc private func saveButtonPressed() {
        guard let ip = ipInputTextField.text, let port = portInputTextField.text, !ip.isEmpty, !port.isEmpty else {
            let alert = UIAlertController(title: "Uzupełnij wszystkie pola", message: "Wszyskie dane muszą zostać podane.", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
            present(alert, animated: true)
            return
        }
        var newDevice = Device()
        newDevice.ip = ip
        newDevice.port = Int32(port) ?? 0
        DeviceManager.shared.device = newDevice
        showSpiner()
        homeViewController?.connectToServerAndGetData()
        dismissSpiner()
        dismissAction()
    }

    private func showSpiner() {
        addChild(spinnerViewController)
        spinnerViewController.view.frame = view.frame
        view.addSubview(spinnerViewController.view)
        spinnerViewController.didMove(toParent: self)
    }
    
    private func dismissSpiner() {
        spinnerViewController.willMove(toParent: nil)
        spinnerViewController.view.removeFromSuperview()
        spinnerViewController.removeFromParent()
    }
}

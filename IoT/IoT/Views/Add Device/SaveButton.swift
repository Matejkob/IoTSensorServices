//
//  SaveButton.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class SaveButton: UIButton {
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupView()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension SaveButton {
    private func setupView() {
        backgroundColor = .systemPink
        setTitle("Dodaj", for: .normal)
        setTitleColor(.white, for: .normal)
        titleLabel?.font = UIFont.systemFont(ofSize: 15.0, weight: .bold)
        layer.cornerRadius = 22.0
        
        snp.makeConstraints { (make) in
            make.height.equalTo(44)
        }
    }
}

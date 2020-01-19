//
//  InputTextField.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class InputTextField: UITextField {
    
    override var placeholder: String? {
        didSet {
            if let placeholder = placeholder {
                attributedPlaceholder = NSAttributedString(string: placeholder, attributes: [NSAttributedString.Key.foregroundColor: UIColor.systemPink.withAlphaComponent(0.7)])
            }
        }
    }
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupView()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension InputTextField {
    private func setupView() {
        backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
        layer.cornerRadius = 22.0
        layer.borderColor = UIColor.systemPink.cgColor
        layer.borderWidth = 2.0
        textColor = .systemPink
        
        let paddingView = UIView(frame: CGRect(x: 0, y: 0, width: 22.0, height: 44.0))
        leftViewMode = .always
        leftView = paddingView
        
        snp.makeConstraints { (make) in
            make.height.equalTo(44)
        }
    }
}

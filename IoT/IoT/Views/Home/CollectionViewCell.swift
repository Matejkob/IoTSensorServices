//
//  CollectionViewCell.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit
import SnapKit

extension CollectionViewCell {
    struct ViewModel {
        var device = Device()
    }
}

class CollectionViewCell: UICollectionViewCell {
    
    static let reuseIdentifier = "CollectionViewCell"
    
    private let imageView = UIImageView()
    private let nameLabel = UILabel()
    private let ipAddres = UILabel()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupView()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension CollectionViewCell {
    func updateView(with viewModel: ViewModel) {
        nameLabel.text = viewModel.device.name
        ipAddres.text = "IP: " + viewModel.device.ip
    }
}

extension CollectionViewCell {
    private func setupView() {
        backgroundColor = .systemPink
        layer.cornerRadius = 16.0
        
        setupImageView()
        setupNameLable()
        setupIpAddres()
    }
    
    private func setupImageView() {
        imageView.image = UIImage(named: "lotIcon")?.withRenderingMode(.alwaysTemplate)
        imageView.contentMode = .scaleAspectFit
        imageView.tintColor = .white
        
        addSubview(imageView)
        imageView.snp.makeConstraints { (make) in
            make.top.equalTo(self).offset(8)
            make.left.equalTo(self).offset(12)
            make.height.equalTo(36)
            make.width.equalTo(36)
        }
    }
    
    private func setupNameLable() {
        nameLabel.numberOfLines = 2
        nameLabel.textColor = .white
        nameLabel.font = UIFont.systemFont(ofSize: 14, weight: .bold)
        
        addSubview(nameLabel)
        nameLabel.snp.makeConstraints { (make) in
            make.top.equalTo(self.imageView.snp.bottom).offset(4)
            make.left.equalTo(self).offset(12)
            make.right.equalTo(self).offset(-12)
        }
    }
    
    private func setupIpAddres() {
        ipAddres.textColor = .white
        ipAddres.font = UIFont.systemFont(ofSize: 13, weight: .regular)
        
        addSubview(ipAddres)
        ipAddres.snp.makeConstraints { (make) in
            make.top.equalTo(self.nameLabel.snp.bottom).offset(2)
            make.left.equalTo(self).offset(12)
            make.right.equalTo(self).offset(-12)
        }
    }
}

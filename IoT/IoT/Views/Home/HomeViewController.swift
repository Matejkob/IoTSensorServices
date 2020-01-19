//
//  HomeViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {
    
    private let collectionView = UICollectionView()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
    }
}

extension HomeViewController {
    private func setupView() {
        view.backgroundColor = .white
        navigationController?.navigationBar.prefersLargeTitles = true
        title = "Czujniki IoT"
    }
    
    private func setupCollectionView() {
        
        view.addSubview(collectionView)
    }
}

//
//  HomeViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit
import SnapKit

class HomeViewController: UIViewController {
    
    var collectionView: UICollectionView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
    }
}

extension HomeViewController {
    private func setupView() {
        title = "Czujniki IoT"
        view.backgroundColor = .white
        navigationController?.tabBarItem.title = ""
        navigationController?.navigationBar.prefersLargeTitles = true
        
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        let collectionViewLayout = UICollectionViewFlowLayout()
        let screenWidth = UIScreen.main.bounds.size.width
        let itemWidth = (screenWidth - 3 * 16.0) / 2.0
        collectionViewLayout.itemSize = CGSize(width: itemWidth, height: 110.0)
        
        collectionView = UICollectionView(frame: .zero, collectionViewLayout: collectionViewLayout)
        collectionView?.delegate = self
        collectionView?.dataSource = self
        collectionView?.register(CollectionViewCell.self, forCellWithReuseIdentifier: CollectionViewCell.reuseIdentifier)
        
        collectionView?.backgroundColor = .white
        
        view.addSubview(collectionView!)
        collectionView?.snp.makeConstraints { (make) in
            make.top.bottom.equalTo(self.view)
            make.left.equalTo(self.view).offset(16)
            make.right.equalTo(self.view).offset(-16)
        }
    }
}

extension HomeViewController: UICollectionViewDelegate {
    
}

extension HomeViewController: UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return DevicesManagers.shared.devices.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CollectionViewCell.reuseIdentifier, for: indexPath) as? CollectionViewCell else {
            return UICollectionViewCell()
        }
        
        return cell
    }
}

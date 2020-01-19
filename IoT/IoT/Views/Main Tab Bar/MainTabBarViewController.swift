//
//  MainTabBarViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class MainTabBarViewController: UITabBarController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViewControllers()
        setupView()
    }
}

extension MainTabBarViewController {
    private func setupViewControllers() {
        viewControllers = [
            createDummyNavigationController(withImage: "house", for: HomeViewController()),
            createDummyNavigationController(withImage: "person", for: UserProfileViewController())
        ]
    }
    
    private func setupView() {
        tabBar.backgroundColor = .white
        tabBar.tintColor = .black
    }
    
    private func createDummyNavigationController(withImage imageName: String, for viewController: UIViewController) -> UINavigationController {
        let navigationController = UINavigationController(rootViewController: viewController)
        navigationController.tabBarItem.image = UIImage(systemName: imageName)
        navigationController.tabBarItem.selectedImage = UIImage(systemName: imageName + ".fill")
        return navigationController
    }
}

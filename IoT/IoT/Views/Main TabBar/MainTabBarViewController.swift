//
//  MainTabBarViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit

class MainTabBarViewController: UITabBarController {
    
    private let homeViewController = HomeViewController()
    private let addDeviceViewController = AddDeviceViewController()
    private let userProfileViewController = UserProfileViewController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViewControllers()
        setupView()
    }
}

extension MainTabBarViewController {
    private func setupViewControllers() {
        viewControllers = [
            createDummyNavigationController(withImageName: "house", for: homeViewController),
            createDummyViewController(withImageName: "plus.circle", for: addDeviceViewController),
            createDummyNavigationController(withImageName: "person", for: userProfileViewController)
        ]
    }
    
    private func setupView() {
        tabBar.isTranslucent = false
        tabBar.backgroundColor = .white
        tabBar.tintColor = .black
        tabBar.unselectedItemTintColor = .black
        delegate = self
    }
    
    private func createDummyNavigationController(withImageName imageName: String, for viewController: UIViewController) -> UINavigationController {
        let navigationController = UINavigationController(rootViewController: viewController)
        navigationController.tabBarItem.image = UIImage(systemName: imageName)
        navigationController.tabBarItem.selectedImage = UIImage(systemName: imageName + ".fill")
        navigationController.navigationBar.tintColor = .systemPink
        return navigationController
    }
    
    private func createDummyViewController(withImageName imageName: String, for viewController: UIViewController) -> UIViewController {
        viewController.tabBarItem.image = UIImage(systemName: imageName)
        return viewController
    }
}

extension MainTabBarViewController: UITabBarControllerDelegate {
    func tabBarController(_ tabBarController: UITabBarController, shouldSelect viewController: UIViewController) -> Bool {
        if viewController.isKind(of: AddDeviceViewController.self) {
            let addDeviceViewController = AddDeviceViewController()
            addDeviceViewController.homeViewController = homeViewController
            let navigationController = UINavigationController(rootViewController: addDeviceViewController)
            navigationController.navigationBar.tintColor = .systemPink
            present(navigationController, animated: true)
            return false
        }
        return true
    }
}

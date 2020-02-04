//
//  HomeViewController.swift
//  IoT
//
//  Created by Mateusz Bąk on 1/19/20.
//  Copyright © 2020 Mateusz Bąk. All rights reserved.
//

import UIKit
import SnapKit
import Socket

class HomeViewController: UIViewController {
    
    var collectionView: UICollectionView?
    private var socket: Socket?
    private var sensors: [Sensor] = []
    private let spinnerViewController = SpinnerViewController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupView()
        connectToServer()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        navigationController?.navigationBar.tintColor = .systemPink
    }
}

extension HomeViewController {
    private func setupView() {
        title = "Czujniki IoT"
        view.backgroundColor = .white
        navigationController?.tabBarItem.title = ""
        navigationController?.navigationBar.prefersLargeTitles = true
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .refresh, target: self, action: #selector(fetchData))
        
        setupCollectionView()
    }
    
    private func setupCollectionView() {
        let collectionViewLayout = UICollectionViewFlowLayout()
        let screenWidth = UIScreen.main.bounds.size.width
        let itemWidth = (screenWidth - 3 * 16.0) / 2.0
        collectionViewLayout.itemSize = CGSize(width: itemWidth, height: 140.0)
        collectionViewLayout.minimumLineSpacing = 16.0
        collectionViewLayout.minimumInteritemSpacing = 16.0
        
        collectionView = UICollectionView(frame: .zero, collectionViewLayout: collectionViewLayout)
        collectionView?.dataSource = self
        collectionView?.delegate = self
        collectionView?.register(CollectionViewCell.self, forCellWithReuseIdentifier: CollectionViewCell.reuseIdentifier)
        
        collectionView?.backgroundColor = .white
        
        view.addSubview(collectionView!)
        collectionView?.snp.makeConstraints { (make) in
            make.top.bottom.equalTo(self.view)
            make.left.equalTo(self.view).offset(16)
            make.right.equalTo(self.view).offset(-16)
        }
    }
    
    @objc private func fetchData() {
        showSpiner()
        connectToServer()
        dismissSpiner()
    }
    
    private func connectToServer() {
        do {
            socket = try Socket.create()
        } catch {
            print("Error while create socket")
            return
        }
        
        guard let socket = socket else {
            return
        }
        do {
            try socket.connect(to: "46.174.0.213", port: 7555)
        } catch {
            print("Error while connecting to server")
            return
        }
        
        var dataInJson = Data()
        do {
            let dataToSend = Request(action: RequestAction.get_data_from_sensor.rawValue)
            dataInJson = try JSONEncoder().encode(dataToSend)
        } catch {
            print("Error while encoding struct to data")
            return
        }
                
        do {
            try socket.write(from: dataInJson)
        } catch {
            print("Error while writing to server")
            return
        }
        
        var data = Data()
        do {
            try socket.read(into: &data)
        } catch {
            print("Error while reading and decoding data")
            return
        }
        
        do {
            let readData = try JSONDecoder().decode(Response.self, from: data)
            if readData.successFlag == "True" {
                sensors = readData.sensors
                collectionView?.reloadData()
            }
        } catch {
            print("Error while decoding")
            return
        }
        
        socket.close()
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

extension HomeViewController: UICollectionViewDataSource, UICollectionViewDelegate {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return sensors.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: CollectionViewCell.reuseIdentifier, for: indexPath) as? CollectionViewCell else {
            return UICollectionViewCell()
        }
        var cellModel = CollectionViewCell.ViewModel()
        cellModel.sensor = sensors[indexPath.row]
        cell.updateView(with: cellModel)
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        let deviceDetailsViewController = DeviceDetailsViewController()
        let sensor = sensors[indexPath.row]
        deviceDetailsViewController.label.text = sensor.name + "\n" + sensor.value
        deviceDetailsViewController.hidesBottomBarWhenPushed = true
        navigationController?.pushViewController(deviceDetailsViewController, animated: true)
    }
}

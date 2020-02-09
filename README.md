## Internet of Things Socket Communication Services
**IoTSensorServices** is a client server app with backend written in python and front-end in swift. It is an utility that simplifies reading data from sensors connected to Raspberry Pi and presenting it to user in safe and elegant way. Networking is made on sockets and Transmission Control Protocol (TCP).

## Contents
- [Requirements](#requirements)
- [Features](#features)
- [Installation and Usage](#installation-and-usage)
- [How it's working](#how-it-is-working)
- [Dependencies](#dependencies)
- [Authors](#authors)
- [License](#license)

## Requirements
### Server
* Python 3.7+
* Raspbian 4.0+
TODO
### Client
* Mac OS X 10.15+
* iOS 13.0+
* Xcode 11.0+
* Swift 5.1+

## Features
- [x] Easy connecting to the server with known IP and port address
- [x] Readable interface to read data from sensors
- [x] Easy connection of sensors

## Installation and Usage
### Server
To install server you need Raspian 4.0+ installed on Rassbery pi. Connect the sensors to Pi and clone the repo. If you changed pin connection just set the varibles in code. To start program run it with command line "python3 -m Server.task_interface.py". 
TODO ❗️

### Client
To install client app you need Xcode 11.0+, Mac OS X 10.15+. Just clone this repo, open loT -> loT.xcworkspace in xcode and buill it on your own device. Nextly to connect to server you have to chose UITabBarItem with a 'plus' icon in UITabBar. Complete the data and click the button. Client will try connect to the server and fetch data. 

## How it is working
### Server

TODO ❗️

### Client
User can trigger fetching data in three ways. 1. At application start, data is downloading from the remembered ip address and port. 2. User can manually trigger fetching by pressing refresh button. 3. When a user add new ip address with port and press "Add" button data will be automatically fetch. IP address and port are saved in User Defaults - an interface to the user’s defaults database, where you store key-value pairs persistently across launches of your app. The networking work on TCP. Firstly we are creating socket. Next we try connect to server. If result of it will be successful we encode swift struct to json data and we write this data to server. Nextly we call read metod and when we receive data from socket we decode data and update UI. Everything Everything happens on the main thread.

## Dependencies
### Server
* https://github.com/adafruit/Adafruit_Python_DHT - To get data from DHT 11 sensor
TODO ❗️
### Client
* https://github.com/IBM-Swift/BlueSocket - Socket framework for Swift using the Swift Package Manager.
* https://github.com/SnapKit/SnapKit - It is a DSL to make Auto Layout easy on both iOS and OS X.

## Authors
* https://github.com/matejkob
* https://github.com/kkuuba
* https://github.com/plbakol2

## License
IoTSensorServices is released under the MIT license. See LICENSE for details.

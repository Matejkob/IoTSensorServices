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
* packages defined in requierments.txt

### Client
* Mac OS X 10.15+
* iOS 13.0+
* Xcode 11.0+
* Swift 5.1+

## Features
- [x] Easy connecting to the server with known IP and port address
- [x] Readable interface to read data from sensors
- [x] Easy sensor connection

## Installation and Usage
### Server
To deploy server you need Raspian 4.0+ or any Unix system supporting Rassbery pi hardware. Connect all sensors to Pi and clone the repo. If you have changed pin connection just set appropertive varibles in code. To start program run it with command line "python3 -m Server.task_interface.py". In addition you can add bash script to crontab in order to autmatically start server when device is booting.
In case when user wants to access server from the outside local network -> NAT on local router is needed.

### Client
To install client app you need Xcode 11.0+, Mac OS X 10.15+. Just clone this repo, open loT -> loT.xcworkspace in xcode and buill it on your own device. Nextly to connect to server you have to chose UITabBarItem with a 'plus' icon in UITabBar. Complete the data and click the button. Client will try connect to the server and fetch data. 

## How it is working
### Server
This part of the project contains two core classes:

* server.py - SocketServer class is responsible for all communication events. On create object of server class, tcp socket with defined settings is created. This class allows to send any type of data via socket by serializing it to JSON object.

* task_interface.py - TaskService class which inherits from SocketServer is connected with requests handling. It's get task info from received data and starts particular action via SensorApi class. Also it contains some error handling and provide services responses with additional task inforamtions.

* sensors.py - SensorAPI class is resposible for sensors services base on GPIO pins interface. Main role of this class is to provide all
data from sensors and return it in defined python dictionary model.

### Client
User can trigger fetching data in three ways. 1. At application start, data is downloading from the remembered ip address and port. 2. User can manually trigger fetching by pressing refresh button. 3. When a user add new ip address with port and press "Add" button data will be automatically fetch. IP address and port are saved in User Defaults - an interface to the user’s defaults database, where you store key-value pairs persistently across launches of your app. The networking work on TCP. Firstly we are creating socket. Next we try connect to server. If result of it will be successful we encode swift struct to json data and we write this data to server. Nextly we call read method and when we receive data from socket we decode data and update UI. Everything happens on the main thread.

## Dependencies
### Server
* https://github.com/adafruit/Adafruit_Python_DHT - To get data from DHT 11 sensor
* https://pypi.org/project/RPi.GPIO/ - For GPIO module support

### Client
* https://github.com/IBM-Swift/BlueSocket - Socket framework for Swift using the Swift Package Manager.
* https://github.com/SnapKit/SnapKit - It is a DSL to make Auto Layout easy on both iOS and OS X.

## Authors
* https://github.com/matejkob
* https://github.com/kkuuba
* https://github.com/plbakol2

## License
IoTSensorServices is released under the MIT license. See LICENSE for details.

# Big-data-IOT-proj
Analyzing data from some built in python libraries that generate sensor data
# Sensor Data Analysis App

This application generates sensor data, displays it, and performs analytics on the data. It consists of several modules/classes that handle different aspects of the data collection, processing, communication, and visualization.

## Communication.py

The `Communication` class provides methods for sending and receiving data to/from a server.

## Dashboard.py

The `Dashboard` class is responsible for displaying sensor data and analytics results. It uses matplotlib to visualize the data.

## data_processor.py

The `DataProcessor` class contains static methods for calculating various statistical measures and normalizing data.

## device.py

The `Device` class represents a device that collects sensor data, processes it, and communicates with a server. It uses instances of the `Sensor`, `DataProcessor`, and `Communication` classes.

## main.py

The `main.py` file serves as the entry point of the application. It creates instances of sensors, data processors, communication modules, and devices. It collects sensor data, processes it, sends it to the server, and receives data from the server. Finally, it utilizes the `Dashboard` class to display the collected data and analytics results.

## sensor.py

The `Sensor` class is an abstract base class that represents a generic sensor. It provides a method to read data from the sensor. The `TemperatureSensor`, `HumiditySensor`, and `LightSensor` subclasses inherit from the `Sensor` class and implement specific sensor types.

---

Please note that this is just a brief overview of the project structure and its main components. For detailed information on how to use each class and its methods, please refer to the source code documentation and comments.

Feel free to explore the code and modify it according to your specific needs. Happy coding!

from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard
from sensor import TemperatureSensor, HumiditySensor, LightSensor
def main():
    temperature_sensor = TemperatureSensor(-10, 40, "Temperature")
    humidity_sensor = HumiditySensor(0, 100, "Humidity")
    light_sensor = LightSensor(0, 1023, "Light")
    
    data_processors = [DataProcessor() for _ in range(3)]
    communications = [Communication("https://central-server.example.com") for _ in range(3)]
    devices = [Device(sensor, data_processor, communication) for sensor, data_processor, communication in zip([temperature_sensor, humidity_sensor, light_sensor], data_processors, communications)]
    
    for device in devices:
        device.collect_data(10)
        processed_data = device.process_data()
        device.send_data_to_server(processed_data)
        device.receive_data_from_server()
    
    dashboard = Dashboard()
    for device in devices:
        dashboard.display_data(device.data,device.sensor.name)
        dashboard.display_analytics(device.process_data(), device.sensor.name)


if __name__ == "__main__":
    main()
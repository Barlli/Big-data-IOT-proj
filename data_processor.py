import statistics
import numpy as np

class DataProcessor:
    @staticmethod
    def calculate_average(data):
        return statistics.mean(data)

    @staticmethod
    def calculate_min(data):
        return min(data)

    @staticmethod
    def calculate_max(data):
        return max(data)

    @staticmethod
    def normalize_data(data):
        data_mean = np.mean(data)
        data_std = np.std(data)
        return (data - data_mean) / data_std
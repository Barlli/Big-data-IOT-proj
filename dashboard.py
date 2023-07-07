import matplotlib.pyplot as plt
import numpy as np
class Dashboard:
    def display_data(self, data, name):
        print(f"Timestamp\t\t{name} Sensor Data")
        print("-" * 40)
        for timestamp, value in data:
            print(f"{timestamp}\t{value:.2f}")

    def display_analytics(self, analytics, name):
        average, minimum, maximum, normalized= analytics
        print("Analytics Results")
        print("-" * 40)
        print(f"Average {name}: {average:.2f}")
        print(f"Minimum {name}: {minimum:.2f}")
        print(f"Maximum {name}: {maximum:.2f}")
        normalized_str = ', '.join([f'{x:.2f}' for x in normalized])
        print(f"Normalized {name}: [{normalized_str}]")
        plt.figure(figsize=(8, 4))
        plt.title(f"{name} Analytics Results")
        plt.plot(np.array(analytics[-1]))
        plt.ylabel("Normalized Data")
        plt.xlabel("Timestamp")
        plt.show()
  
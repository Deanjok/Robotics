import numpy as np

class SolarPanel:
    def __init__(self, max_power_w):
        self.max_power_w = max_power_w

    def generate_power(self, sun_angle_deg):
        if abs(sun_angle_deg) >= 90:
            return 0
        sun_angle_deg = np.deg2rad(sun_angle_deg)
        power = self.max_power_w * np.cos(sun_angle_deg)
        return power

solar_power = SolarPanel(max_power_w=100)
charge_power = solar_power.generate_power(sun_angle_deg=90)
print(charge_power)
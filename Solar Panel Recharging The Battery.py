import numpy as np

class SolarPanel:
    def __init__(self, max_capacity_w):
        self.max_capacity_w = max_capacity_w

    def generate_power(self, sun_angle_deg):
        if abs(sun_angle_deg) >= 90:
            return 0
        sun_angle_deg = np.deg2rad(sun_angle_deg)
        power = self.max_capacity_w * np.cos(sun_angle_deg)
        return power

class Battery:
    def __init__(self, capacity_wh: float, current_charge_wh):
        self.capacity_wh = capacity_wh
        self.current_charge_wh = current_charge_wh

    def consume(self, power_w, duration_h):
        energy_used = power_w * duration_h
        self.current_charge_wh -= energy_used
        if self.current_charge_wh <= 0:
             print(f"Battery is fully depleted: 0")
             self.current_charge_wh = 0
             return 0
        return self.current_charge_wh
    def charge(self, power_w, duration_h):
        energy_gained = power_w * duration_h
        self.current_charge_wh += energy_gained
        if self.current_charge_wh >= self.capacity_wh:
            print(f"Battery is fully charged: {self.capacity_wh:.2f} Wh")
            self.current_charge_wh = self.capacity_wh
            return self.capacity_wh
        return self.current_charge_wh

# The higher the angle the less power it will produce
sun_angle_deg = 20
solar_power = SolarPanel(max_capacity_w=100)
charge_power = solar_power.generate_power(sun_angle_deg)
print(f"The angle of the solar panel is: {sun_angle_deg} degrees relative to the sun, meaning it is producing {charge_power:.2f} W")

# 1. Initialize the battery with a starting charge
battery = Battery(capacity_wh=1000, current_charge_wh=500)
print(f"Starting battery charge: {battery.current_charge_wh:.2f}/{battery.capacity_wh:.2f} Wh")

# 2. Consume power (discharge)
power_used = 15
hours_used = 4
new_battery_charge = battery.consume(power_used, hours_used)
print(f"After consuming {power_used}W for {hours_used} hours, the battery charge is: {new_battery_charge:.2f} Wh")

# 3. Charge using the solar panel
solar_charging_hours = 5
charged_battery_level = battery.charge(power_w=charge_power, duration_h=solar_charging_hours)
print(f"After charging with the solar panel at a {sun_angle_deg} degree angle for {solar_charging_hours} hours, the battery charge is: {charged_battery_level:.2f} Wh")
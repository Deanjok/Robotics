class Battery:
    def __init__(self, capacity_wh: float, current_charge_wh):
        self.capacity_wh = capacity_wh
        self.current_charge_wh = capacity_wh

    def consume(self, power_w, duration_h):
        energy_used = power_w * duration_h
        self.current_charge_wh -= energy_used
        if self.current_charge_wh <= 0:
             print(f"Battery is fully depleted: 0")
             self.current_charge_wh = 0
             return 0
        return self.current_charge_wh

battery = Battery(capacity_wh=100, current_charge_wh=100)
print(battery.capacity_wh)
print(battery.current_charge_wh)
updated_charge = battery.consume(power_w=100, duration_h=10)
print(updated_charge)
class Cooldown_Handler:
    def __init__(self, max_value=0, value=0):
        self.value = value
        self.max_value = max_value

    # Looping cooldown
    def Update_Cooldown(self, delta_time):
        if self.value > 0:
            self.Set_Cooldown(self.value - delta_time)
            return False
        self.Reset_Cooldown()
        return True

    # One off cooldown — caller owns what happens on expiry
    def Tick(self, delta_time):
        if self.value > 0:
            self.Set_Cooldown(self.value - delta_time)
        return self.value <= 0
    

    def Set_Cooldown(self, value):
        self.value = max(0, value)

    def Reset_Cooldown(self):
        self.Set_Cooldown(self.max_value)

    def Save_Data(self):
        return {'value': self.value, 'max_value': self.max_value}

    def Load_Data(self, data):
        self.value = data['value']
        self.max_value = data['max_value']
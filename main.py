#3-misol
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, toza):
        self.__battery = toza


p1 = Phone('iPhone 15', 90)

res = p1.battery
print(res)

p1.battery = 15
print(p1.battery)

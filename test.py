class Car:
    """ Just simple car abstraction """

    def __init__(self, model, maker, release_data):
        self.release_data = release_data
        self.maker = maker
        self.model = model
        self.odometer = 0

    def car_info(self):
        print(f'The car mode  is {self.model} was build by {self.maker} in {self.release_data}')

    def set_odometer(self, milliage):
        if milliage >= self.odometer:
            self.odometer = milliage
            print(f" Actual car odometer value is {self.odometer}")
        else:
            print("You cant set milliage lesser that actual value!")

    def add_odometer(self, delta):
        if delta > 0:
            self.odometer += delta
            print(f" Actual car odometer value is {self.odometer}")
        else:
            print(f'you cant deacrease odometer value')


class Battery:
    """ Класс описывающий простейшую батарею """
    def __init__(self, capacity=75, cycle=0):
        self.cycle = cycle
        self.capacity = capacity

    def add_cycle(self, count=1):
        self.cycle += count

    def decrese_capacity(self):
        self.capacity = self.capacity - self.capacity * (self.cycle / 10) / 10

    def battery_info(self):
        print(f'Battery remaining capacity is : {self.capacity}')
        print(f'Battery charging cycles is : {self.cycle}')


class ElectricCar(Car):
    """ Электрокар - расширяет класс Car"""
    def __init__(self, model, maker, release_data):
        super().__init__(model, maker, release_data)
        self.battery = Battery()


mycar = Car('320d', 'BMW', '2013-03-03')

newcar = ElectricCar('model S', 'Tesla', '2019-04-11')
newcar.set_odometer(30)
newcar.car_info()
newcar.battery.add_cycle(50)
newcar.battery.decrese_capacity()
newcar.battery.battery_info()

class Car:

    def __init__(self, mark='WV', color='red', max_speed=120):
        self.mark = mark
        self.color = color
        self.max_speed = max_speed
        self.__speed = 0
        self._odometer = 0

    @property
    def speed(self):
        return self.__speed
    property()
    @speed.setter
    def speed(self, cur_speed):
        self.__speed = cur_speed
        if self.__speed > self.max_speed:
            print('BOOOM!')
            self.__speed = 0

    def run(self, time):
        self._odometer += self.__speed*time

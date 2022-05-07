class Robot:
    def __init__(self, name, variety):
        self.name = name
        self.variety = variety
        print("Robot")

    def get_info(self):
        return "{} is a {} robot".format(self.name, self.variety)


class ServiceRobot(Robot):
    def __init__(self, name):
        super().__init__(name, "service")


chappy = ServiceRobot("Chappi")
print(chappy.get_info())

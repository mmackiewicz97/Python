import numpy.random as random

class Pedestrian:

    def __init__(self, speed, distance):
        self.speed = speed
        self.distance = distance
        self.evacuation_time = 0

    def calculate_evacuation_time(self):
        self.evacuation_time = self.distance/self.speed

class Evacuees:

    def __init__(self):
        self.number_of_pedestrian = 0
        self.pedestrian = []

    def add_pedestrian(self, pedestrian):
        self.pedestrian.append(pedestrian)

    def get_number_of_pedestians(self):
        return len(self.pedestrian)

    def calculate_evacuation_time_of_pedestrians(self):
        assert len(self.pedestrian) != 0, 'There is no pedestrians in the building'
        for i in self.pedestrian:
            i.calculate_evacuation_time()

    def get_evacuation_time(self):
        assert len(self.pedestrian) != 0, 'There is no pedestrians in the building'
        times = []
        for i in self.pedestrian:
            times.append(i.evacuation_time)
        return min(times)

    def get_lagger(self):
        assert len(self.pedestrian) != 0, 'There is no pedestrians in the building'
        times = []
        for i in self.pedestrian:
            times.append(i.evacuation_time)
        return times.index(min(times))



num_of_pedestrian = 100
evacuees = Evacuees()
pedestrians = []
for i in range(num_of_pedestrian):
    pedestrians.append(Pedestrian(speed=random.normal(1.2, 0.2, 1), distance=random.uniform(10, 80, 1)))

for i in pedestrians:
    evacuees.add_pedestrian(i)

num = evacuees.get_number_of_pedestians()
evacuees.calculate_evacuation_time_of_pedestrians()
print('Czas ewakuacji: {} s'.format(evacuees.get_evacuation_time()[0]))
print('Ostatnia osoba id: {}'.format(evacuees.get_lagger()))
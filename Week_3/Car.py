class CarBase:
    car_type = None
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count

class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    def get_body_volume(self):
        body_length, body_width, body_height = self.body_whl.split('x')
        volume = float(body_length)*float(body_width)*float(body_height)
        return volume
            


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


#def get_car_list(csv_filename):
    #car_list = []
    #return car_list


track1 = Truck('Man', '2.jpeg', 20, '8x3x2.5')
print(track1.car_type)
print(track1.brand)
print(track1.photo_file_name)
print(track1.carrying)
print(track1.get_body_volume())
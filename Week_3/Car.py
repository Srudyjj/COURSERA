import csv
import sys

class CarBase:
    car_type = None
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        filename, file_extension = os.path.splitext(self.photo_file_name)
        return file_extension

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



def get_car_list(csv_filename):
    with open(csv_filename, 'r+', encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        list_car = []
        for row in reader:
            car_property = {}
            listtypeproperty = [
                'car_type','brand','passenger_seats_count','photo_file_name',
                'body_whl','carrying','extra'
            ]
            if len(row) < 7:
                #print("Bad row")
                continue
            else:
                for i in range(7):
                    car_property[listtypeproperty[i]] = row[i]
                #print(car_property)
                list_car.append(car_property)
        print(list_car)

            



get_car_list('coursera_week3_cars.csv')
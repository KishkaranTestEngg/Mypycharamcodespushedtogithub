class Vehicle:
    def __init__(self, model,rental_rate):
        self.model=model
        self.rental_rate=rental_rate

    def calculate_rental(self,days):
        return self.rental_rate * days


class Car(Vehicle):
    def __init__(self, maker_name, car_model, color, year_of_registering, rental_rate):
        self.maker_name=maker_name
        self.car_model=car_model
        self.color=color
        self.year_of_registering=year_of_registering
        self.rental_rate=rental_rate
    def calculate_rental_car(self, no_of_days):
         car_rental=self.rental_rate * no_of_days
         return car_rental

class Bike(Vehicle):
    def __init__(self,bike_name,type_bike,color_available, date_of_registering, rental_rate):
        self.bike_name=bike_name
        self.type_bike=type_bike
        self.color_available=color_available
        self.date_of_registering=date_of_registering
        self.rental_rate=rental_rate

    def calculate_rental_bike(self, no_of_hours):
        bike_rental=self.rental_rate * no_of_hours
        return bike_rental

class Truck(Vehicle):
    def __init__(self, truck_name, type_of_truck, available_models, date_of_purchase, rental_rate):
        self.truck_name=truck_name
        self.type_of_truck=type_of_truck
        self.available_models=available_models
        self.date_of_purchase=date_of_purchase
        self.rental_rate=rental_rate

    def calculate_rental_truck(self,no_of_months_used):
        truck_rental=self.rental_rate *no_of_months_used
        return truck_rental

car = Car("Tata","micro_suv", "blue", "2026", 10000 )
bike=Bike("FZ", "sports", "grey","2025", 3000)
truck=Truck("Ashok_leyland","tripper","5","2023",30000 )

print(car.calculate_rental_car(5))
print(bike.calculate_rental_bike(10))
print(truck.calculate_rental_truck(3))
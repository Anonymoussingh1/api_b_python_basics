class Car():
    
    @staticmethod
    def start_engine():
        print("Normal Engine Started")

    def stop_engine(self):
        print("Normal Engine Started")
        
# static method
print(Car.start_engine())

# not static method
# print(Car.stop_engine())

car = Car()
car.stop_engine()
class vehicle:

    def __init__(self, plate_number, model):
        self.plate_number = plate_number
        self.model = model
        

class driver:

    def __init__(self, name, assigned_vehicle):
        self.name = name
        self.assinged_vehicle = None

    def assign_vehicle(self, Vehicle):
        self.assigned_vehicle = self.model 

Vehicle = vehicle("ABC 1234", "Toyota Vios")
Model = vehicle("Toyota Vios")
plate_number = vehicle("ABC 1234")
driver1 = driver("Mr. Santos")

driver1.assign_vehicle.model(Model)
driver1.assign_vehicle.plate_number(plate_number)

print(driver1.assign_vehicle.model(Model))
print(driver1.assign_vehicle.plate_number(plate_number))
print(driver1)


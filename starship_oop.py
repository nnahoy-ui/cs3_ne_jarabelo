print("Welcome to the Space Launch Fuel Calculator!")

class Starships:
    def __init__(self, base_weight, cargo_weight, final_fuel):
        self.base_weight = base_weight
        self.cargo_weight = cargo_weight
        self.final_fuel = final_fuel

    def calculate_fuel(self):
        base_weight = 50000
        cargo_weight = 1000
        self.final_fuel = (self.base_weight + self.cargo_weight) * 3

        return self.final_fuel

  def display_info(self):
        print("Total Weight:", self.base_weight + self.cargo_weight)
        print("Total Fuel:", self.final_fuel)

    starship = Starships(50000, 1000, 0)
    starship.cargo_weight()
    starship.cargo_weight()
    starship.cargo_weight()
    starship.calculate_fuel()

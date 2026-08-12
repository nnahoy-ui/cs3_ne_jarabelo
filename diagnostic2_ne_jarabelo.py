print("Welcome to the Space Launch Fuel Calculator!")

BASE_WEIGHT = 50000

def calculate_fuel(cargo_weight):
    total_weight = BASE_WEIGHT + cargo_weight
    return total_weight * 3

def cargo_weight_from_type(cargo_type):
    t = cargo_type.strip().lower()
    if t == "satellite":
        return 1000
    if t == "rover":
        return 2500
    if t == "supplies":
        return 500

    return None

while True:
    cargo_type = input("Enter cargo type (Satellite, Rover, Supplies) or 'launch' for blast off!: ")
    if cargo_type.strip().lower() == "launch":
        print("Blast off!")
        break

    cw = cargo_weight_from_type(cargo_type)
    if cw is None:
        print("Item is not approved for the mission")
        continue

    fuel = calculate_fuel(cw)
    print(f"Total fuel needed for launch: {fuel} gallons")

    total_cargo_weight = cw

    print("The total weight of the cargo is" , total_cargo_weight, "pounds")
            
    
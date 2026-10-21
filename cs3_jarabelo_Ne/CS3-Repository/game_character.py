class GameCharacter:

    def __init__(self, health, strength, defense, speed):
        self.__health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.level = 10

    def take_damage(self, hit_points):
        actual_damage = self.defense - hit_points
        self.__health -= actual_damage
        self.defense -= actual_damage 
        print(f"Player taking {hit_points} damage")
        print(f"Player has {self.defense} defense")
        print(f"Actual damage taken: {actual_damage}")

    def train(self, train_points):
        self.strength += train_points
        print(f"Player trained. Strength: {self.strength}")

    def health_regen(self, regen_points):
        self.__health += regen_points
        print(f"Player is healing: Health {self.__health}")

    def show_stat(self):
        print(f"Player Health: {self.__health}")
        print(f"Player Strength: {self.strength}")
        print(f"Player Defense: {self.defense}")


Character_Nnahoy = GameCharacter(100, 80, 80, 50)

Character_Nnahoy.__health
Character_Nnahoy.train(50)
Character_Nnahoy.take_damage(50)
Character_Nnahoy.health_regen(1)
Character_Nnahoy.take_damage(10)
Character_Nnahoy.health_regen(100)
print("--------------------------")
print(Character_Nnahoy.defense)
print(Character_Nnahoy.__health)
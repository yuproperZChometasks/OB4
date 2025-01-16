class Weapon:
    def attack(self):
        raise NotImplementedError("Метод attack должен быть реализован в дочерних классах")

class Sword(Weapon):
    def attack(self, fighter):
        print(f"{fighter.name} наносит удар мечом.")
        return "Монстр побежден!"

class Bow(Weapon):
    def attack(self, fighter):
        print(f"{fighter.name} стреляет из лука.")
        return "Монстр побежден!"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def fight(self, monster):
        if self.weapon is None:
            print("Выберите оружие перед боем.")
            return
        else:
            result = self.weapon.attack(self)
            if result == "Монстр побежден!":
                print(result)
            else:
                print("Боец не смог победить монстра.")

class Monster:
    pass

# Пример использования
fighter = Fighter("Иван")
monster = Monster()

weapon_list = [Sword(), Bow()]
for i in range(2):
    weapon = weapon_list[i]
    fighter.change_weapon(weapon)
    print(f"Боец выбирает {weapon.__class__.__name__}")
    fighter.fight(monster)
    print("\n")

class Weapon:
    def attack(self):
        """Абстрактный метод атаки, который должен быть реализован в дочерних классах."""
        raise NotImplementedError("Метод атаки не реализован.")

class Sword(Weapon):
    """Класс меча, реализующий метод атаки."""
    def attack(self, fighter):
        print(f"{fighter.name} атакует мечом и наносит урон монстру!")

class Bow(Weapon):
    """Класс лука, реализующий метод атаки."""
    def attack(self, fighter):
        print(f"{fighter.name} стреляет из лука и наносит урон монстру!")

class Fighter:
    """Базовый класс бойца."""
    def __init__(self, name, weapon=None):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        """Метод смены оружия бойца."""
        self.weapon = new_weapon

    def fight(self, monster):
        """Метод боя, вызывающий метод атаки выбранного оружия."""
        if self.weapon:
            self.weapon.attack(self)
        else:
            print("Боец не вооружен!")

class Monster:
    """Базовый класс монстра."""
    pass

# Пример использования

def main():
    fighter = Fighter("Иван")
    monster = Monster()

    # Добавление меча
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.fight(monster)

    # Добавление лука
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.fight(monster)

if __name__ == "__main__":
    main()
"""
Этот код демонстрирует применение принципа открытости/закрытости (Open/Closed Principle), позволяя легко добавлять новые типы оружия без изменения существующих классов бойцов и механизма боя.
"""
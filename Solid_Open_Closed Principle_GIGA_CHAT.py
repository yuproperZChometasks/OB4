from abc import ABC, abstractmethod


# Абстрактный класс для всех видов оружия
class Weapon(ABC):
    
    @abstractmethod
    def attack(self, monster):
        pass


# Класс для меча
class Sword(Weapon):
    
    def attack(self, monster):
        print(f"Боец атакует {monster.name} мечом.")
        return 10  # Урон от меча


# Класс для лука
class Bow(Weapon):
    
    def attack(self, monster):
        print(f"Боец стреляет стрелами в {monster.name}.")
        return 8  # Урон от лука


# Класс для монстров
class Monster:
    
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} повержен!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


# Класс для бойца
class Fighter:
    
    def __init__(self, weapon=None):
        self.weapon = weapon
        
    def set_weapon(self, new_weapon):
        self.weapon = new_weapon
        
    def fight(self, monster):
        if self.weapon is not None:
            damage = self.weapon.attack(monster)
            monster.take_damage(damage)
        else:
            print("Боец безоружен! Не могу атаковать.")


if __name__ == "__main__":
    # Создание объектов
    fighter = Fighter()
    monster = Monster("Оборотень")
    
    # Бой без оружия
    fighter.fight(monster)
    
    # Изменение оружия на меч
    sword = Sword()
    fighter.set_weapon(sword)
    fighter.fight(monster)
    
    # Изменение оружия на лук
    bow = Bow()
    fighter.set_weapon(bow)
    fighter.fight(monster)
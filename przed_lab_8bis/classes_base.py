from random import randint, choice


class NegativePowerError(Exception):
    def __init__(self, power):
        super().__init__('Power cannot be negative')
        self.power = power

class NameError(Exception):
    pass

class NegativeHealthError(Exception):
    def __init__(self, health):
        super().__init__('Health cannot be negative')
        self.health = health

class InvalidHeadCountError(Exception):
    def __init__(self, count):
        super().__init__('Needs to have at least one head')
        self.head_count = count


class Player:
    """
    Class Player. Contains attributes:
    :param name: player's name
    :type name: str

    :param power: player's power, defaults to 5
    :type power: int
    """
    def __init__(self, name, power=5):
        self._name = name
        power = int(power)
        if power < 0:
            raise NegativePowerError(power)
        self._power = int(power)

    def name(self):
        return self._name

    def power(self):
        return self._power

    def set_name(self, new_name):
        if not new_name:
            raise NameError("Name cannot be empty")
        self._name = str(new_name).title()

    def set_power(self, new_power):
        if new_power < 0:
            raise NegativePowerError(new_power)
        self._power = int(new_power)

    def info(self):
        """
        Returns basic description of the player
        """
        power = self._power
        return f"My name is {self._name}. My current power is {self._power}."

    def attack(self, enemies):
        if self._power == 0 or not enemies :
            return (None, 0, False)
        # choose enemy from enemies
        enemy = choice(enemies)
        # calculate damage
        damage = randint(1, self.power())
        # apply damage
        took_hit = enemy.take_damage(damage)
        self.set_power(self._power - 1)
        return (enemy, damage, took_hit)

    def __str__(self):
        return self.info()


class Enemy:
    """
    Class Enemy. Contains attributes:
    :param name: enemy's name
    :type name: str

    :param health: enemy's health
    :type health: int
    """
    def __init__(self, name, health):
        if not name:
            raise NameError("Name cannot be empty")
        health = int(health)
        if health < 0:
            raise NegativeHealthError("Health cannot be negative")
        self._name = name
        self._health = health

    def name(self):
        """
        Returns name of the enemy.
        """
        return self._name

    def health(self):
        """
        Returns health of the enemy.
        """
        return self._health

    def set_name(self, new_name):
        """
        Sets name of enemy to new_name.
        """
        if not new_name:
            raise NameError("Name cannot be empty")
        self._name = new_name

    def set_health(self, new_health):
        """
        Sets health of enemy to new_health.
        """
        self._health = max(0, new_health)

    def __str__(self):
        name = self._name
        health = self._health
        return f'This is {name}. It has {health} health points left.'

    def take_damage(self, damage):
        """
        Reduces health of enemy by damage
        """
        damage = int(damage)
        if damage <= 0:
            raise ValueError("Damage has to be positive")
        self._health -= min(damage, self._health)
        return True

    def is_alive(self):
        """
        Returns True if health greater than 0
        """
        return self._health > 0


class Hydra(Enemy):
    def __init__(self, name, health, heads=1):
        super().__init__(name, health)
        if heads < 1:
            raise InvalidHeadCountError(heads)
        self._heads = heads
        self._base_health = health

    def heads(self):
        return self._heads

    def base_health(self):
        return self._base_health

    def __str__(self):
        base = super(Hydra, self).__str__()
        return base + f' It has {self._heads} heads.'

    def regenerate(self, points):
        if points < 0:
            raise ValueError('Cannot regenerate negative number of points')
        if self._health >= self._base_health:
            return
        self._health = min(self._base_health, self._health + points)

    def take_damage(self, damage):
        """
        Reduces health of enemy by damage
        """
        damage = int(damage)
        if damage <= 0:
            raise ValueError("Damage has to be positive")
        self._health -= min(damage, self._health)
        
        # if has multiple heads and health drops to 0, will loose one head and regenerate full health
        # if has one head left and health drop to 0, will loose last head
        if self._health == 0 and self._heads > 1:
            self._heads -= 1
            self._health = self._base_health
        elif self._health == 0 and self._heads == 1:
            self._heads -= 1

        return True

class DragonHydra(Hydra):
    def take_damage(self, damage):
        if randint(0, 1):
          return super().take_damage(damage)
        return False

class Game:
    def __init__(self, player, enemies=None):
        self.player = player
        self.enemies = enemies if enemies else []
        self._result = None

    def play(self, rounds):
        print("Starting game")
        for round in range(1, rounds+1):
            print(f"ROUND {round}")
            target, damage, status = self.player.attack(self.enemies)
            if target:
                if status:
                    print(f"{target.name()} took {damage} points of damage.")
                    if not target.is_alive():
                        print(f"{target.name()} died.")
                        self.enemies.remove(target)
                else:
                    print(f"{target.name()} escaped damage.")
        self._result = bool(self.enemies)
        return self._result


if __name__ == "__main__":
    pass
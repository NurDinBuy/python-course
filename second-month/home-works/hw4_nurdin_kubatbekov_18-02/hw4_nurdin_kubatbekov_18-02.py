from random import randint


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} [{self.__damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def hit(self, heroes):
        for h in heroes:
            if h.health > 0:
                h.health = h.health - self.damage


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    @super_ability.setter
    def super_ability(self, value):
        self.__super_ability = value

    def hit(self, boss):
        if boss.health > 0:
            boss.health = boss.health - self.damage

    def apply_super_ability(self, boss, heroes):
        pass


# ________________________ПЕРСОНАЖИ________________________

class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_ability(self, boss, heroes):
        coeff = randint(2, 5)
        boss.health = boss.health - coeff * self.damage
        print(f'Warrior hits critically: {coeff * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_ability(self, boss, heroes):
        boost = randint(2, 4)
        print(f'Boost: {boost}')
        for h in heroes:
            if h.health > 0:
                h.damage += boost


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, "HEAL")
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    @heal_points.setter
    def heal_points(self, value):
        self.__heal_points = value

    def apply_super_ability(self, boss, heroes):
        for h in heroes:
            if h.health > 0 and h != self:
                h.health += self.heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SAVE_DAMAGE_AND_REVERT")

    def apply_super_ability(self, boss, heroes):
        if self.health - boss.damage:
            self.damage = self.damage + boss.damage // 12
        else:
            boss.damage = boss.damage


class Thor(Hero):
    def __init__(self, name, health, damage, stan=0):
        super().__init__(name, health, damage, 'STAN_LOCK')
        self.__stan = stan

    def apply_super_ability(self, boss, heroes):
        if self.health > 0 and round_number == 1:
            self.damage = self.__stan
        elif self.damage == self.__stan:
            boss.damage = 50
        else:
            boss.damage = 0


class Golem(Hero):
    def __init__(self, name, health, damage, protect=0):
        super().__init__(name, health, damage, 'PROTECT')
        self.__protect = protect

    def apply_super_ability(self, boss, heroes):
        for h in heroes:
            if h.health > 0:
                self.__protect = boss.damage // 5
                if boss.damage > 0:
                    h.health = h.health + self.__protect
                else:
                    h.health = h.health - boss.damage


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'HAPPY_HACKING')

    def apply_super_ability(self, boss, heroes):
        hp_hacking = randint(5, 20)
        for h in heroes:
            boss.health - hp_hacking
            h.health + hp_hacking


class Shaman(Hero):
    def __init__(self, name, health, damage, de_baff=500):
        super().__init__(name, health, damage, 'SHAMAN')
        self.__de_baff = de_baff

    '''Shaman забирает здоровье у союзников и добавляет их к боссу'''

    def apply_super_ability(self, boss, heroes):
        for h in heroes:
            if h.health > 0:
                h.health - self.__de_baff
                boss.health + self.__de_baff


round_number = 0


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} ______________')
    print(boss)
    for h in heroes:
        print(h)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def start_game():
    boss = Boss("Dragon", 10000, 50)
    warrior = Warrior("Atrei", 270, 10)
    doc = Medic("Aibolit", 250, 5, 15)
    magic = Magic("Gendolf", 260, 20)
    berserk = Berserk("Gats", 280, 20)
    assistant = Medic("Med Brat", 290, 10, 5)
    thor = Thor('Lorian', 300, 20)
    golem = Golem('Grok', 500, 5)
    programmer = Hacker('Anon', 200, 10)
    shaman = Shaman('Shaman', 150, 1)
    heroes_list = [warrior, doc, magic, berserk, assistant, thor, golem, programmer, shaman]

    print_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        round(boss, heroes_list)


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(heroes)
    for h in heroes:
        if h.health > 0:
            h.hit(boss)
            h.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


start_game()

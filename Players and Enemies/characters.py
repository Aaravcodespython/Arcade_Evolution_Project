#parent class for players
class Player():
    def __init__(self,name,health,speed):
        self.name = name
        self.health = health
        self.speed = speed

    def showstats(self):
        print(f"PLAYER | NAME-{self.name} | HEALTH-{self.health} | SPEED-{self.speed}")

class ShieldedPlayer(Player):
    def __init__(self,name,health,speed,shield):
        super().__init__(name,health,speed)
        self.shield = shield

    def showstats(self):
        print(f"SHIELDED PLAYER | NAME-{self.name} | HEALTH-{self.health} | SPEED-{self.speed} | SHIELD-{self.shield}")

#parent class for enemies
class Enemy():
    def __init__(self,type,health,speed,damage = 50):
        self.type = type
        self.health = health
        self.speed = speed
        self.damage = damage

    def showstats(self):
        print(f"ENEMY | TYPE-{self.type} | HEALTH-{self.health} | SPEED-{self.speed} | ")

    def attack(self):
        print(f"ENEMY | TYPE-{self.type} | DAMAGE-{self.damage} (DAMAGES THE PLAYER)")

class BossEnemy(Enemy):
    def __init__(self,type,health,speed,damage,ability,ability2):
        super().__init__(type,health,speed,damage)
        self.ability = ability
        self.ability2 = ability2

    def attack(self):
        print(f"☠️BOSS ATTACK☠️ | ENEMY | TYPE-{self.type} | HEAVY DAMAGE-{self.damage} (DAMAGES THE PLAYER A LOT)")

class FastEnemy(Enemy):
    def __init__(self,type,health,speed):
        super().__init__(type,health,speed)

    def attack(self):
        print(f"⚡FAST ATTACK⚡ | ENEMY | TYPE-{self.type} | STRIKE TWICE INSTANTLY FOR 50 DAMAGE")

class HealerEnemy(Enemy):
    def __init__(self,type,health,speed,heal_power):
        super().__init__(type,health,speed)
        self.heal_power = heal_power

        def attack(self):
            print(f" ➕HEAL➕ | ENEMY | TYPE-{self.type} | HEALS TEAM FOR-{self.heal_power}")
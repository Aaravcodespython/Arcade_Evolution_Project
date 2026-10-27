from characters import Player, ShieldedPlayer, Enemy, BossEnemy, FastEnemy, HealerEnemy
print("-----ARENA COMBAT-----")

#Creating all of our hero objects

#Creating our normal hero object
hero = Player(name = "WEWOW", health = 9001, speed = 16)

#Creating our shielded hero object
shielded_hero = ShieldedPlayer(name = "WOWEW", health = 14859, speed = 12, shield = 4984)

#Creating all of our enemy objects

#Creating our basic enemy object
basic_enemy = Enemy(type = "Skeleton", health = 180, speed = 5, damage = 27)

#Creating our fast enemy object
fast_enemy = FastEnemy(type = "Goblin", health = 270, speed = 50)

#Creating our boss enemy object
boss_enemy = BossEnemy(type = "BEGOWOWUOUR", health = 23858, speed = 2, damage = 1000,
                       ability = "Energy Bomb (ITS REALLY BIG)", ability2 = "Health Regen at low health")

#Creating our healer enemy object
healer_enemy = HealerEnemy(type = "Evil Mage", health = 1395, speed = 10, heal_power = 389)

players = [hero, shielded_hero]
print("\n----Hero Stats----")

for player in players:
    player.showstats()

enemies = [basic_enemy, fast_enemy, boss_enemy, healer_enemy]
print("\n-----Enemy Stats-----")

for enemy in enemies:
    enemy.showstats()

print("\n-----Enemy Attacks-----")

for enemy in enemies:
    enemy.attack()
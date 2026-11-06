# Monster en speler
monster_health = 150
player_damage = 25

# Houd het aantal aanvallen bij
attack_count = 0

# Val het monster aan totdat het verslagen is
while monster_health > 0:
    monster_health -= player_damage
    attack_count += 1

    # Zorg dat health niet onder 0 komt
    if monster_health < 0:
        monster_health = 0

    print("Monster health:", monster_health)

# Print het aantal aanvallen
print("Monster verslagen!")
print("Aantal aanvallen:", attack_count)
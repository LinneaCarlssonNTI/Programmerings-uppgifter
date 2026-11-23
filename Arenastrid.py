import random

def visa_status(spelare_hp, monster_hp):
    print(f"Spelare: {spelare_hp} HP  |  Monster: {monster_hp} HP")
    print("------------------------------------")

def visa_meny():
    print("1. Svärdhugg")
    print("2. Eldklot")
    print("3. Läkande dryck")

def spelare_drag(val):
    while val != "1" and val != "2" and val != "3":
        val = input("Du behöver välja 1, 2 eller 3") 

    if val == "1":
        skada = random.randint(15, 20)
        print(f"Attacken gjorde {skada} HP i skada")

    elif val == "2":
        träff = random.randint(1, 2)

        if träff == 1:
            skada = 35
            print(f"Attacken gjorde {skada} HP i skada")
        else:
            skada = 0
            print("Attacken missade och gjorde 0 HP i skada")

    else:
        skada = -20
        print("Du dricker en läkande dryck och återställer 20 HP")

    return skada
 

def monstrets_drag():
        skada = random.randint(10, 25)
        print(f"Monstret attackerar dig och gör {skada} HP i skada")

        return skada


spelare_hp = 100
monster_hp = 100

while spelare_hp > 0 and monster_hp > 0:
    visa_status(spelare_hp, monster_hp)
    visa_meny()

    val = input("Vad vill du göra?")

    resultat = spelare_drag(val)
    if resultat > 0:
        monster_hp = monster_hp - resultat
    else:
        spelare_hp = spelare_hp - resultat

    if monster_hp > 0:
        monster_resultat = monstrets_drag()
        spelare_hp = spelare_hp - monster_resultat

    if spelare_hp <= 0:
        print("Monstret dödade dig och vann")
    elif monster_hp <= 0:
        print("Du lyckades döda monstret och vann!")

visa_status(spelare_hp, monster_hp)
        
    




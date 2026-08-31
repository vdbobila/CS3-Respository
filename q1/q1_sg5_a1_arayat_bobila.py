class Hero:
    def __init__(hero,name,health=100):
        hero.name = name
        hero.health = health
    def take_damage(hero,amount):
        hero.health = hero.health - amount
        print(f"{hero.name} took {amount} damage!")
        print(f"{hero.name} health: {hero.health}")

print("You are Arthur, Your Opponent is Morgana!")
print("")

heroOne = Hero("Arthur")
heroTwo = Hero("Morgana")

battlemode = input("Do you wish to fight? (enter Y if yes): ").upper()

if battlemode == "Y":
    herohurt = Hero.take_damage(heroOne,10)
    vhurt = Hero.take_damage(heroTwo,0)
else:
    print("You chose not to fight.")
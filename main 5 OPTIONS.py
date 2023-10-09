u = '1 .RPG'
v = '2 .Shooter'
w = '3. crafting'
x = '4. Mmorpg'
z = '5. Story'

print(u)
print(v)
print(w)
print(x)
print(z)

def main():
    y = ""
    while y != 'q':

        y = input("what is your favorite type of video game?")
        if y == "1":
            rpg_desc()
        elif y == "2":
            shooter_desc()
        elif y == "3":
            crafting_desc()
        elif y == "4":
            mmo_desc()
        elif y == "5":
            story_desc()
        else:
            print('this is incorrect')



def rpg_desc():
    print('RPG’s are kinda okay. Too mundane for me')


def shooter_desc():
    print('shooters are the best I agree. Theres nothing better than destroying people in multiplayer')


def crafting_desc():
    print('Crafting is so bad bro why do you like that? how many hours have you wasted to craft a diamond sword?')


def mmo_desc():
    print('MMORPG ‘s are sick asf. Theres nothing better than Kingdoms of Amular reckoning')


def story_desc():
    print('Story? Like the walking dead? Yea... have fun pressing one button the whole time.')

main()
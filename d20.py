import random
import time


stren = 4
dex = 6
intel = 0
aclass = 5
bonus_to_hit = round(dex/2)
bonus_to_dmg = 0
bad_hp = 1000000


# GET USER INITIATIVE
def get_init():
    init = input('continue? y/n')
    if init == 'y':
        combat()

    elif init == 'n':
        print("goodbye!")

    else:
        print('Invalid!')
        init=input('y/n')
        get_init()
# scrolling *** take it easy ;]
def slowdown():

    for i in range(2):
        time.sleep(.5)
        print("*", end='')
    time.sleep(.5)
    print('*')
    time.sleep(.5)
    print('')


# roll d20 function
def get_roll():
    roll = (random.randint(1, 20) + bonus_to_hit)
    slowdown()
    print("""roll:""", roll - bonus_to_hit, """
             """)
import random
import time


stren = 2
dex = 3
intel = 0
aclass = 5
bonus_to_hit = round(dex/2)
bad_hp = 1000000

items = [('rapier', 1, 0, 0),('longsword', 0, 1, 1)]



def combat():
    global stren
    global bad_hp

    def get_roll():
        roll = (random.randint(1, 20) + bonus_to_hit)
        print("""
             roll:""", roll - bonus_to_hit, """
             """)
        return roll
    roll = get_roll()


    print("strength, dex:", stren, dex,)
    print("enemy armor class:", aclass)
    print('to hit: ', aclass+7)

    time.sleep(2)

## ROLL TO HIT
    #miss condition
    if roll > 7:
        print("roll+bonus to hit:", roll)
    if roll < 7:
        get_hit = 0
        print("miss!")
    elif roll > 7 and roll - aclass < 7:
        get_hit=0
        print('Your blow was deflected!')
    #critical hit condition
    elif roll == 20:
        get_hit = 2
        print('Critical hit!')
    ##critical miss condition
    elif roll == 1:
        get_hit = 0
        print('critical miss!')
    #hit condition
    else:
        get_hit = 1
        print('Hit!')


#CRITICALS
        time.sleep(2)


    if roll == 1:
        print("Critical miss!")
        time.sleep(2)


### APPLYING DAMAGE
    def get_damage():
        if get_hit == 3:
            return 0
        else:
            damage = (get_hit * (stren + random.randint(1,6)))
        print('hit for: ', damage, '  hit bonus (',get_hit, ') * (strength [', stren,'] + 1d6 (',round((damage / get_hit)-stren),')')
        return damage

    if get_hit==1:
        bad_hp = bad_hp - get_damage()


    time.sleep(2)


    print('enemy hp:', bad_hp)
    print("""
  ***
  """)


### GET USER INITIATIVE
    init = input('continue? y/n')
    if init == 'y':
        combat()
    elif init == 'n':
        print("goodbye!")
    else:
        print('Invalid!')
        init=input('y/n')


print(bad_hp)

combat()

print('test')
    return roll



# INVENTORY SYSTEM V0.1 very minimal so far, format is: ('itemname, +to hit, +to dmg, item id# to help me later on.)
items = (('rapier', 2, 0, 0),('longsword', 0, 1, 1))

choose = input('will you wield a [l]ongsword or a [r]apier?')
def get_equip(choose):
    if choose == 'l':
        equipped = list(items[1])
    if choose == 'r':
        equipped = list(items[0])
    return equipped

equipped = get_equip(choose)
print('equipped: ', (equipped[0]))
bonus_to_hit = bonus_to_hit + equipped[1]
bonus_to_dmg = bonus_to_dmg + equipped[2]

slowdown()

# GET USER INITIATIVE
def get_init():
    init = input('continue? y/n')
    if init == 'y':
        combat()

    elif init == 'n':
        print("goodbye!")

    else:
        print('Invalid!')
        init=input('y/n')
        get_init(init)
def combat():
    global stren
    global bad_hp

    roll = get_roll()

    print("roll + bonus to hit: ", roll)


# ROLL TO HIT.............get_hit is an integer 0-3 to indicate (critical) hit or (critical) miss
    def get_hit(roll):
    # critical hit condition = 2

        if roll == 20:
            print('Critical hit!')
            return 2
    # miss condition = 0
        if roll < 7:
            print("miss!")
            return 0

    # Armor deflect condition = 0
        if roll > 7 and roll - aclass < 7:

            print('Your blow was deflected!')
            return 0
    #critical miss condition = 3
        if roll == 1:
            print('critical miss!')
            return 3

    #hit condition
        else:

            print('Hit!')

        print("roll+bonus:", roll)
        return 1


    time.sleep(2)
#attention get_hit is both a variable and a function from here on out.
    get_hit=get_hit(roll)



    # APPLYING DAMAGE
    def get_damage(get_hit):
        if get_hit == 3:
            return 0
        else:
            hit_roll = random.randint(1,6)
            damage = round((get_hit * (round(stren/2, 1))+ hit_roll)+bonus_to_dmg)
            print('hit for: ', damage, '  hit multiplier (',get_hit, ') * (strength bonus [',round(stren/2, 1) ,'] + 1d6 [',hit_roll,']) + weapon bonus [',bonus_to_dmg, ']')
            return damage

    if get_hit==1 or get_hit==2:
        bad_hp = bad_hp - get_damage(get_hit)


    slowdown()


    # restart loop
    print('enemy hp:', bad_hp)
    print("""
  ***
  """)
    get_init()




print('enemy hp: ', bad_hp)

combat()
get_init()
print('if you are seeing this, something went wrong or you killed the enemy. good job?')

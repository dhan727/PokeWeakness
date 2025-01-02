# Resists = {}
# Weakness = {}
# Immune = {}
# Regular = {}
class Types(dict):
    def __init__(self, name, normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy):
        self.name = name
        self.normal = normal
        self.fire = fire
        self.water = water
        self.electric = electric
        self.grass = grass
        self.ice = ice
        self.fighting = fighting
        self.poison = poison
        self.ground = ground
        self.flying = flying
        self.psychic = psychic
        self.bug = bug
        self.rock = rock
        self.ghost = ghost
        self.dragon = dragon
        self.dark = dark
        self.steel = steel
        self.fairy = fairy
    def __iter__(self):
        for val in vars(self).values():
            yield(val)
    def returnKeys(self):
        keys = list()
        for key in vars(self).keys():
            keys.append(key)
        return keys
    def printType(self):
        print(f"{self.name}")

normal = Types("normal",1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1)
fire = Types("fire",1,0.5,2,1,0.5,0.5,1,1,2,1,1,0.5,2,1,1,1,0.5,1)
water = Types("water",1,0.5,0.5,2,2,0.5,1,1,1,1,1,1,1,1,1,1,0.5,1)
electric = Types("electric",1,1,1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,0.5,1)
grass = Types("grass",1,2,0.5,0.5,0.5,2,1,2,0.5,2,1,2,1,1,1,1,1,1)
ice = Types("ice",1,2,1,1,1,0.5,2,1,1,1,1,1,2,1,1,1,2,1)
fighting = Types("fighting",1,1,1,1,1,1,1,1,1,2,2,0.5,0.5,1,1,0.5,1,2)
poison = Types("poison",1,1,1,1,0.5,1,0.5,0.5,2,1,2,0.5,1,1,1,1,1,0.5)
ground = Types("ground",1,1,2,0,2,2,1,0.5,1,1,1,1,0.5,1,1,1,1,1)
flying = Types("flying",1,1,1,2,0.5,2,0.5,1,0,1,1,0.5,2,1,1,1,1,1)
psychic = Types("psychic",1,1,1,1,1,1,0.5,1,1,1,0.5,2,1,2,1,2,1,1)
bug = Types("bug",1,2,1,1,0.5,1,0.5,1,0.5,2,1,1,2,1,1,1,1,1)
rock = Types("rock",0.5,0.5,2,1,2,1,2,0.5,2,0.5,1,1,1,1,1,1,2,1)
ghost = Types("ghost",0,1,1,1,1,1,0,0.5,1,1,1,0.5,1,2,1,2,1,1)
dragon = Types("dragon",1,0.5,0.5,0.5,0.5,2,1,1,1,1,1,1,1,1,2,1,1,2)
dark = Types("dark",1,1,1,1,1,1,2,1,1,1,0,2,1,0.5,1,0.5,1,2)
steel = Types("steel",0.5,2,1,1,0.5,0.5,2,0,2,0.5,0.5,0.5,0.5,1,0.5,1,0.5,0.5)
fairy = Types("fairy",1,1,1,1,1,1,0.5,2,1,1,1,0.5,1,1,0,0.5,2,1)

def pokemonWeakness(name,type1,type2):
    L1 = list()
    L2 = list()
    L3 = list()
    for i in type1:
        L1.append(i)
    L1.pop(0)
    #if only 1 type
    if type2 == 0: 
        L1.insert(0,name)
        return L1 
    for j in type2:
        L2.append(j)
    L2.pop(0)
    L3 = [x * y for x,y in zip(L1,L2)]
    L3.insert(0,name) 
    return L3



def main():
    with open("pokemon.tsv") as infile:
        for line in infile:
            line = line.strip()
            fields = line.split(',')
            name = fields[0]
            form = fields[1]
            type1 = fields[2]
            type2 = fields[3]
            pokemon = 














    test = pokemonWeakness("Klefki",steel,fairy) #correct
    test1 = pokemonWeakness("Charmander",fire,0)
    # print(len(test1))
    # print(normal.returnKeys()[1])
    weaknesses = {}
    for i in range(len(test1)):
        weaknesses.update({normal.returnKeys()[i] : test1[i]})
    print(weaknesses)    


if __name__ == "__main__": main()
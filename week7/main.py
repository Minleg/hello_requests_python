from animals import cat # import module_name imports everything - classes, variables, functions, refer these things from that module by using modulename.thing
from animals.bird import Bird # import Bird class from bird module
from animals.ninebandedarmadillo import NineBandedArmadillo as Armadillo # using alias when module name is long or when we have conflicting names of modules

def main():
    
    # imported whole module
    kitten = cat.Cat('Kitty') # modulename.thing
    kitten.make_sound()
    
    # import class Bird from bird module
    penguin = Bird('Penguin') # uses classname directly
    penguin.make_sound()
    
    armadillo = Armadillo('Armadillo')
    armadillo.make_sound()
    

if __name__ == '__main__':
    main()
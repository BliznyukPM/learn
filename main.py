# batle 2 warrior
import random
#функция монетка для определения жребия
def coin():
    b = random.randint(1,4)
    print(b)
    if b % 2 == 0:
        return (True)
    else:
        return (False)
# create  class Warrior
class Warrior:
    #выставляем очки жизни
    def sethealth(self,n):
        self.health = n
    #смотрим очки жизни
    def gethealth(self):
        try:
            return self.health
        except:
            print("error1")
    #применяем повреждения
    def damage(self, damagein):
        self.health=self.health-damagein
    #определяем статус жив или мертв
    def status(self):
        if self.health>0:
            return ("live")
        else:
            return ("dead")
# create 2 unit class Warrior
unit1 = Warrior()
unit2 = Warrior()
unit1.sethealth(100)
unit2.sethealth(100)
while unit1.status()=='live' and unit2.status()=='live':
    coin()
    if coin()==True:
        unit1.gethealth()
        print("Юнит1 имеет",unit1.gethealth(),"очков")
        print("юнит2 наносит удар")
        unit1.damage(20)
        print("Юнит1 получает 20 очков урона")
        print("У юнита1 осталось",unit1.gethealth(),"очков")
    else:
        unit2.gethealth()
        print("Юнит2 имеет",unit2.gethealth(),"очков")
        print("юнит1 наносит удар")
        unit2.damage(20)
        print("Юнит2 получает 20 очков урона")
        print("У юнита2 осталось",unit2.gethealth(),"очков")

if unit1.status()=='dead':
    print("Юнит1 убит, Юнит2 выиграл")
else:
    print("Юнит2 убит, Юнит1 выиграл")
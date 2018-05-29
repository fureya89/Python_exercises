class Czlowiek:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        self.diff = 0

    def count_bmi(self):
        if self.bmi < 18.5:
            print("{}, masz niedowagę: ".format(self.name))
        elif 25 > self.bmi >= 18.5:
            print("{}, masz prawidłową wagę: ".format(self.name))
        elif 30 > self.bmi >= 25:
            print("{}, masz nadwagę: ".format(self.name))
        else:
            print("{}, jesteś otyły: ".format(self.name))
        print("Twoje BMI wynosi:" + str(self.bmi))

    def diff_to_norm(self):
        if self.bmi < 18.5:
            best_weight = 18.5 * ((self.height / 100) ** 2)
            self.diff = round(best_weight-self.weight, 2)
            print("Przytyj minimum {} kg by mieć prawidłową wagę!".format(self.diff))
        elif self.bmi >= 25:
            best_weight2 = 25 * (((self.height) / 100) ** 2)
            self.diff = round(self.weight - best_weight2, 2)
            print("Schudnij minimum {} kg by mieć prawidłową wagę!".format(self.diff))
        else:
            print("Waga w normie! Tak trzymaj!")

    def to_burn(self):
        calories = self.diff*6000
        to_run = round(calories/600, 2)
        to_cycle = round(calories/500, 2)
        to_hobby = round(calories/250, 2)
        to_chess = round(calories/150, 2)
        print("{}, aby schudnąć {} kg musisz biegać {}godz. lub jezic na rowere {} godz., uprawiać hobby {} godz. albo grać w szachy {} godz. ".format(self.name, self.diff, to_run, to_cycle, to_hobby, to_chess))

    def to_eat(self):
        calories = self.diff*6000
        chocolate = round(calories*100/450, 2)
        potatoes = round(calories*100/80, 2)
        print("{}, aby przytyć o {} kg musisz zjeść {} g czekolady lub {} g ziemniaków "
              .format(self.name, self.diff, chocolate, potatoes))

    def what_to_do(self):
        if self.bmi >= 25:
            self.to_burn()
        elif self.bmi < 18.5:
            self.to_eat()
        else:
            print("Waga prawidłowa. Nic nie musisz robić")

kasia = Czlowiek("Kasia", 165, 70)
kasia.count_bmi()
kasia.diff_to_norm()
kasia.what_to_do()

basia = Czlowiek("Basia", 165, 45)
basia.count_bmi()
basia.diff_to_norm()
basia.what_to_do()










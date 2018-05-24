from random import randint

def quiz(rangeRandomNumber, numberOfShots):
    random_number = randint(1, rangeRandomNumber)
    print(random_number)  # displaying a random number - for testing
    next = True
    temp = numberOfShots

    while next:
        liczba = int(input("Podaj liczbe z przedzialu 1-100\n"))
        if liczba != random_number:
            numberOfShots -= 1
            if numberOfShots > 0:
                print("To nie jest ta liczba! Pozostało {} próby".format(numberOfShots))
            else:
                print("Skończyły sie próby!")
                next = False
        else:
            print("Brawo! odgadłeś liczbę w {} kroku!".format(temp-numberOfShots+1))
            next = False


nextGame = True
isNextGame = True
print("Witaj użytkowniku! Przed Tobą gra polegająca na zgadywaniu liczby!")

while isNextGame:
    while nextGame:
        print("Wybierz opcje gry:")
        print("a) losujesz liczbę z przedziału od 1 do 100 w pięciu krokach - wpisz 'a'")
        print("b) losujesz liczbę z przedziału od 1 do 1000 w siedmiu krokach - wpisz 'b'")
        option = str(input("Wybieram opcję: "))

        if option == 'a':
            quiz(101, 5)
            nextGame = False
        elif option == 'b':
            quiz(1001, 7)
            nextGame = False
        else:
            print("Nie wpisałeś opcji 'a' bądź 'b'")

    choice = input("Czy chcesz grać jeszcze raz? t/n: ")

    if choice == 't':
        isNextGame = True
        nextGame = True
    elif choice == 'n':
        print("Żegnaj!")
        isNextGame = False
    else:
        print("Wpisz 'n' albo 't'")




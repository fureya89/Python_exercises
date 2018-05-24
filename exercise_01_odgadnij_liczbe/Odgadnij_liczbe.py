from random import randint

gameSummary = {'numberOfGames':1, 'wonGames':0, 'lostGames':0 }


def quiz(rangeRandomNumber, numberOfShots):
    randomNumber = randint(1, rangeRandomNumber)
    print("Wylosowana liczba: {} - do testów".format(randomNumber))  # displaying a random number - for testing
    nextShot = True
    temp = numberOfShots

    while nextShot:
        number = int(input("Podaj liczbe z przedzialu 1-100\n"))
        if number != randomNumber:
            numberOfShots -= 1
            if numberOfShots > 0:
                if number > randomNumber:
                    print("podałeś za dużą liczbę. Spróbuj jeszcze raz. Pozostało {} próby".format(numberOfShots))
                if number < randomNumber:
                    print("podałeś za małą liczbę. Spróbuj jeszcze raz. Pozostało {} próby".format(numberOfShots))
            else:
                print("Skończyły sie próby!")
                gameSummary['lostGames'] += 1
                nextShot = False
        else:
            print("Brawo! odgadłeś liczbę w {} kroku!".format(temp-numberOfShots+1))
            gameSummary['wonGames'] += 1
            nextShot = False


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
        gameSummary['numberOfGames']+=1
        isNextGame = True
        nextGame = True
    elif choice == 'n':
        print("Żegnaj!")
        isNextGame = False
    else:
        print("Wpisz 'n' albo 't'")

print("Dziękujemy za grę! Rozegrałeś {} parti w tym {} wygrałeś a {} przegrałeś!".format(gameSummary['numberOfGames'], gameSummary['wonGames'], gameSummary['lostGames']))
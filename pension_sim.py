import os

os.system('cls')
print("Hej och välkommen till Pension Simulator")
print("Syftet med denna simulator är för att se hur länge du har kvar till pension.")
print("Vi räknar med att man går på pension när man är 65år.")
print("I denna simulator kan man även se hur mycket pengar man har efter ex antal månader man har sparat.")
print("Så till exempel har du sparat 500kr i månaden i 40år då ska du få svaret 20 000kr")
print("\n")
print("Låt oss börja!")

name = str(input("Vi börjar med ditt namn. \nVad heter du: "))

try:
    os.system('cls')
    age = int(input(f"Hej {name}! \nhur gammal är du: "))
    money_saved = int(input("Hur mycket pengar har du lagt undan i månaden? \nSumma: "))
except ValueError:
    print("Felaktig inmatning. Ålder och sparad summa måste vara nummer.")
    exit()

pension = 65

def pension_calc():

    if age < pension:
        os.system('cls')
        save_age = age
        years_left = pension - age

        test_age = save_age + years_left

        total_savings = test_age * money_saved
        print(f"Du har {years_left}år kvar!")
        print(f"När du går i pension har {total_savings}kr sparat! Bra jobbat!")
        input("Tryck Enter för att avsluta")

    elif age == pension:
        os.system('cls')
        total_savings = pension * money_saved
        print("Du är vid pensionsåldern!")
        print(f"Du har sparat {total_savings} kr! Bra jobbat!")
        input("Tryck Enter för att avsluta")

    else:
        os.system('cls')
        total_savings = age * money_saved
        print("Vi rekommenderar att du går i pension.")
        print(f"Eftersom din ålder är över 65 år har du sparat {total_savings}kr. Bra jobbat!")
        input("Tryck Enter för att avsluta")

pension_calc()
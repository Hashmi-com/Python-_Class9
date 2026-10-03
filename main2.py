print("Welcome to ride builder")
print("Step 1: Pick your vehicle")
print ("1. Car\n2.Bike")
UI = int(input("Choose 1 or 2"))

if UI == 1:
    print("Step 2: Pick your car type")
    print("1. Sedan")
    print("2. SUV")
    UI2 = int(input("Choose 1 or 2"))
    if UI2 == 1:
        print("You picked: Sedan")
        print("Seats: 5 passengers")
        print("Famliy type: famliy roadtrips")
    else:
        print("You picked: SUV")
        print("Seats: 7 passengers")
        print("Famliy type: Off road adventures")
else:
     print("Step 2: Pick your bike type")
     print("1. Scooty")
     print("2. Mountain bike")
     UI3 = int(input("Choose 1 or 2"))
     if UI3 == 1:
             print("You picked: Scooty")
             print("Top speed: 80 kmph")
             print("Best for: City roads")
     else:
        print("You picked: Mountain Bike")
        print("Top speed: 40kmph")
        print("Best for off-road trails")
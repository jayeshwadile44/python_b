# This was introduced in python 3.10

a = int ( input ("Enter number between 1 and 10: "))

match a:
    case 1:
        print("You won a lottery")
    case 2:
        print("You won a Charger")
    case 3:
        print("You won a gift")
    case _:
        print("Better Luck next time")

Status = 404

match Status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")
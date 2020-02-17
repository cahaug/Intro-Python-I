# This code deteremines if a user-inputted number is likely to be prime or not
def is_prime(x):
    if x == 2:
        return True
    elif x == 3:
        return True
    elif x == 5:
        return True
    elif x == 7:
        return True
    elif x == 11:
        return True
    elif x == 13:
        return True
    elif x == 17:
        return True
    elif x == 19:
        return True
    elif x == 23:
        return True
    elif x == 29:
        return True
    elif x % 2 == 0:
        return False
    elif x % 3 == 0:
        return False
    elif x % 5 == 0:
        return False
    elif x % 7 == 0:
        return False
    elif x % 9 == 0:
        return False
    elif x % 11 == 0:
        return False
    elif x % 13 == 0:
        return False
    elif x % 17 == 0:
        return False
    elif x % 19 == 0:
        return False
    elif x % 23 == 0:
        return False
    elif x % 29 == 0:
        return False
    else:
        return True
    
print("Is this Integer a Prime Number?")
x = input("Enter an integer: ")
x = int(x)
is_prime(x)
if is_prime(x):
    print("Likely Prime!")
else:
    print("Not Prime!")
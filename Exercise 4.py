print("Please choose an equation")
print([1], "PV = nRT", "~ ideal gas equation")
print([2], "Vf = Vi + at", "~ free-fall")
print([3], "Exit")

equation = int(input("Enter the number that corresponds to the equation: "))
if equation == 1:
    print("You chose PV = nRT")
    print([81], "P")
    print([82], "V")
    print([83], "n")
    print([84], "R")
    print([85], "T")
    print([86], "Exit")
    print("Choose from the following a variable to compute for [choose only one]")
    variable = int(input("Enter numbers 81-86: "))
    if variable == 81:
        V = int(input("Value for variable V: "))
        n = int(input("Value for variable n: "))
        R = int(input("Value for variable R: "))
        T = int(input("Value for variable T: "))
        P = ((n * R) * T) // V
        print("P = ", P)
    elif variable == 82:
        P = int(input("Value for variable P"))
        n = int(input("Value for variable n"))
        R = int(input("Value for variable R"))
        T = int(input("Value for variable T"))
        V = ((n * R) * T) // P
        print("V = ", V)
    elif variable == 83:
        P = int(input("Value for variable P"))
        V = int(input("Value for variable V"))
        R = int(input("Value for variable R"))
        T = int(input("Value for variable T"))
        n = ((P * V) // (R * T))
        print("n = ", n)
    elif variable == 84:
        P = int(input("Value for variable P"))
        V = int(input("Value for variable V"))
        n = int(input("Value for variable n"))
        T = int(input("Value for variable T"))
        R = ((P * V) // (n * T))
        print("R = ", R)
    elif variable == 85:
        P = int(input("Value for variable P"))
        V = int(input("Value for variable V"))
        n = int(input("Value for variable n"))
        R = int(input("Value for variable R"))
        T = ((P * V) // (n * R))
        print("T = ", T)
    elif variable == 86:
        # go back to formula selection
    # else:
        print("please select another number")
        # go back to variable selection
elif equation == 2:
    print("You chose Vf = Vi + at")
    print([91], "Vf")
    print([92], "Vi")
    print([93], "a")
    print([94], "t")
    print([95], "Exit")
    print("Choose from the following a variable to compute for [choose only one]")
    variable = int(input("Enter numbers 91-95: "))
    if variable == 91:
        Vi = int(input("Value for variable Vi: "))
        a = int(input("Value for variable a: "))
        t = int(input("Value for variable t: "))
        Vf = (Vi + (a * t))
        print("Vf = ", Vf)
    elif variable == 92:
        Vf = int(input("Value for variable Vf: "))
        a = int(input("Value for variable a: "))
        t = int(input("Value for variable t: "))
        Vi = (Vf // (a * t))
        print("Vi = ", Vi)
    elif variable == 93:
        Vi = int(input("Value for variable Vi: "))
        Vf = int(input("Value for variable Vf: "))
        t = int(input("Value for variable t: "))
        a = ((Vf - Vi) // t)
        print("a = ", a)
    elif variable == 94:
        Vi = int(input("Value for variable Vi: "))
        Vf = int(input("Value for variable Vf: "))
        a = int(input("Value for variable a: "))
        t = ((Vf - Vi) // a)
        print("t = ", t)
    elif variable == 95:
        # go back to formula selection
    # else:
        print("please select another number")
            # go back to variable selection
elif equation == 3:
    print("Exit")
else:
    print("Please choose between 1-3")


print("Press 4 to go back to formula selection")
# put loop back to formula selection here
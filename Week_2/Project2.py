#Polynomials Calculator

#Cubic Equation
def cube_root(x):
    return x**(1/3) if x >= 0 else -(-x)**(1/3)

def cubic():
    print("\nCubic Equation Root Calculator \nLet's Start.\n")

    A= float(input("Coefficient of x^3: "))
    B= float(input("Coefficient of x^2: "))
    C= float(input("Coefficient of x: "))
    D= float(input("Constant(coefficient of x^0): "))

    if A == 0:
        print("Not a cubic equation.")
        return

    # Convert to depressed cubic form: t^3 + pt + q = 0
    p = (3*A*C - B**2) / (3*A**2)
    q = (2*B**3 - 9*A*B*C + 27*A**2*D) / (27*A**3)
    delta = (q**2) / 4 + (p**3) / 27

    if delta > 0:
        # One real root, two complex
        u = cube_root(-q/2 + delta**0.5)
        v = cube_root(-q/2 - delta**0.5)
        root1 = u + v - B / (3*A)
        print("One real root:", root1)
    elif delta == 0:
        # All real roots, at least two equal
        root1 = 2 * cube_root(-q/2) - B / (3*A)
        root2 = -cube_root(-q/2) - B / (3*A)
        print("Two or three equal real roots:", root1, root2)
    else:
        # Three distinct real roots using trigonometry
        r = (-p/3) ** 0.5
        theta = (1/3) * (q / (2 * r**3)).Acos()
        root1 = 2 * r * (theta).cos() - B / (3*A)
        root2 = 2 * r * ((theta + 2*3.14159/3).cos()) - B / (3*A)
        root3 = 2 * r * ((theta + 4*3.14159/3).cos()) - B / (3*A)
        print("Three real roots:", root1, root2, root3)

    #Returning to the beginning
    r= int(input("\n Press 1 to return and any key to quit "))
    if r == 1:
        start()
    else:
        print("Thanks for using this calculator. :)")



#Quartic Equation
def quartic():
    print("\nQuaritc Equation Root Calculator. \nLet's Start.\n")

    
    
    #Returning to the beginning   
    r= int(input("\n Press 1 to return and any key to quit "))
    if r == 1:
        start()
    else:
        print("Thanks for using this calculator. :)")

    

#Quadratic
def quadratic():
    print("\nQuadratic Equation Root Calculator. \nLet's Start.\n")

    A= float(input("Coefficient of x^2: "))
    B= float(input("Coefficient of x: "))
    C= float(input("Coefficient of x^0 (constant): "))
    
    
    root1= ((-1*(B)) + (B**2 - 4*A*C)**(1/2))/2*A
    root2= ((-1*(B)) - (B**2 - 4*A*C)**(1/2))/2*A
    print("Your roots are, ", root1, root2)

    #Returning to the beginning
    r= int(input("\nPress 1 to return and any key to quit "))
    if r == 1:
        start()
    else:
        print("Thanks for using this calculator. :)")




#Starting Screen
def start():
    calc= int(input("\n--------------------------------------------\nWelcome to the Polynomials Calculator. \n We have 3 Calculators available. \n Cubic(type 1) \n Quartic(type 2) \n Quadratic(type 3). \n press 0 to quit. "))
    if calc == 1:
        cubic()
    if calc == 2:
        quartic()
    if calc == 3:
        quadratic()
    if calc == 0:
        print("Have a good day!")
    else:
        print("invalid number. try again")
        start()

start()   
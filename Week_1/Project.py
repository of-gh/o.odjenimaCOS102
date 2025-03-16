#Multi Money Calculator

#Simple Interest
def smplint():
    print("\nSimple Interest Calculator. \nLet's Start.\n")

    P= int(input("What is your Principal? "))
    R= float(input("What is your Rate?(to 1 dp) "))
    T= int(input("How long is this for? (in years) "))

    A = P*(1+(R/100)*T)
    print("Your Simple Interest is,", A )
    
    #Returning to the beginning
    r= int(input("\n Press 1 to return and any key to quit "))
    if r == 1:
        start()
    else:
        print("Thanks for using this calculator. :)")



#Compound Interest
def cmpdint():
    print("\nCompund Interest Calculator. \nLet's Start.\n")

    P= int(input("What is your Principal? "))
    R= float(input("What is your Rate?(to 1 dp) "))
    T= int(input("How long is this for? (in years) "))
    n= int(input("Enter the number of times to compound yearly "))

    A= (P*(1 + (R/n)))^(n*T)
    print("Your Compound Interest is,", A)
    
    #Returning to the beginning   
    r= int(input("\n Press 1 to return and any key to quit "))
    if r == 1:
        start()
    else:
        print("Thanks for using this calculator. :)")

    

#Annuity Plan
def antypln():
    print("\nAnnuity Plan Calculator. \nLet's Start.\n")

    PMT= int(input("Enter the amount of each annuity payment "))
    P= int(input("What is your Principal? "))
    R= float(input("What is your Rate?(to 1 dp) "))
    T= int(input("How long is this for? (in years) "))
    n= int(input("Enter the number of times to compound yearly "))
    
    #The annuity plan on the slides had an error with the placement of the '1-' and the power 'nt' so I corrected it
    A= (PMT*(1-(1+(R/n))^(-1*n*T)))/(R/n)
    print("Your Annuity is, ",A)

    #Returning to the beginning
    r= int(input("\nPress 1 to return and any key to quit "))
    if r == 1:
        start()
    else:
        print("Thanks for using this calculator. :)")




#Starting Screen
def start():
    calc= int(input("\n--------------------------------------------\nWelcome to the Multi Money Calculator. \n We have 3 Calculators available. \n Simple Interest(type 1) \n Compound Interest(type 2) \n Annuity Plan(type 3). \n press 0 to quit. "))
    if calc == 1:
        smplint()
    if calc == 2:
        cmpdint()
    if calc == 3:
        antypln()
    if calc == 0:
        print("Have a good day!")
    else:
        print("invalid number. try again")
        start()

start()   
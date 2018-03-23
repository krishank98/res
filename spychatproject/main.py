#Objective To create a spychat project and create a file main.py
#Objective Greet the user and ask for his/her name and salutation and print it
#Objective To ask user to create a new user or continue with default and for new user ask name and salutation
#Objective To ask user for his/her age and rating
#Objective Display an appropriate message according to rating

#Greeting the user
print("Welcome to Spy Chat")
print("What's up!")
print("Let's get started")
#Asking user for name
spy_name=input("Please enter your name?\n")
if len(spy_name)>0:
     #Asking user for salutation
    spy_salutation=input("What should we call you (Mr. or Ms.)?\n")
     #Greeting the user again
    print("Alright "+spy_salutation+" "+spy_name+" I\'d like to know a little bit more about you...")
    #Asking the user for his/her age and converting to integer value
    spy_age=int(input("What is your age?\n"))
    #checking if age is valid or not
    if spy_age < 18 and spy_age > 60:
       print("Sorry! your age is not valid to become a spy")
    else:
    # Asking user for rating
        spy_rating = float(input("What is your rating(out of 5?)\n"))
    # checking the range of spy_rating and displaying the message
        if spy_rating > 4.5:
            print("you are very good")
        elif spy_rating >= 3.5 and spy_rating < 4.5:
            print("you are one of good ones")
        elif spy_rating >= 2.5 and spy_rating < 3.5:
             print("you can always do better")
        else:
             print("we can always use somebody to help you in the office")
          # Displaying authentication complete and displaying a welcome message to user
        print("Authentication complete. Welcome " + spy_salutation + "" + spy_name + " age:" + str(spy_age) + " Proud to have you onboard")
else:
    print("Please enter a valid name")













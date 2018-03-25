#Objective To create a spychat project and create a file main.py
#Objective To give user a choice if he want to continue as default or create a new one
#Objective Greet the user and ask for his/her name and salutation and print it
#Objective To ask user to create a new user or continue with default and for new user ask name and salutation
#Objective To ask user for his/her age and rating
#Objective Display an appropriate message according to rating
#Objective For default user import details from spy_details

#importing Spy_details file
import Spy_details

#defining a function menu_choice to display message for default user
def menu_choice(name,salutation,age,rating):
    menu_choice_1="1. To add status\n"+ "2.Quit\n"
    answer = int(input(menu_choice_1))
    while(answer!=2):

      if answer==1:
          status=input("enter status:\n")
          print("%s %s status has been added"%(salutation,name))

      answer = int(input(menu_choice_1))

    print("Quitting")

#asking user if he/she want to create a new user or continue with default
user_choice=input("Do you want to continue as " +Spy_details.default_spy_salutation+Spy_details.default_spy_name+" or create a new one (def or new):\n")

if user_choice=="def":
    menu_choice(Spy_details.default_spy_name,Spy_details.default_spy_salutation,Spy_details.default_spy_age,Spy_details.default_spy_rating)
elif user_choice=="new":
    #Greeting the user
    print("Welcome to Spy Chat")
    print("What's up!")
    print("Let's get started")
   #Asking user for name
    spy_name=input("Please enter your name?\n")
    #validating user name
    if len(spy_name)>0:
        #Asking user for salutation
         spy_salutation=input("What should we call you (Mr. or Ms.)?\n")
        #Greeting the user again
         print("Alright "+spy_salutation+" "+spy_name+" I\'d like to know a little bit more about you...")
         #Asking the user for his/her age and converting to integer value
         spy_age=int(input("What is your age?\n"))
         #checking if age is valid or not
         if spy_age > 18 and spy_age < 60:
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
             print("Authentication complete. Welcome %s %s age: %d Proud to have you onboard"%(spy_salutation,spy_name,spy_age))

         else:
             print("Sorry! your age is not valid to become a spy")

    else:
         print("Please enter a valid name")
else:
    print("please enter right choice")












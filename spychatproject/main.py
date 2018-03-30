#Objective To create a spychat project and create a file main.py
#Objective To give user a choice if he want to continue as default or create a new one
#Objective Greet the user and ask for his/her name and salutation and print it
#Objective To ask user to create a new user or continue with default and for new user ask name and salutation
#Objective To ask user for his/her age and rating
#Objective Display an appropriate message according to rating
#Objective For default user import details from spy_details

#importing Spy_details file
import Spy_details

status_messages=['Busy at office','Watching movie','Surfing web']
Friends_name=[]
Friends_age=[]
Friends_rating=[]
Friends_is_online=[]
def add_status(current_status):
    updated_status=None
    if len(current_status)>0:
        print("You current status is:\n"+current_status)
    else:
        print("you didn't enter any status")
    choice=input("do you want to select status from you old status or add a new one ?(old/new):\n")
    if choice.lower()=='old':
        count=0;
        for message in status_messages:
            print(str(count+1) + " ." + message)
            count=count+1
        status_choice=int(input("Select status you want to set\n"))
        new_status=status_messages[status_choice-1]
        return new_status
    else :
        updated_status=input("enter status:\n")
        if len(updated_status)>0:
            status_messages.append(updated_status)
            print("new status has been added\n")
        else:
            print("please enter a valid status")
    return updated_status

def add_friend():
    friend_name=input("enter you friend_name:\n")
    friend_salutation=input("mr. or ms.:\n")
    new_name=friend_salutation+" "+friend_name
    friend_age=int(input("what is age of your friend:\n"))
    friend_rating=float(input("what is rating of your friend:\n"))
    if len(friend_name)> 0 and friend_age >17 and friend_rating>0:
        Friends_name.append(new_name)
        Friends_age.append(friend_age)
        Friends_rating.append(Friends_rating)
        Friends_is_online.append(True)
    else:
        print("Please enter right details")
    return len(new_name)

#defining a function menu_choice to display message for default user
def start_chat(name,salutation,age,rating):
    menu_choice="1.Add a status update\n"+"2.Add a friend\n"+"3.Send a secret message\n"+"4.Read a secret messsage\n"+"5.Read chat from a user\n"+"6.Close Application\n"+"Enter choice:\n"

    current = ""
    answer = int(input(menu_choice))

    continue_app=True
    while(continue_app):
      if answer==1:
          current= add_status(current)
          print('status"'+current+'"'+"has been set\n")

          print("%s %s status has been added"%(salutation,name))
      elif answer==2:
          add_friend()
      elif answer==6:
          continue_app=False

      answer = int(input(menu_choice))

    print("Quitting")

#asking user if he/she want to create a new user or continue with default
user_choice=input("Do you want to continue as " +Spy_details.default_spy_salutation+Spy_details.default_spy_name+" or create a new one (def or new):\n")

if user_choice.lower()=="def":
    start_chat(Spy_details.default_spy_name,Spy_details.default_spy_salutation,Spy_details.default_spy_age,Spy_details.default_spy_rating)
elif user_choice.lower()=="new":
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

             start_chat(spy_name,spy_salutation,spy_age,spy_rating)

         else:
             print("Sorry! your age is not valid to become a spy")

    else:
         print("Please enter a valid name")
else:
    print("please enter right choice")












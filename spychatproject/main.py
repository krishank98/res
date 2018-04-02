#Objective To create a spychat project and create a file main.py
#Objective To give user a choice if he want to continue as default or create a new one
#Objective Greet the user and ask for his/her name and salutation and print it
#Objective To ask user to create a new user or continue with default and for new user ask name and salutation
#Objective To ask user for his/her age and rating
#Objective Display an appropriate message according to rating
#Objective For default user import details from spy_details

#importing Spy_details file

from Spy_details import default_spy
from steganography.steganography import Steganography
import datetime

status_messages=['Busy at office','Watching movie','Surfing web']

Friends=[]


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
    new_friend = {
        'name':'',
        'salutation':'' ,
        'age':'',
        'rating':'',

    }
    new_friend['name']=input("enter you friend_name:\n")
    new_friend['salutation']=input("Mr. or Ms. :\n")
    new_friend['name']=new_friend['name']+" "+new_friend['salutation']
    new_friend['age']=int(input("what is age of your friend:\n"))
    new_friend['rating']=float(input("what is rating of your friend:\n"))
    if len(new_friend['name'])> 0 and new_friend['age'] >17 and new_friend['rating']>0:
        Friends.append(new_friend)

    else:
        print("Please enter right details")
    return len(Friends)


def select_a_friend() :
  item_number = 0

  for friend in Friends:
    print ("%d  %s" % ((item_number + 1), friend['name']))

    item_number = item_number + 1

  friend_choice = int(input("Choose from your friends"))
  friend_choice_position = friend_choice - 1

  return friend_choice_position


def send_message():
  friend_choice = select_a_friend()

  original_image = input("What is the name of the image?")
  output_path = 'fib1.png'
  text = input("What do you want to say?")
  Steganography.encode(original_image, output_path, text)
  new_chat = {
      "message": text,
      "time": datetime.now(),
      "sent_by_me": True
  }

  Friends[friend_choice]['chats'].append(new_chat)
  print ("Your secret message is ready!")


def read_message():
  sender = select_a_friend()

  output_path = input("What is the name of the file?")
  secret_text = Steganography.decode(output_path)
  new_chat = {
      "message": secret_text,
      "time": datetime.now(),
      "sent_by_me": False
  }

  friend[sender]['chats'].append(new_chat)
  print ("Your secret message has been saved!")


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
          number_of_friends=add_friend()
          print("you have %d friends"%(number_of_friends))
      elif answer==3 :
          send_message()
      elif answer==4 :
          read_message()

      elif answer==6:
          continue_app=False

      answer = int(input(menu_choice))

    print("Quitting")

#asking user if he/she want to create a new user or continue with default
user_choice=input("Do you want to continue as " +default_spy['salutation']+default_spy['name']+" or create a new one (def or new):\n")

if user_choice.lower()=='def':
    start_chat(default_spy['name'],default_spy['salutation'],default_spy['age'],default_spy['rating'])
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












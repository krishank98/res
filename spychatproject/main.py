#Objective To create a spychat project and create a file main.py
#Objective To give user a choice if he want to continue as default or create a new one
#Objective Greet the user and ask for his/her name and salutation and print it
#Objective To ask user to create a new user or continue with default and for new user ask name and salutation
#Objective To ask user for his/her age and rating
#Objective Display an appropriate message according to rating
#Objective For default user import details from spy_details

#importing Spy_details file

from Spy_details import Spy, ChatMessage,chats,spy,friends

from steganography.steganography import Steganography

from datetime import datetime

import csv

from termcolor import colored



status_messages=['Busy at office','Watching movie','Surfing web']


def add_status(current_status):
    updated_status=None
    if len(current_status)>0:
        print("You current status is:\n"+current_status)
    else:
        print("you didn't enter any status")
    choice=raw_input("do you want to select status from you old status or add a new one ?(old/new):\n")
    if choice.lower()=='old':
        count=0;
        for message in status_messages:
            print(str(count+1) + " ." + message)
            count=count+1
        status_choice=int(raw_input("Select status you want to set\n"))
        new_status=status_messages[status_choice-1]
        return new_status
    else :
        updated_status=raw_input("enter status:\n")
        if len(updated_status)>0:
            status_messages.append(updated_status)
            print("new status has been added\n")
        else:
            print("please enter a valid status")
    return updated_status

def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)

    new_friend.name=raw_input("enter you friend_name:")
    new_friend.salutation=raw_input("Mr. or Ms. :")
    new_friend.age=int(raw_input("what is age of your friend:"))
    new_friend.rating=float(raw_input("what is rating of your friend:"))
    if len(new_friend.name)> 0 and new_friend.age >17 and new_friend.rating>0:

        friends.append(new_friend)
        with open("friends.csv", "a") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating, new_friend.is_online])

    else:
        print("Please enter right details")

    return len(friends)

def select_a_friend() :
  item_number = 0

  for friend in friends:
    print ("%d  %s" % ((item_number + 1), friend.name))

    item_number = item_number + 1

  friend_choice = int(raw_input("Choose from your friends:"))
  friend_choice_position = friend_choice - 1

  return friend_choice_position

special_words = ['SAVE ME', 'SOS' , 'HELP']

def send_message():
  friend_choice = friends[select_a_friend()].name


  original_image = raw_input("What is the name of the image?(sample.jpg)")
  output_path = 'output.jpg'
  secret_text = raw_input("What do you want to say?")
  if secret_text in special_words:
      secret_text = colored(secret_text + ": IT'S EMMERGENCY!! Come for help", "red")
  Steganography.encode(original_image, output_path, secret_text)
  new_chat = ChatMessage(spy_name=spy.name, friend_name=friend_choice, time=datetime.now().strftime("%d %B %Y"),message=secret_text)
  chats.append(new_chat)

  print ("Your secret message is ready!")

  with open('chats.csv', 'a') as chats_data:
      writer = csv.writer(chats_data)
      writer.writerow([new_chat.spy_name, new_chat.friend_name, new_chat.time, new_chat.message])

def read_message():
  sender = select_a_friend()


  output_path = raw_input("What is the name of the file?(output.jpg)")
  secret_text_1 = Steganography.decode(output_path)
  print "message is: "+secret_text_1

  chat = ChatMessage(spy_name=spy.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"),message=secret_text_1)
  friends[sender].chats.append(chat)

  with open("chats.csv", 'a') as chat_record:
      writer = csv.writer(chat_record)
      writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])

def readchat(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
            try:
                c = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                if c.spy_name == spy.name and c.friend_name == name_friend:
                    print colored("You sent message to the Spy name: %s " % name_friend, "red")
                    print colored("On Time: [%s]" % c.time, "blue")
                    print("Message: %s" % c.message)
                    return 1
            except IndexError:
                pass
            continue



#defining a function menu_choice to display message for default user

def start_chat(name,salutation,age,rating):



    current_status_message=None


    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=(row[1]), age=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # load_chats() is a function which loads all the chats of spies stored in chats.csv
    def load_chats():
        with open("chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue

    # both functions are called so that chats and list of friends are loaded before its usage
    load_friends()
    load_chats()


    show_menu = True

    menu_choice="1.Add a status update\n"+"2.Add a friend\n"+"3.Send a secret message\n"+"4.Read a secret messsage\n"+"5.Read chat from a user\n"+"6.Close Application\n"+"Enter choice:\n"

    current = ""
    answer = int(raw_input(menu_choice))

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
      elif answer==5:

          print "select a friend whose chat you want to see"
          choice = select_a_friend()
          readchat(choice)
      elif answer==6:
          continue_app=False

      answer = int(input(menu_choice))

    print("Quitting")

#asking user if he/she want to create a new user or continue with default
user_choice=raw_input("Do you want to continue as " +spy.salutation+spy.name+" or create a new one (def or new):\n")

if user_choice.lower()=='def':
    start_chat(spy.name,spy.salutation,spy.age,spy.rating)
elif user_choice.lower()=="new":
    #Greeting the user
    print("Welcome to Spy Chat")
    print("What's up!")
    print("Let's get started")
   #Asking user for name
    spy_name=raw_input("Please enter your name?\n")
    #validating user name
    if len(spy_name)>0:
        #Asking user for salutation
         spy_salutation=raw_input("What should we call you (Mr. or Ms.)?\n")
        #Greeting the user again
         print("Alright "+spy_salutation+" "+spy_name+" I\'d like to know a little bit more about you...")
         #Asking the user for his/her age and converting to integer value
         spy_age=int(raw_input("What is your age?\n"))
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












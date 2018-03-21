#Objective To create a spychat project and create a file main.py
#Objective Greet the user and ask for his/her name and salutation and print it
#Objective To ask user to create a new user or continue with default and for new user ask name and salutation


print("Welcome to Spy Chat")
print("What's up!")
print("Let's get started")
spyname=input("Please enter your name?\n")
salutation=input("What should we call you (Mr. or Ms.)?\n")
print("Alright "+salutation+spyname+" I\'d like to know a little bit more about you...\n")
selection=input("Which user you want to continue with?(new or def)\n")
if selection =="new":
    spyname_1 = input("Please enter user_name:/n")
    salutation_1 = input("What should we call you (Mr. or Ms.)?\n")
    print(salutation_1+spyname_1+",new user has been created")
else:
    exit(0)





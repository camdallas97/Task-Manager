#Defined the function reg user that is called when r is selected by the admin
def reg_user():
  user_password_confirm = False

  new_user = input("Enter your username: ")
  f = open("user.txt", "r+")
  lines = f.read()
  lines = lines.splitlines()

  #Put all the users into a list to be manipulated later
  user_list = []
  for user in lines:
    temp = user.strip()
    temp = user.split(", ")
    user_list.append(temp[0])

  #Used a while loop so that every time the admin entered a username
  #in the list it would repeat until a valid answer was entered 
  while new_user in user_list:
    new_user = input("Enter a non existing username: ")

  #After a non-existing username is entered a while loop is used
  #so that when both passwords are the same it changes the boolean that it
  #will allow the username and password to be registered/written to user.txt 
  while user_password_confirm == False:
    new_password = input("Enter your password: ")  
    confirm_password = input("Confirm your password: ")

    if new_password == confirm_password:
      user_password_confirm = True

    else:
      print()
      print("Password is not the same")
      print()
      
    if user_password_confirm == True:
      f = open("user.txt", "a")
      f.write("\n" + new_user + "," + " " + confirm_password) 
      f.close()
      print()
      print("User Added")

#Defined the function for add_task
#If 'a' is selected a series of questions about the task is prompted to the user
#A final question is prompted if they want to add it which will change the boolean to True
#if yes is selected and will write all the input in a specific order seperated by a ", " to the tasks.txt
#file as it will be split in future use     
def add_task():
  task_conditions_met = False
  while task_conditions_met == False:
    which_user = input("The username of the person to whom the task is assigned: ") 
    title_task = input("The title of the task: ")
    desciption = input("Task desciption: ")
    date_assign = input("The date that the task was assigned to the user in format YYYY-MM-DD: ")
    due_date = input("The due date of the task in format YYYY-MM-DD: ")
    task_completed = "No"
    task_added = input("Are you sure you want to add this task? Yes?/No?/Redo?: ")

    if task_added.capitalize() == "Yes":
      task_conditions_met = True

    elif task_added.capitalize() == "No":
      exit()
  
    elif task_added.capitalize() == "Redo":
      print()
      print("Enter your task")
      print()
      
    else:
      break
      
  if task_conditions_met == True:
    f1 = open("tasks.txt", "a")
    f1.write("\n" + which_user + ", " + title_task + ", " + desciption + ", " + date_assign + ", " + due_date + ", " + task_completed)
    f1.close()
    print()
    print("Task Added")

#Defined the function for view_all that is called when va is selected by the user
#If 'va' is selected, python will loop through the text in tasks.txt that has splitlines()
#and has been split accordingly so that it will print all the tasks with each task formulated
#on a new line and formated in a user frienly way as shown below  
def view_all():
  f1 = open("tasks.txt", "r") 
  lines1 = f1.read()
  lines1 = lines1.splitlines()

  for x in lines1:
    temp1 = x.strip()
    temp1 = x.split(", ")
    print("Task:             {}".format(temp1[1]))
    print("Assigned to:      {}".format(temp1[0]))
    print("Date assigned:    {}".format(temp1[3]))
    print("Due date:         {}".format(temp1[4]))
    print("Task Complete:    {}".format(temp1[5]))
    print("Task Description: {}".format(temp1[2]))
    print()
  f1.close()

#Defined a function for view_mine that is called when the user selects vm
def view_mine():
  f1 = open("tasks.txt", "r+") 
  lines1 = f1.read()
  lines1 = lines1.splitlines()

  task_list = []
  user_task_indexes = []
  task_index = 0
  count = 0

  #The entire file is put into a list to be manipulated later
  for x in lines1:
    temp1 = x.strip()
    temp1 = x.split(", ")
    task_list.append(temp1)

    #when the function is called by the user it will only display the tasks
    #assigned to them using the if statement for the username equaling the index in the list
    #Each time the loop falls on the username a count will go up to be used for numbering the tasks
    #as well as a task index which will also go up
    #
    if username == temp1[0]:
      count += 1
      user_task_indexes.append(task_index)
      print("{}.Task:           {}".format(count,temp1[1]))
      print("Date assigned:    {}".format(temp1[3]))
      print("Due date:         {}".format(temp1[4]))
      print("Task Complete:    {}".format(temp1[5]))
      print("Task Description: {}".format(temp1[2]))
      print()
    task_index += 1

  #The user is then prompted with an edit question but also an option to go back to the main menu
  task_edit = input("Would you like to edit a task? Yes or -1 to go back to main menu: ")
  print()

  #if the user wants to edit a task they are asked to enter the number of the task
  #which was made possible by the count displayed with each task
  #the choice of the task has to be -1 from that value as progamming indexes start at 0
  #Once a task number is given, an edit menu is di
  splayed where there are options for the
  #user, due date or task completion status
  if task_edit.capitalize() == "Yes":
    task_number = int(input("Enter the number of the task you want to edit: "))
    choice = task_number-1
    print()
    edit_menu()
    print()
    edit_option = input("Enter your choice: ")

    #For option 'user', the user can enter in the the new username 
    if edit_option.capitalize() == "User":
      user_change = input("Enter the new user: ")

      #if the task completion status is "yes" then any changes wanted to made will be met with an error message
      if task_list[user_task_indexes[choice]][5].capitalize() == "Yes":
        print("Cannot edit a completed task")

      #otherwise the username will be changed
      else:
        task_list[user_task_indexes[choice]][0] = user_change

      #Because the tasks are in a list, the entire task list is written back to the text file with just that change
      file = open("tasks.txt", "w")
      for x in task_list:
        file.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + x[4] + ", " + x[5] + "\n" )
      file.close()

    #For option 'date', the user can enter in the the new due date in a specific format with the '-' symbol
    elif edit_option.capitalize() == "Date":
      date_change = input("Enter the new date in format YYYY-MM-DD: ")

      #if the task completion status is "yes" then any changes wanted to made will be met with an error message
      if task_list[user_task_indexes[choice]][5].capitalize() == "Yes":
        print("Cannot edit a completed task")

      #otherwise the due date will be changed
      else:
        task_list[user_task_indexes[choice]][4] = date_change

      #Because the tasks are in a list, the entire task list is written back to the text file with just that change
      file = open("tasks.txt", "w")
      for x in task_list:
        file.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + x[4] + ", " + x[5] + "\n" )
      file.close()

    #For option 'task', the user can enter in the the new task completion status  
    elif edit_option.capitalize() == "Task":
      task_change = input("Enter the task completion status Yes/No: ")

       #if the task completion status is "yes" then any changes wanted to made will be met with an error message
      if task_change.capitalize() == "Yes" and task_list[user_task_indexes[choice]][5].capitalize() == "Yes":
        print("Cannot edit a completed task")

      #otherwise the task completion status will be changed
      else:
        task_list[user_task_indexes[choice]][5] = task_change

      #Because the tasks are in a list, the entire task list is written back to the text file with just that change
      file = open("tasks.txt", "w")
      for x in task_list:
        file.write(x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + ", " + x[4] + ", " + x[5].capitalize() + "\n" )
      file.close()
    
  #When the users selects -1 an admin menu will print if the admin is logged in
  #or the user menu will print if a regular user is logged in
  elif task_edit == "-1":

    if admin_status == True:  
      admin_menu()
      menu_option()
    else:
      user_menu()
      menu_option()
  
  f1.close() 

#defined a function for generate reports to be called when the admin selects 'gr'
def generate_reports():

  #imported these functions to be used for the overdue calculation
  from datetime import datetime
  import time
 
  f1 = open("tasks.txt", "r+") 
  line1 = f1.read()
  line1 = line1.splitlines()

  f3 = open("user.txt", "r+") 
  line3 = f3.read()

  complete_counter = 0
  incomplete_counter = 0
  task_list = []

  #once again put the tasks into a list 
  for x in line1:
    temp = x.strip()
    temp = x.split(", ")
    task_list.append(temp)

  #looped through the task list and depending on the condition at index 5
  #would increase one of the counters
  for task_complete in task_list:
    if task_complete[5] == "No":
      incomplete_counter += 1
    if task_complete[5] == "Yes":
      complete_counter += 1

  #for the overdue calculation I created an overdue counter
  #Defined a variable for todays date using the imported functiona that would compare the date at index 4
  #to the current date and depending on that result would increase or not increase the overdue counter 
  overdue_counter = 0
  today = datetime.today().strftime('%Y-%m-%d')
  for z in task_list:
    if z[4] < today and z[5] == "No":
      overdue_counter += 1

  #Below are percentage calculations for the percentage incomplete and percentage overdue
  perc_incomplete = (incomplete_counter/(incomplete_counter + complete_counter))*100
  perc_incomplete = round(perc_incomplete, 2)

  perc_overdue = (overdue_counter/(incomplete_counter + complete_counter))*100
  perc_overdue = round(perc_overdue, 2)

  #Once all the necessary calculations are made they are written to task_overvier.txt
  f2 = open("task_overview.txt", "r+")
  
  f2.write("Total tasks = " + str(incomplete_counter + complete_counter))    
  f2.write("\nTotal completed tasks = " + str(complete_counter))
  f2.write("\nTotal incompleted tasks = " + str(incomplete_counter))
  f2.write("\nTotal incompleted tasks that are overdue = " + str(overdue_counter))
  f2.write("\nThe percetage of tasks incomplete = {}%".format(perc_incomplete))  
  f2.write("\nThe percetage of tasks overdue = {}%".format(perc_overdue))    

  #The calculations below are to made for user_overview.txt
  f1 = open("tasks.txt", "r+") 
  line1 = f1.read()

  #to get the task count all I needed to do was to count the number of lines in tasks.txt
  task_count = 1
  for a in line1:
    temp = a.strip()
    temp = a.split(",")
    if a == "\n":
      task_count += 1

  #used the same logic for the user count in user.txt    
  user_count = 1
  for b in line3:
    temp = b.strip()
    temp = b.split(",")
    if b == "\n":
      user_count += 1
  f3.close

  f3 = open("user.txt", "r+") 
  line3 = f3.read()
  line3 = line3.splitlines()

  #To get stats on each user I first had to put all the users into a list from user.txt
  users = []
  for i in line3:
    temp = i.strip()
    temp = i.split(", ")
    users.append(temp[0])

  #I created an empty list for all the information calculated below that would be written down to the
  #text file once it was completed
  user_statslist = []
  #I looped through each user in the user list through the task list by nesting loops 
  for user in users:
    usertask_count = 0
    usertask_incomplete = 0
    usertask_incomplete_overdue = 0
    #using the same logic in task_overview if certain conditions were met at specific indexes for each user
    #then each user's count for each condition would either go up or remain the same
    for task in task_list:
      if task[0] == user:
        usertask_count += 1
        if task[5] == "No":
          usertask_incomplete += 1
          if task[4] < today:
            usertask_incomplete_overdue += 1

    #The percentages for other conditions were then calculated below using the results from above
    percent_user_tasks = (usertask_count/task_count)*100
    usertask_complete = usertask_count - usertask_incomplete
    percent_user_complete = (usertask_complete/usertask_count)*100
    percent_user_incomplete = (usertask_incomplete/usertask_count)*100  
    percent_user_overdue = (usertask_incomplete_overdue/usertask_incomplete)*100 

    #To make sure it is written to the text file in a user-friendly way the list created in the beginning is used
    #to store each users stats in a neat order and then written out to user_overview.txt
    user_statslist.append([user, usertask_count, percent_user_tasks, percent_user_complete, percent_user_incomplete, percent_user_overdue])

  f4 = open("user_overview.txt", "w")
  
  f4.write("The number of users = " + str(user_count))
  f4.write("\nThe number of tasks = " + str(task_count))

  #looped through the list created to write out the information in a user friendly way
  for user in user_statslist:
    f4.write("\n")
    f4.write("\nUsername = " + user[0]  )       
    f4.write("\nTotal user tasks = " + str(user[1]) )
    f4.write("\nTotal percentage of tasks to user = " + str(user[2]) + "%" )
    f4.write("\nTotal percentage of tasks complete = " + str(user[3]) + "%" )
    f4.write("\nTotal percentage of tasks incomplete = " + str(user[4]) + "%" )
    f4.write("\nTotal percentage of tasks overdue = " + str(user[5]) + "%" )       
   
  f1.close()
  f2.close()
  f3.close()
  f4.close()

#Defined a function for display_statistics to be called when the admin selects 'ds'
def display_statistics():

  #All that happens here is that I store the all information on both text files into 2 variables
  #that will be printed out to the admin when this option is selected
  task_overview_file = open("task_overview.txt", "r")
  task_contents = task_overview_file.read()
  print(task_contents)
  print()

  user_overview_file = open("user_overview.txt", "r")
  user_contents = user_overview_file.read()
  print(user_contents)
  
  task_overview_file.close()
  user_overview_file.close()

#An edit menu function showing the options from which the user can choose in view_mine
def edit_menu():
  print("Select user to edit the user")
  print("Select date to edit the due date")
  print("Select task to edit the task completion status")

#An admin memu fucntion that displays choice text if the admin logs in
def admin_menu():
  print("Welcome Admin!")
  print()  
  print("Please select one of the following options:")
  print("r - register user")
  print("a - add task")
  print("va - view all tasks")
  print("vm - view my tasks")
  print("gr - generate reports")
  print("ds - statistics (Select \"gr\" before \"ds\")")
  print("e - exit")
  print()

#A user memu fucntion that displays choice text if a regular user logs in
def user_menu():
  print("Welcome User!")
  print()  
  print("Please select one of the following options:")
  print("a - add task")
  print("va - view all tasks")
  print("vm - view my tasks")
  print("e - exit")
  print()

#This function is called once a specific user logs in and depending on which type of menu
#was printed out for them , they will select a specific option that will call one of the functions defined above
#the admin will have all the options available as defined in 'admin_status' for extra security
def menu_option():
  option = input("Enter your choice: ") 
  print()
  if option == "r" and admin_status == True:
    reg_user()

  elif option == "a":
    add_task()
  
  elif option == "va": 
    view_all()

  elif option == "vm":
    view_mine()
  
  elif option == "ds" and admin_status == True:
    display_statistics()

  elif option == "gr" and admin_status == True:
    generate_reports()
    
  elif option == "e":
    exit()

  else:
    print("Not a valid choice. Start Again")
  

print("Login!")
print()
admin_status = False
username_password_attempt = False

#Created a while loop for the username and password
#Until the 1 of the conditions is met the loop will repeat  
while username_password_attempt == False :
  username = input("Enter username: ")
  password = input("Enter password: ")
  print()

  f = open("user.txt", "r+")
  line = f.read()
  line = line.splitlines()

  #Created a specific boolean condition for the admin
  #Once that condition is met it will print a menu specifically for the admin
  if username == "admin" and password == "adm1n":
      admin_status = True

  if admin_status == True:  
      admin_menu()

  #Created a for loop to split the words in the text file into a list seperated
  #by the ", " in order to create a temp[0] list and a temp[1] list
  #for username and password respectively so that when both were entered correctly and did
  #not change the condition of 'admin_status' it would print a non-admin menu
  for x in line:
    temp = x.strip()
    temp = x.split(", ")
      
    if username == temp[0] and password == temp[1]:
      username_password_attempt = True
      
  if username_password_attempt == True and admin_status == False:
      user_menu()

  #If both user and admin booleans were not met, the loop is repeated with an error message
  elif username_password_attempt == False and admin_status == False:
      print("Error Try again")
      print()
      f.close()     

menu_option()

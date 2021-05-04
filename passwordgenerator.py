#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#
#               ~Custom Password Generator~
#                     Console Version    
#     Developed By: Stat1cNull and SweetBerry Software
#     Last Update: May 4th 2021
#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#$&#
import random
import os
#Variables
uppercase = 0
lowercase = 0
numbers = 0
available = 0
location = 0
length = 0
special = []#Array for special chars
numchars = 0
pass_num = 0
settings = 0
rand_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890#$&*@!"
num_chars = "1234567890"
clear = lambda: os.system("cls")#Clear out console
#Check if input is a number
def check_int(var, prompt):
  while True:
    var = input(prompt)
    if var.isnumeric():
      return int(var)
      break
    print("Invalid Input, please enter a number")
#Functions
#Custom Random Password Generator
def random_password_gen(uppercase, lowercase, numbers, numchars):
  global special
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
  nums = "1234567890"
  password = ""
  #Generate Password
  for x in range(uppercase):#Pick Uppercase
    password += random.choice(upper)
  for y in range(lowercase):#Pick Lowercase
    password += random.choice(lower)
  for z in range(numbers):#Pick numbers
    password += random.choice(nums)
  for b in range(numchars):#Pick special chars
    password += special[b]
  final = list(password)
  random.shuffle(final)#Shuffle characters in password
  print("".join(final))#Convert List back to string
#Number and Random Password Generator
def simple_pas_gen(chars, number_of_passwords, length, name: str):
  print("Here are your {0} passwords: ".format(name))
  #Generate Passwords
  for x in range(number_of_passwords):
    password = ""#Store password and reset it
    for y in range(length):
      password += random.choice(chars)
    print(password)
#Application
def run_app(): 
  global uppercase, lowercase, numbers, numchars, settings, available, special, pass_num, length
  #Settings
  print("""
  Custom Password Generator
  By DeadAnarch1st
  What do you want your password to be ?
    1. Custom Random Password
    2. Password with Familiar Word(Under Development)
    3. Number Password
    4. Random Password
  """)
  settings = check_int(settings, "Enter your choice: ")
  #Length for Random and Number passwords
  if settings == 1 or settings == 3 or settings == 4:
    length = check_int(length,"How long would you like your password to be ?")
    lowercase = length
    available = length#Amount of characters we can change
    #Number of passwords at a Time
    pass_num = check_int(pass_num, "How many passwords would you like to be generated ?")
    while pass_num == 0:
      if pass_num == 0:
        pass_num = check_int(pass_num, "Input cannot be 0, please try again")
    clear()

  #Settings for Random Password
  if settings == 1:
    print("Length: " + str(length))
    print("Lowercase Letters: " + str(lowercase))
    print("Available Character Spaces: " + str(available))
    uppercase = check_int(uppercase,"How many characters would you like to be uppercase ?")
    #Check if user puts more uppercase chars than available
    if uppercase > available:
      while uppercase > available:
        print("Too many uppercase characters, enter a number less than " + str(available))
        uppercase = check_int(uppercase,"How many characters would you like to be uppercase ?")
    lowercase = lowercase - uppercase
    available = available - uppercase
    clear()

    #Check if there are any available spaces left
    if available > 0:
      print("Length: " + str(length))
      print("Lowercase Letters: " + str(lowercase))
      print("Uppercase Letters: " + str(uppercase))
      print("Available Spaces: " + str(available))
      numbers = check_int(numbers,"How many characters would you like to be numbers ?")
      if numbers > available:
        while numbers > available:
          print("Too many number characters, enter a number less than " + str(available))
          numbers = check_int(numbers,"How many characters would you like to be numbers ?")
      lowercase = lowercase - numbers
      available = available - numbers
      clear()

    if available > 0:
      print("Length: " + str(length))
      print("Lowercase Letters: " + str(lowercase))
      print("Uppercase Letters: " + str(uppercase))
      print("Number Chars: " + str(numbers))
      print("Available Spaces: " + str(available))
      chars = input("Would you like special characters in your password ? yes/no")
      chars = chars.lower()#Convert input into lowercase
      if chars == "yes":#User wants special chars
        numchars = check_int(numchars,"How many special characters would you like ?")
        if numchars > available:#Check if user wants to enter more characters than available
          while numchars > available:#If user is stupid and keeps trying to enter too many chars
            print("Too many special characters, please enter different number")
            numchars = check_int(numchars,"How many special characters would you like ?")
        for x in range(numchars):#Loop for however many special chars user wants
          counter = x + 1
          signs = input("Input your #" + str(counter) + " special character: ")
          special.append(signs)#Store special chars in array
      else:
        pass#Skip
    clear()
    #Show Random Password
    print("Here is your Custom Random Passwords: ")
    for i in range(pass_num):
      random_password_gen(uppercase, lowercase, numbers, numchars)
    run_app()
  #Generate Number Password
  if settings == 3:
    simple_pas_gen(num_chars, pass_num, length, "Number")
    run_app()
  #Generate Random Password
  if settings == 4:
    simple_pas_gen(rand_chars, pass_num, length, "Random")
    run_app()
  #Password with Familiar Word
  if settings == 2:
    location = 0
    word = input("What word do you want to use for your password ?")
    #Check if the word is valid
    w_len = len(word)#Get length of the word
    if w_len < 3 or w_len > 15:
      while w_len < 3 or w_len > 15:
        word = input("Your word is invalid, please enter a word 3 to 15 characters long")
        w_len = len(word)
    available = w_len
    #Settings for the word
    print("Password so far: " + word)
    print("Length of the password: %s" % w_len) 
    print("Available to change: %s" % available)
    uppercase = check_int(uppercase, "How many characters you want to be uppercase ?")
    if uppercase > w_len:
      while uppercase > w_len:
        uppercase = int(input("Invalid number, enter number less than length of the word"))
    available -= uppercase
    #APPLY UPPERCASE SETTINGS TO THE WORD-----------------------
    #THIS CODE HAS BEEN VERY VERY BAD AND HAS BEEN MISBEHAVING DADDY$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    index = list()#index of letters to change
    for x in range(uppercase):#Loop through chars and randomly pick ones to change
      var = random.randint(0, w_len - 1)
      index.append(var)#Pick random number and that number will be index of a char to change
    chan_word = list(word)
    for i in index:#Apply uppercase to the selected characters
      chan_word[i] = chan_word[i].upper()
    password = "".join(chan_word)#Convert from list back to string
    #THIS CODE HAS BEEN VERY VERY BAD AND HAS BEEN MISBEHAVING DADDY###################################################################
    clear()
    print("Password so far: " + password)
    print("Length of the password: %s" % w_len) 
    print("Available to change: %s" % available)
    print("Uppercase characters: %s " % uppercase)
    numbers = check_int(numbers, "How many numbers would you like to add ?")
    print("""
      Where would you like to place numbers in the password:
          #1 In the Front 
          #2 In the Back
          #3 In the Middle
          #4 Randomly Over the Password
          #5 Half in the Back, Half in the Front
    """)
    location = check_int(location, " ")
    for x in range(numbers):
      num = random.choice(num_chars)
    nums = list(num)
    #Apply Number Settings
    if location == 1:#Front
      password = password[:0] + nums[0] + password[0:]#Insert number in the word
      print("Here is your password: " + password)

run_app()








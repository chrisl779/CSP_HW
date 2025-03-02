import random

#GORILLA BEGINNER


def gorilla():
  x = input("Grunt Grunter! Grunt Gru Grunt Grunt? Yes/No: ")
  if (x.lower() == "yes"):
    print("Grunt")
    return
  else:
    print("Grunt")
    input("Grunt Grunt?")
    if int:
      print("Grunt grunt Grunt")
    elif float:
      print("Grunt... Grunt Grunt")
    else:
      print("Grunt tsk tsk tsk Grunt")
  user_input = input("Grunt Grunt int 1 grunt 10 Grunt: ")
  if (str(type(user_input)) != "int"):
    return
  int_value = int(user_input)
  if int_value > 6:
    print("Grunt Grunt")
    return

  else:
    print("Gruunt... Grunt")
    return


#BELOW AVERAGE JOE beginner


def belowAverageJoe():

  name = str(input("What's your name? "))
  print("Hello " + name + ", my name is also " + name + ".")
  print()

  age = int(input("How old are you, " + name + "? "))
  if (age > 20):
    print("Wow, you're really old! ")

  elif (age > 13 and age <= 19):
    print("Wow, you're still a teenager")

  elif (age <= 12):
    print("Wow, you're really young!")

  print()

  hair = str(input("What color is your hair " + name + "? "))
  if (hair.lower() == "black"):
    print("My hair is black too! ")

  elif (hair.lower() == "brown"):
    print("That's nice! ")

  elif (hair.lower() == "blonde" or hair.lower() == "blond"):
    print("Wow! ")

  else:
    print("That's so enthralling! ")
  print()

  sib = int(input("How many siblings do you have, " + name + "? "))
  if (sib == 0):
    print("Having no siblings is really sad. ")

  elif (sib == 1):
    print("Having a family of 4 is a great balance!")

  elif (sib > 2):
    print("You were definitely neglected as a child, " + name + ".")

  else:
    print("I'm not sure how you have negative siblings...")
  print()

  pets = str(input("Do you have any pets? "))
  if (pets is True or pets.lower() == "yes" or pets.lower() == "yeah"):
    pettype = str(input("What pet do you have? "))
    if (pettype.lower() == "dog"):

      print("I love dogs! ")
    elif (pettype.lower() == "cat"):

      print("I love cats! ")
    elif (pettype.lower() == "fish"):

      print("I love fish! ")

  elif (pets is not True or pets.lower() == "no" or pets.lower() == "nah"):
    petwant = str(input("What pet would you want (if you had to get one)? "))
    if (petwant.lower() == "dog"):

      print("I love dogs! ")
    elif (petwant.lower() == "cat"):

      print("I love cats! ")
    elif (petwant.lower() == "fish"):

      print("I love fish! ")
  print()

  drink = str(input("What's your favorite drink? "))
  if (drink.lower() == "water"):

    print("Good choice! ")
  elif (drink.lower() == "milk"):

    print("Solid choice! ")
  elif (drink.lower() == "soda" or drink.lower() == "pepsi"
        or drink.lower() == "coke"):

    print("Ok...")
  else:
    print("Interesting choice! ")
  print()

  day = input("Anyways, how's your day going, " + name + "? ")
  if (day.lower() == "good"):
    print("Glad to hear that!")

  elif (day.lower() == "bad"):
    print("Sorry to hear that, hope your day gets better.")

  elif (day.lower() == "fine"):
    print("That's good!")

  else:
    print("Cool!")
  print()

  print("My day is going pretty well. The Mets won!")
  base = str(input("Do you watch or play baseball? "))
  if (base is True or base.lower() == "yes" or base.lower() == "yeah"):
    print("Nice.")
    print()

    team = str(input("What's your favorite team?"))
    if (team.lower() == "yankees"):
      print("Congratulations, you're basic!")

    elif (team.lower() == "dodgers"):
      print("Congratulations, you're a bandwagon!")

    elif (team.lower() == "braves"):
      print("Congratulations, you might not have a personality!")

    else:
      print("That's nice! ")
    print()

  elif (base is not True or base.lower() == "no" or base.lower() == "nah"):
    print("Ok...")
    print()

    sports = input("What sports do you play then? ")
    if (sports.lower() == "basketball"):
      print(
          "It is statistically probable that you will never play in the NBA!")

    elif (sports.lower() == "football"):
      print(
          "It is statistically probable that you will never play in the NFL!")

    elif (sports.lower() == "none"):
      print("No sports, interesting...")

    else:
      print("Intresting choice of sports... ")
    print()

  hobby = str(input("What do you like to do in your free time? "))
  if (hobby.lower() == "read"):

    print("My favorite author is Twain!")
  elif (hobby.lower() == "draw"):

    print("My favorite artist is Picasso!")
  elif (hobby.lower() == "listen to music"):

    print("My favorite singer/songwriter is Taylor Swift!")
  else:
    print("That's fascinating! ")
  print()


#PIRATE intermediate
def pirate():
  print("Ahoy matey! How do you do? ")
  while (True):
    pirate_byecheck = input("")
    if (pirate_byecheck == "bye"):
      return
    resp = random.randint(1, 10)
    if (resp == 1):
      print("Blimey!")
    if (resp == 2):
      print("Shiver me timbers!")
    if (resp == 3):
      print("Aye aye!")
    if (resp == 4):
      print("Arrrrr")
    if (resp == 5):
      print("Aye, my heartie")
    if (resp == 6):
      print("Yo ho ho!")
    if (resp == 7):
      print("You little landlubber!")
    if (resp == 8):
      print("Avast, matey!")
    if (resp == 9):
      print("A smooth sea never made a skilled pirate, aye!")
    if (resp == 10):
      print("I'm the captain here!")


#COPYCAT INTERMEDIATE


def copycat():
  print("*** IF YOU EVER WANT TO END THE CONVERSATION, SAY 'BYE' ***")
  print()

  print("Hey there! What's your name? ")
  name = input("")
  if (name.lower() == "bye"):
    return
  print("My name is " + name + " too!")
  print()

  print(name + ", how old are you?")
  age = input("")
  if (age.lower() == "bye"):
    return
  print("I'm " + str(age) + " too!")
  print()

  print(name + ", how many siblings you have?")
  sib = input("")
  if (sib.lower() == "bye"):
    return
  print("I have " + str(sib) + " siblings too!")
  print()

  print(name + ", what color is your hair?")
  hair = input("")
  if (hair.lower() == "bye"):
    return
  print("I have " + str(hair) + " hair too!")
  print()

  print(name + ", how is your day going?")
  day = (input(""))
  if (day.lower() == "bye"):
    return
  print("I'm " + str(day) + " siblings too!")
  print()

  print(name + ", what's you favorite thing about life?")
  life = (input(""))
  if (life.lower() == "bye"):
    return
  print("I like " + str(life) + " too!")
  print()

  print(name + ", what's you favorite sport?")
  sport = (input(""))
  if (sport.lower() == "bye"):
    return
  print("I like " + str(life) + " too!")
  print()

  while (True):
    copycat_byecheck = input()
    if (copycat_byecheck.lower() != "bye"):
      return
    print(copycat_byecheck)


#AVERAGE JOE expert


def averageJoe():
  while True:
    x = str(input("What's up man, got a little room for some small talk? "))
    if (x.lower() == "no"):
      return
    else:
      y = input("what do want to talk about? Sports, Music, Food? ")
      if y.lower() == "sports":
        a = input("whats your favorite sport? ")
        print("No kidding, I like" + a + "too! ")
      elif y.lower() == "music":
        b = input("what genres do you listen to? ")
        if b.lower() == "80's rock":
          print("That's my jam right there! ")
        else:
          print(
              "My kids listen to that but I prefer the smooth sound of the 80's. "
          )
      elif y.lower() == ("food"):
        c = input("Do you prefer Asian food or Italian? ")
        if c.lower() == ("italian"):
          print("We have something in common! I love me some Italian. ")
        elif c.lower() == ("both"):
          print("That's what everyone says...")
        elif c.lower() == ("asian"):
          return
        else:
          print("No kidding!")
      else:
        return
      z = input("Do you want to talk about anything else? ")
      if z.lower() == ("no", "NO", "No"):
        return


#MENU


def menu():
  while (True):
    choice = ""
    print()
    print()
    print()
    print("Welcome to the menu!")
    print("Who do you want to talk to?")
    print("Below Average Joe, Gorilla, Copycat, Pirate, or Average Joe?")
    choice = input("")
    if (choice.lower() == "below average joe"):
      print()
      belowAverageJoe()
    if (choice.lower() == "gorilla"):
      print()
      gorilla()
    if (choice.lower() == "average joe"):
      print()
      averageJoe()
    if (choice.lower() == "copycat"):
      print()
      copycat()
    if (choice.lower() == "pirate"):
      print()
      pirate()


menu()

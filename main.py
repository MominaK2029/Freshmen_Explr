#Prologue
print("In this little town....")
print(" ")
print("Everything was perfect.")
print(" ")
print("Until, an invasive species from the unknown spread into our land.")
print(" ")
print("Those who preyed upon the species, were infected. They couldn't find the source. Yet those beings seemed to shift. Minor mutations over time, until they were unrecognizable. The chain eventually reached humans. The humans who consumed the infection walked unaware. Soon the disease became air-born.")
print(" ")
print("And that's when it happened. The lockdown. The Apocalypse.")
print(" ")
print("Humans began turning to their primitive ways. We were spread across the land. My parents were severely ill. They haven't found a cure for the disease. My sister and I have no idea what to do. We quarantined them in the basement. There have been some speculation on a cure but until then, we don't know what to do.")
print(" ")
print("I plan to go out tomorrow. I have to find more rations for the month.")
print(" ")
print("I head to bed. Tomorrow will hopefully be good...")
print(" ")
# Game Begins
print("*")
print("**")
print("***")
print(" ")
# Character name
name = input("Enter your name...")

print(name, "..")
print(name, "...")
print(name.upper())

#First pinpoint
choice1 = input("Wake up (A) or Sleep in (B)")

#SL 1, 3, 4
if choice1 == "A":
  print(name, "woke up to their sister.")
  print(" ")
  print("'C'mon you have to be early to avoid the zombies! Mom and Dad start their rounds and attempts at around 5pm and it's 1 right now. Get up.'")
  print(" ")
  print(name, "got up and made sure they had the proper gear on.", name, "looked at their pistol")
  #Second pinpoint
  choice2 = input("Leave the pistol and carry a knife instead (A) or Carry pistol and Knife (B)")
  #SL 1, 4
  if choice2 == "A":
    print(name, "went out in search of supplies and carried on through the woods gathering resources that managed to last.", name, "raided a grocery store last time but they seemed to find more resources in the other companies...")
    print(" ")
    print("'Sis, I'm home.'", name, "shouts out. Silence, weird.")
    print("They go to grab their gun but it has dissappeared")
    choice3 = input("What do you do? Explore the area (A) or get out of the house with your supplies (B) .")
    #SL 1
    if choice3 ==  "B":
      print(name, "ran out of the house with their supplies and decided to run away. The terror may have ended. But hardships are still in their heart. Ending…")
      print(1)
    #SL 1, 4
    elif choice3 == "A":
        print("You choose to explore the area.", name, "sister must be playing.")
        print("They find their sister, she's standing eerily. With your gun.")
        print("'Sister'", name, "calls out. She starts moving forward. You have to make a decision")
        choice4 = input("Do you fight your way out (A) or just give up and get infected (B) ?")
        #SL1 final choice
        if choice4 == "A":
          print("You ran away while you still had the chance. Your family is now gone. You're on your own. Ending…")
        print(1)
    #else: 
      #choice4 == "B":
      #print("You came this far. It was too difficult. Maybe it was time to..")
      #print("The world fades to black. Ending...")
      #print("4")
      #SL 3 + 4
  if choice2 == "B":
    print("You took both with you. Just in case.")
    print("The outside was dangerous. You never know what you might come across.")
    print(" ")
    print("You stumbled upon an unknown base, the facial recognition scans your face.")
    print(" ")
    print("The base was wonderful. You met so many survivors on your trip. And the cure.")
    print(" ")    
    print("But it only worked on newly infected or safe people. Not those who have been morphed.")    
    print(" ")    
    print("You made your way back home. Your sister stood in the kitchen. A bit purple...")
    print(" ")
    print("'Sis?'", name," called out. You sister turned around, she was turning. You looked at the cure")
    choice5 = input("Do you negotiate (A) or inject her with the cure (B)?")
    #SL3 Final decision
    if choice5 == "B":
      print(name, "moved quick. Before she could even react,", name, "inject the cure into her thigh. She crumbles to the floor, screaming.")
      print(" ")
      print("She moved back from them. 'Wha..did I-?' she was cut off by shrieking.")
      print(" ")
      print("Their parents banged on the door. The door that was about to break.", name, "grabbed her arm.")
      print(" ")
      print("They ran as far and as fast as they could, as", name, "recalled the place.")
      
      print(name, "lead their sister through the trees and back at those doors. Safe at last. Ending...")
      print("3")
    elif choice5 == "A":
      print(name, "tried to argue with her.")
      print(" ")
      print("Mellany, put the gun, down. I have the cure. Please.")
      print(" ")
      print("'Why didn't you save me faster", name, ". Why?! You let our parents rot.' She charged at me. I didn't want to hurt her.")
      print(" ")
      print("I tried my best to keep away. Until I saw the spots. She was infected... and I know Im the same.")
      print(" ")
      print("The next few seconds were a blur... until everything went dark. Ending...")
      print("4")
elif choice1 == "B":
  print("My days became longer as I became lonelier. My sibling,", name, "became more and more distant as time passed.")
  print(" ")
  print("I didn't know what to think of it. When I tried to wake her up they just slept. I didn't know what to do.")
  print(" ")
  print("Until I thought about it.")
  print(" ")
  print("This time was usually when the Zombies were innactive. They rampaged more through the night.")
  print(" ")
  print("Rather than the early hours of sunrise. Could they...")
  print(" ")
  print("I made my decision. With my knife.")
  print(" ")  
  print("Walking back into the room, I raised my right hand.")
  print(" ")
  choice6 = input("Are you going to wake up (A) or continue to sleep (B)?")
  if choice6 == "A":
    print("They woke up quite fast. Only to see the last face of their life time. Their sister.", name, "screams filled the house.")
    print("Mellany let go of the knife after lodging it at her sibling's throat. Her hands shook.")
    print("Mellany felt the guilt build up. She freaked out at the bang. Her hand sprung to the knife. Stabbing her own heart.")
  else:
    choice6 == "B"
    print(name, "continued to sleep. Mellany stood over them. She raised her hand. And...strike")
    print("")
                    


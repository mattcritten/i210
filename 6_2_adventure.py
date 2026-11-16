print("Welcome to the Adventure Game!")
print("You are standing at the entrance of a dark cave.")

direction = input("Do you want to go right or left? ")

#if user goes left
if direction == "left":
     #user encounters a dragon
     print("Walking a little further, a large canvern appears. \nHere, A large dragon crawls out of the shadows and roars at you.")
     #user asked if they want to fight or leave
     fight_or_flight = input("Do you want to fight or leave? ")
     #if user chooses to fight dragon
     if fight_or_flight == "fight":
           #user loses battle to dragon, game ends
            print("You engage the dragon in combat, but it quickly spins 360 degrees whipping his tail at you. You are hit, and sent across the cavern into a wall, killing you.\nGAME OVER ")
     #if user chooses to leave the cave
     if fight_or_flight == "leave":
            #user leaves unscathed, game ends
           print("You leave the cave before the dragon can attack, surviving the short conflict.\nGAME OVER")

#if user goes right
if direction == "right":
     #user finds a river
     print("Walking a little further, a soaring river appears, flowing perpendicular to the cave.")
     #user is asked if they want to swim or leave
     swim_or_leave = input("Do you want to swim or leave? ")
      #if user chooses to swim
     if swim_or_leave == "swim":
             #user finds treasure, game ends
            print("Swimming downstream, your foot latches on a chest. Quickly grabbing and inspecting the chest, you find a fortune of gold. Congratulations!\nGAME OVER")
      #if user chooses to leave cave
     if swim_or_leave == "leave":
             #user leaves unscathed, game ends
            print("You leave the cave.\nGAME OVER")

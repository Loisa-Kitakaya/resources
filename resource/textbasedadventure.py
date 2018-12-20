import sys
import random
import time

def time1():
    time.sleep(0.000001)

number = random.randint(5,20)


class user:

    
    def __init__ (self, player_name, player_health, health_potion, big_wrench, blue_keycard):

        self.__player_health = player_health
        self.__player_name = player_name
        self.__health_potion = health_potion
        self.__big_wrench = big_wrench
        self.__blue_keycard = blue_keycard

    def getName(self):
        return self.__player_name

    def getHealth(self):
        return self.__player_health

    def getPotion(self):
        return self.__health_potion

    def setHealth(self):
        self.__player_health = 100
        return self.__player_health

    def minusHealth(self, number):
        self.__player_health -= number
        return self.__player_health
        
    def minusPotion(self):
        self.__health_potion -= 1
        return self.__health_potion

    def plusPotion(self, number1):
        self.__health_potion += number1
        return self.__health_potion

    def plusHealth(self):
        self.__player_health += 35
        return self.__player_health
    
    def getWrench(self):
        self.__big_wrench
        return self.__big_wrench

    def pickupWrench(self, onebigwrench):
        self.__big_wrench += onebigwrench
        return self.__big_wrench
      
    def blueKeycard(self):
        self.__blue_keycard
        return self.__blue_keycard

    def plusKeycard(self, onekeycard):
        self.__blue_keycard += onekeycard
        return self.__blue_keycard

    def minusKeycard(self):
        self.__blue_keycard -= 1
        return self.__blue_keycard

def loot_big_wrench(player1):
    
    onebigwrench = 1
    
    player1.pickupWrench(onebigwrench)
    print("You now have a massive, deadly tool for killing", player1.getWrench(), "a giant plumbers wrench")
    print("\n")
    time.sleep(3)
    
def loot_key_card(player1):
    
    onekeycard = 1
    
    player1.plusKeycard(onekeycard)
    print("You now have", player1.blueKeycard(), "blue keycards")
    print("\n")
    time.sleep(3)

def loot(player1):
    
    import random
    number1 = random.randint(1,2)

    print("You find", number1, "first-aid kits")
    print("\n")
    player1.plusPotion(number1)
    print("You now have", player1.getPotion(), "first aid kits")
    print("\n")
    time.sleep(3)
        
        
def firstfight(player1):
    
    time.sleep(1)
                     
    
    soldier = user('Soldier', 80, 0, 0, 0)

    print("Your characters stats are: Health:\t", player1.getHealth())
    time.sleep(2)
                      
    fight(soldier, player1, name1)

    

def fight(soldier, player1, name1):
    import random
    import sys
    
    player1 = user(name1, player1.getHealth(), player1.getPotion(), player1.getWrench(), player1.blueKeycard())
    soldier = user('Soldier', soldier.getHealth(), soldier.getPotion(), soldier.getWrench(), soldier.blueKeycard())
        
    p = 0
    while p == 0:
        
        attack = input("1 = Attack with weapon, 2 = use potion")
        print("\n")
                         
        if attack == "1" and player1.getWrench() == 1:
            number = random.randint(5,20)             
            time.sleep(1)
            print("You strike at your enemy with the massive plumbers wrench. Soldier's health now is\t", soldier.minusHealth(number))
            print("\n")
            time.sleep(.05)
            number = random.randint(5,20)
            print("Soldier hits you back and your health is now at\t\t\t\t\t\t\t\t", player1.minusHealth(number))
            print("\n")
            time.sleep(.003)

            if soldier.getHealth() <= 0:

                print("You have won the fight!")
                loot(player1)
                p = 2
                
            elif player1.getHealth() <= 0:
                print("You died.")
                time.sleep(2)
                print("\n\n\n\n\n\n\n\n\n\n")
                print("Thanks for playing")
                time.sleep(5)
                print("\n\n\n\n\n\n\n\n\n\n")
                sys.exit(0)

        elif attack == "1" and player1.getWrench() == 0:
            number = random.randint(5,15)             
            time.sleep(1)
            print("You strike at your enemy with your fists. Soldier's health now is\t", soldier.minusHealth(number))
            print("\n")
            time.sleep(.05)
            number = random.randint(5,20)
            print("Soldier hits you back and your health is now at\t\t", player1.minusHealth(number))
            print("\n")
            time.sleep(.003)

            if soldier.getHealth() <= 0:

                print("You have won the fight!")
                loot(player1)
                p = 2
                
            elif player1.getHealth() <= 0:
                print("You died.")
                time.sleep(2)
                print("\n\n\n\n\n\n\n\n\n\n")
                print("Thanks for playing")
                time.sleep(5)
                print("\n\n\n\n\n\n\n\n\n\n")
                sys.exit(0)
                         
        elif attack == "2":
                         
            time.sleep(1)
            
            if player1.getPotion() == 0:
                print("You don't have any first-aid kits")
            else:
                print("You use a first aid-kit!")
                
                player1.plusHealth(), player1.minusPotion()

                print("Your characters stats are: Health:", player1.getHealth(), "Health Potion:", player1.getPotion())

                if player1.getHealth() > 100:
                         
                    player1.setHealth()
                    print("Soldier hits you back and your health is now at", player.minusHealth(number))
                         
        
        else:
            continue








def main():
    
    while True:
        
        import sys
        import time
    
    

        #Displaying game intro, asking user to make a choice.
        print ("*************************************************")
        print ("*******Welcome to the game Lightning Sword*******")
        print ("*************************************************")
        time.sleep(1)
        


        from time import sleep

        w = """You are in an underwater research facility that has been
attacked by unknown assailants. As the assistant to the head
researcher, you were hired in to assist Dr. Weathers with
the Lightning Sword project. Project Lightning Sword still
remains in large a mystery to you. Although you worked closely
with the doctor you were never allowed to see the big picture.
Right now that's the least of your worries, as chaos ensues around you.
Alarms were triggered a while ago. As you sit in your room,
you hear short bursts of automatic rifle fire and only one
thing is for certain, you have to survive.\n """
        for c in w:
            time1()
            sys.stdout.write(c)#This is to remove white space between each iteration/character
            sys.stdout.flush()
            #System call needs to be performed in order to do an output, system calls are expensive and time consuming
            #(because of the context switch, etc). Therefore user space libraries try to buffer it and you need
            #to flush it manually if needed.

        global name1
        name1 = input("What would you like your player to be named?")

        ########### player starting statistics
        player1 = user(name1, 100, 1, 0, 0)
        ########### player starting statistics

        print("\n")
        time.sleep(1)
        print ("Welcome,", name1, "please choose what you would like to do")
        print ("0 = Quit, 1 = Start New Game, 2 = Continue")
        time.sleep(1)
        choice = input()
        
        if choice == "1":
            
            starting_room(player1)
            time.sleep(1)
            continue
        
        elif choice == "2":
            
            print("this continues previus game")
            time.sleep(1)
            continue
        
        else:#here is a conditional y/n statement to quit program
            
            print("Are you sure you want to quit? Please enter y for yes and n for no")
            condition = input().lower()
            
            if(condition == 'y'):
                
                print("Thanks for playing")
                sys.exit(0)
                
            else:
                
                time.sleep(1)
                continue



          
def starting_room(player1):
    
    while True:
        
        import sys
        import time

        from time import sleep

        w = """You are standing in your room, door is locked and you're wondering
if you will get out of this alive. The gunfire keeps getting closer and you know that you
can't stay here, you have to make a move and try and get out. Otherwise it's just a matter
of time before they find you and that option doesn't look very promising.\n\n

You are ready to try your escape but first you should try and get any useful
things from your room to use along the way. Your room-office is a bit bigger than a walk in closet,
textile flooring and gray walls encompas your view and the only things in the room are the bed you
are sitting on (not very comfortable, looks more like a prisoners bed), a framed picture on the wall
and your work desk which has barely enough space for your equipment and computer."""

        for c in w:
            time1()
            sys.stdout.write(c)
            sys.stdout.flush()


        time.sleep(3)
        print("\n")
        
        time.sleep(3)
        print("\n")
        
        print ("Please choose what you would like to do")
        print("\n")
        print ("1 = Walk over to the picture frame, 2 = Walk over to the desk, 3 = Exit the door")
        time.sleep(1)
        print("\n")
        choice = input()
        
        if choice == "1":
            
            from time import sleep

            w = """The picture is of your younger years, when you had hair and your back didn't hurt so much
You wonder when it all fell appart and how you ended up here. There seems to be nothing else of interest
about the picture, you take 5 seconds to daydream of better times."""

            for c in w:
                time1()
                sys.stdout.write(c)
                sys.stdout.flush()

            time.sleep(5)
            print("\n")
            continue
        
        elif choice == "2":
            
            from time import sleep

            w = """You are standing in front of your desk, you see a large computer. Kind of antiquated
for being used in such a high tech environment, I guess that's what they give to assistants.
On the side is various lab equipment that in the current moment matters little. You do notice
a few things of interest however, your blue key-card and a large pipe wrench"""

            for c in w:
                time1()
                sys.stdout.write(c)
                sys.stdout.flush()

            print("\n")
            time.sleep(1)
            start_area_desk(player1)        
        elif choice == "3":
            print("""You make your way for the door and reach for the handle""")
            time.sleep(1)
            hallway1(player1)

        else:
            continue
main()
#Daniel Moon
#Psuedo blackjack cardgame
#Project #2

import random

#Player class
class Player():
    #Initialize class 
    def __init__(self, thename):
        self.__cardhand = []    
        self.__balance = 10     
        self.__name = thename
        return
    
    #Appends card values to hand
    def addcard(self, newVal):
        self.__cardhand.append(newVal)
        return

    #Resets hand when the game has been played 13 times and clears hand for each round
    def clearhand(self):
        self.__cardhand = []
        return
    
    #Returns cards in the hand of player
    def gethand(self, player):
        return self.__cardhand 
    
    #Return name of the player
    def getname(self):
        return self.__name

    #Changes balance of player
    def balancechange(self, value):
        self.__balance += value
        return 
    
    #Returns balance of player
    def getbalance(self):
        return self.__balance
    
    #Returns overload printing to print out the hand of the player
    def __str__(self):
        i = 0

        #Parallel lists hold suite and cards to put in hand
        suite = ["Hearts", "Clubs", "Diamonds", "Spades"] 
        card = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9","10", "Jack", "Queen", "King"]
        hand = ""

        #For loop through the card hand of player to get the matching values for suite and card index
        for each in self.__cardhand:
            
            if each == 52:
                suitestring = suite[3]
            else:
                suitestring = suite[each//13]   #Integer divide the card number to find the suite

            cardstring = card[each%13]      #Modulus of the card number to find the card value
            i += 1
            if i == 1:
                hand = cardstring + " of " + suitestring
            else:
                hand += " and " + cardstring + " of " + suitestring
        return self.__name + "'s hand: " + hand #Return name's hand: with the hand

#Resets all card values in carddeck to false
def resetdeck(deck):
    for i in range(52): 
        deck.append(False)

#Generates a new card between 1 and 52
def newcard():
    c = random.randint(0,51)
    return c

#Draws a random card and appends it to the drawn cards found inside the player classes   
def draw(player, numcards, deck):
    for i in range(numcards):
        new = newcard()
        while deck[new]: #If the card drawn is already true, then draw a new card
            new = newcard()
        player.addcard(new)  
        deck[new] = True #Sets the card value in carddeck to be true for drawn
    return

#Compares the drawn cards of player1 and player2 to deduce a winner
def cmpcards(Player1, Player2):
    cardsum1 = 0        #Sum from player 1
    cardsum2 = 0        #Sum from player 2
    output = ""     

    #Calccounterlates the value of each card
    for i in Player1.gethand("Player1"):
        cardsum1 += i%13
    for i in Player2.gethand("Player2"):
        cardsum2 += i%13 

    #Compares sums to find winner
    if cardsum1 > cardsum2:
        output = True   #True: player 1 is the winner
    elif cardsum1 < cardsum2:
        output = False  #False: player 2 is the winner
    else:
        output = ""     #No output for a tie
    return output

#Main blackjack function takes in 2 players and deck to change
def blackjack(Player1, Player2, deck):

    #Loops until playagain is false and has a counter that allows the player list
    #to alternate from Player 1 to Player 2 being the first to be prompted
    playagain = True
    counter = 0 
    playerlist = [Player1, Player2] 
    resetdeck(deck)
    #Game Loops until one player runs out of money
    while playagain == True:

        #First round of drawing cards with output of balance and hand
        draw(Player1, 1, deck) 
        draw(Player2, 1, deck) 
        print("\n", 10*"-", "Game ", counter+1, 10*"-", "\n", playerlist[counter%2], sep="")
        print(playerlist[(counter+1)%2])
        print("\n" + playerlist[counter%2].getname() + "'s balance: $", playerlist[counter%2].getbalance(), "\n" + playerlist[(counter+1)%2].getname()+ "'s balance: $", playerlist[(counter+1)%2].getbalance(), sep="")
        bet = eval(input(playerlist[counter%2].getname()+ ", how much do you wish to bet?\n"))
        
        #Validation loop to check if the value entered is valid
        validation = False
        while validation == False:
            if bet > 10 or bet <0:
                bet = eval(input("Cannot bet more or less than you have. \nHow much do you wish to bet?\n"))
            else:
                validation = True

        #Handles player input for folding for second player
        playerfold = input(playerlist[(counter+1)%2].getname() + ", would you like to fold or bet?\n")
        if playerfold == "fold":
            playerlist[(counter+1)%2].balancechange(-1)
            playerlist[counter%2].balancechange(1)
            print(playerlist[counter%2].getname(), "Wins!")

            #Second round of drawing cards with output of hand
        else: 
            draw(Player1, 1, deck)
            draw(Player2, 1, deck)
            print("\n", playerlist[counter%2], sep="")
            print(playerlist[(counter+1)%2], "\n", sep="")

            #Compares cards to see who wins and subtracts or adds betted amounts
            if cmpcards(Player1, Player2):
                print(playerlist[counter%2].getname(), "Wins!\n")
                playerlist[counter%2].balancechange(bet)
                playerlist[(counter+1)%2].balancechange(-bet)
            elif not cmpcards(Player1, Player2):
                print(playerlist[(counter+1)%2].getname(), "Wins!\n")
                playerlist[counter%2].balancechange(-bet)
                playerlist[(counter+1)%2].balancechange(bet)  
            else:
                print("It was a tie!\n")

        #TWo cards are cleared from hands
        Player1.clearhand()
        Player2.clearhand()

        #If the game has been played 13 times, the deck is reset
        if counter % 13 == 0:
            deck = []
            resetdeck(deck)
        counter += 1 

        #Determines which player wins the game when a player no longer has money left
        if Player1.getbalance() <= 0:
            print(Player2.getname() + " Wins the Game!")
            playagain = False
        if Player2.getbalance() <= 0:
            print(Player1.getname() + "Wins the Game!")
            playagain = False


#Main Function
def main():
    carddeck = []
    #Takes in Player input
    name1 = input("Player 1 input your name: ")
    name2 = input("Player 2 input your name: ")

    #Create player classes
    Player1 = Player(name1)
    Player2 = Player(name2)    

    #Place two objects in the blackjack function
    blackjack(Player1, Player2, carddeck) 

main()
     
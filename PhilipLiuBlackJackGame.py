# Hi, my name is Philip Liu and welcome to my blackjack game!
# The rules of this game are simple. You start with 2 cards and the objective of the game is to get close to or exactly on 21. 
# However, if you go over 21 then you bust and lose the game. If you decide that you are close enough then you stay. By staying
# the dealer may now try to get a higher amount than you stayed at. If the dealer does then the dealer wins and the game will ask
# you if you would like to keep on playing

#imports
import random
import os

#Global array which represents the deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
bet = 0
money = 100
#intro to the game
print("Welcome to BlackJack!")
bet = input ("How much money would you like to spend. You total is $" + str(money) + " ")

#A function that randomizes the order of the deck
def newDeck(deck):
    hand = []
    #loops through the deck and pushes cards to the front of the deck
    for i in range (2):
        #shuffle the deck
        random.shuffle(deck)
        #take a card from the deck
        card = deck.pop()
        #setting the 11,12,13,14 cards to face cards
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

#A function that asks the user if they would like to play again
def playAgain():
    #use global variables for money and bet
    global money
    global bet
    reload = input ("Would you like to play again? (Y/N): ").lower()
    if reload == "y":
        #input the amount of money you want to bet
        bet = input ("How much money would you like to spend. You total is $" + str(money) + " ")
        game()
    else:
        print("Thanks for playing!")
        exit()

# a function that calculates the total 
def total(hand):
    total = 0
    for card in hand:
        #if the card is a face card then the total adds 10
        if card == "J" or card == "Q" or card == "K":
            total += 10
        #if the card is an Ace then the total will add 11 if lower than 11 else it will add 1
        elif card == "A":
            if total >= 11: total += 1
            else: total += 11
        else:
            #add the number of the card
            total += card
    return total

#A function that adds a card to your hand when you ask the dealer to hit
def hit(hand):
    #adding the first card from the top of the deck to the array
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

#A function that clears everything in the terminal
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

#A function that prints the results of the dealers hands and the players hands
def printResults(dealerHand, playerHand):
	clear()
	print ("The dealer has a " + str(dealerHand) + " for a total of " + str(total(dealerHand)))
	print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))

#A function that sees if the player or dealer had hit 21 within the first 2 cards
def blackjack(dealerHand, playerHand):
    #use global variables for money and bet
    global bet
    global money
    #If the player hits 21
    if total(playerHand) == 21:
        printResults(dealerHand, playerHand)
        print ("Congratulations! You got a Blackjack!\n")
        #gain double if you get 21
        money = money + (bet * 2)
        playAgain()
    #if the dealer hits 21
    elif total(dealerHand) == 21:
        printResults(dealerHand, playerHand)		
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        #lose double if the dealer has 21
        money = money - (bet * 2)
        playAgain()

#The main function where the game is played
def game():
    #use global variables for money and bet
    global bet
    global money
    choice = 0
    clear()
    #setting the dealers and players hands
    dealerHand = newDeck(deck)
    playerHand = newDeck(deck)
    #Stating what you and the dealer has
    print ("The dealer is showing a " + str(dealerHand[0]))
    print ("You have a " + str(playerHand) + " for a total of " + str(total(playerHand)))
    #if either player has 21 then blackjack occurs
    blackjack(dealerHand, playerHand)
    quit = False
    #use a while loop that is continuous while the player is still playing
    while not quit:
        #prompt the user to hit, stay or quit the game
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        #if the user selects to hit
        if choice == 'h':
            #add to the players hand
            hit(playerHand)
            print(playerHand)
            #if the player busts
            if total(playerHand)>21:
                print('You busted')
                money -= int(bet)
                playAgain()
        #if the user selects to stay
        elif choice=='s':
            #A while loop that loops while the dealer isn't bust
            while total(dealerHand) <= 21:
                #If the player's total is larger than the dealers total
                if total(playerHand) > total(dealerHand):
                    #Add to the dealers total
                    hit(dealerHand)
                    print(dealerHand)
                    #if the dealer busts then the player wins
                    if total (dealerHand) > 21:
                        print("Dealer busts. You win!")
                        money += int(bet)
                        playAgain()
                #if the dealers total is larger than the players total
                elif total(dealerHand) > total(playerHand):
                    #the dealer wins and the player loses
                    print(dealerHand)
                    print("Dealer has a higher score. You lose")
                    money -= int(bet)
                    playAgain()
                #if the dealers hand is equal to the players hand
                elif total (dealerHand) == total(playerHand):
                    #The dealer has tied with the player and the game is over
                    print(dealerHand)
                    print("You tied!")
                    money = money
                    playAgain()
        #if the user selects to quit the game
        elif choice == "q":
            #the program prints out bye and then exits the program and the loop
            print("Bye!")
            quit=True
            exit()

#Executes the code
if __name__ == "__main__":
    game()


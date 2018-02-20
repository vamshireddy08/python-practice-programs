import random

myList=[2,3,4,5,6,7,8,9,10,'J','K','Q','A']*4

card_count={'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10}

min_bet=10
max_bet=100

def remove_card(myList,card):
    myList.remove(card)

def dealer_turn(p,d):
    if d.hand>21:
        p.balance+=3*p.bet-p.insurance 
        print "you won! \n your balance is ",p.balance
        quit( )             
    elif d.hand<17:
        d.my_cards(random.choice(myList))
        dealer_turn(p,d)
    else:
        if d.hand>p.hand:
            d.balance+=p.bet 
            p.balance+=2*p.insurance  
            print "you lost\n  your balance is ",p.balance
            quit() 
        elif d.hand<p.hand:
            p.balance+=3*p.bet - p.insurance   
            print " you WON! \n your balance is  ",p.balance
            quit() 
        else:    
            print "game is tied\n your balance is ",p.balance 
            p.balance+=p.bet 
            quit( )


def player_turn(p,d):
         
    print "your cards ",p.cards
    print "your hand count ",p.hand
    print "your bet amount \n",p.bet 
    print "your remaining balance ",p.balance

    if p.hand>21:
        d.balance+=p.bet 
        print "you r busted!\n your balance is ",p.balance
        quit()
    if p.hand==21 and d.hand==21 and len(p.cards)==2:
        p.balance+=p.bet 
        print "match is tied\n your balance is ",p.balance
        quit()
    elif p.hand==21 and len(p.cards)==2 and d.hand!=21:
        p.balance+=2.5*p.bet 
        print "BlackJack \n your balance ",p.balance 
        quit()  
     
    elif (d.hand==21 and p.hand!=21):
        d.balance+=p.bet 
        print "dealer cards\n",d.cards
        print "you are busted!\n"
        quit()
    else:
        print "dealer card \n",d.cards[0]
    #use try block    

    turn=raw_input("press h to hit, d to double, st=stand, i=insurance \n")
    if turn=='h':
        p.my_cards(random.choice(myList))
        player_turn(p,d)
    if turn=='st':
        dealer_turn(p,d)
    if turn=='i':
        while True:
            print "your current balance is ",p.balance
            try: 
                player_insurance=input("enter your insurance amount\n ") 
            except: 
                print "enter a integer number \n"
                continue 
            else:
                break  
        
        if (p.balance-player_insurance)>=0:
            p.insurance=player_insurance 
            p.balance-=player_insurance  
            player_turn(p,d)
        else:
            print "insufficent funds for insurance \n"
            player_turn(p,d) 
    if turn=='d':
        if (p.balance>=2*p.bet):
            p.my_cards(random.choice(myList))
            p.bet*=2
            p.balance-=p.player_bet         
            if p.hand>21:
                d.balance+=p.bet 
                print "you r busted!\n your balance is ",p.balance
                quit() 
            else:
                dealer_turn(p,d)  
        else:
            print "you did't have sufficent funds to double the bet\n"
            player_turn(p,d)  

class Player(object):
    def __init__(self,balance=0):
        self.balance=balance
        self.hand=0
        self.bet=0
        self.insurance=0
        self.cards=[]
    def add_amount(self,amount):
        self.balance+=amount    
    def my_cards(self,card):
        self.cards.append(card)
        remove_card(myList,card) 
        if card==2:
            self.hand+=2   
        if card==3:
            self.hand+=3
        if card==4:
            self.hand+=4
        if card==5:
            self.hand+=5
        if card==6:
            self.hand+=6
        if card==7:
            self.hand+=7
        if card==8:
            self.hand+=8
        if card==9:
            self.hand+=9
        if card==10:
            self.hand+=10
        if card=='J':
            self.hand+=10
        if card=='K':
            self.hand+=10
        if card=='Q':
            self.hand+=10
        if card=='A':
            self.hand+=11
            if self.hand>21:
                self.hand-=10

def start_game():
    x=raw_input("Press 's'  to start the game\n")
    if x=='s':
        p=Player()
        d=Player()
        print "your current balance is ",p.balance
        bal=input("add amount to your account\n")

        p.add_amount(bal)
        p.my_cards(random.choice(myList))
        d.my_cards(random.choice(myList))

        p.my_cards(random.choice(myList))
        d.my_cards(random.choice(myList))
        game(p,d)    
    else:
        quit()
        
def game(p,d):
    while True:
        print "your current balance is ",p.balance
        try:
            player_bet=input("enter your bet amount\n  minimum bet amount is $10\n ") 
        except: 
            print "enter a integer number \n"
            continue 
        else:
            break  
        
    if (p.balance-player_bet)>=0:
        p.bet=player_bet
        p.balance-=player_bet 
        player_turn(p,d)
    else:
        print "insuffecient funds "
        game(p,d)                #use try and catch block

def main():
    start_game()

if __name__=="__main__":
    main() 

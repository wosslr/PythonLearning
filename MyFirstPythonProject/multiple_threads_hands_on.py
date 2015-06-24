# encoding: utf-8
'''
@author: Wosslr
'''
from threading import Thread
from threading import Lock
from time import sleep
from random import randint

cashPool = 0
MAX_CASH = 100
gameFlag = [0] * 4
winningNum = 0

minGameNum = 1
maxGameNum = 3

WAGER = 10

lock = Lock()

class Banker(Thread):
    def __init__(self):
        super(Banker, self).__init__()
    def run(self):
        print "Banker enter game...\n"
        while cashPool < MAX_CASH:
            lock.acquire()
            global winningNum
            winningNum = randint(minGameNum, maxGameNum)
            gameFlag[0] = gameFlag[1] = gameFlag[2] = gameFlag[3] = 0
            print "Banker has given %d as the winning number\n" % winningNum,
            print "Now the cash pool has %d USD\n" % cashPool,
            print "Now the game flag is %s \n" % gameFlag,
            lock.release()
            sleep(4)
        
        print "Game over\n"
        print "Banker has leave the game \n"

class Gamer(Thread):
    ID = 0
    def __init__(self, ID):
        super(Gamer, self).__init__()
        self.ID = ID
    def run(self):
        print "Gamer%d enter game...\n" % self.ID
        x = 0
        global cashPool
        while cashPool < MAX_CASH:
            lock.acquire()
            if gameFlag[self.ID] == 0:
                x = randint(minGameNum, maxGameNum)
                gameFlag[self.ID] = 1
                print "Gamer%d has wager %d as game number\n" % (self.ID, x),
                print "Now the game flag is %s \n" % gameFlag,
                if x == winningNum:
                    cashPool -= 10
                    print "As winning number is %d \n" % winningNum,
                    print "Gamer%d has won 10 USD from cash pool\n" % self.ID,
                else:
                    cashPool += 10
                    print "As winning number is %d \n" % winningNum,
                    print "Gamer%d has lost 10 USD to cash pool\n" % self.ID,
                
                print "Now the cash pool has %d USD\n" % cashPool,
            
            lock.release()
            sleep(2)
            
        print "Gamer%d has leave the game \n" % self.ID

print "Game start...\n"
banker = Banker()
gamer1 = Gamer(0)
gamer2 = Gamer(1)
gamer3 = Gamer(2)
gamer4 = Gamer(3)

banker.start()
gamer1.start()
gamer2.start()
gamer3.start()
gamer4.start()

banker.join()
gamer1.join()
gamer2.join()
gamer3.join()
gamer4.join()

print "Finally the cash pool has %d USD\n" % cashPool,
        
        
        
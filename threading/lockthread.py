from threading import *
import threading

l=Lock()
class flightbooking:
    def __init__(self,ticket_left):
        self.ticket_left = ticket_left
    l.acquire()
    def buy(self,ticket_buy):
        if self.ticket_left >= ticket_buy:
            print("Your ticket is confirmed\n")
            self.ticket_left -= ticket_buy
        else:
            print("Ticket are not left\n")
    l.release()

ticket = flightbooking(10)


t1 = threading.Thread(target=ticket.buy,args=[3])
t2 = threading.Thread(target=ticket.buy,args=[5])
t3 = threading.Thread(target=ticket.buy,args=[6])


t1.start()
t2.start()
t3.start()


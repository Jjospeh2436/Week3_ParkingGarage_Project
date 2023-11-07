class Garage():
    def __init__(self):
        self.parking_spaces = 0
        self.ticket_count = None
        self.ticket_price = None
        self.currentTicket = {"paid": False}

    def total_spaces(self):
        spaces = input("How many parking spaces does your garage has? ")
        self.parking_spaces = int(spaces)
        self.ticket_count = int(spaces)
    
    def set_price(self):
        price = input("Set the ticket price for each parking space: ")
        self.ticket_price = int(price)

    def takeTicket(self):
        self.parking_spaces -= 1
        self.ticket_count -= 1

    def payForParking(self):
        pay_ticket = input(f"Please pay the ticket price associated for your awaited time {self.ticket_price}: ")
        if int(pay_ticket) == self.ticket_price:
            print("Ticket has been paid you have 15 minutes to leave.")
            self.currentTicket["paid"] = True
        else:
            print("Ticket has not been paid, you are not allowed to leave.")

    def leaveGarage(self):
        if self.currentTicket["paid"] == True:
            print("Thank you, have a nice day!")
            self.parking_spaces += 1
            self.ticket_count += 1

        else:
            pay_ticket = input(f"Please pay the ticket price associated for your awaited time {self.ticket_price}: ")
            if int(pay_ticket) == self.ticket_price:
                print("Ticket has been paid you have 15 minutes to leave.")
                self.currentTicket["paid"] = True
                print("Thank you, have a nice day!")
                self.parking_spaces += 1
                self.ticket_count += 1
            else:
                print("Ticket has not been paid, you are not allowed to leave.")

new_garage = Garage()

def run():
    print("Welcome to your new garage! Feel free to name it what you want, but for the mean time we have customers waiting to park so lets get started.")
    while True:
        new_garage.total_spaces()
        if new_garage.parking_spaces <= 0:
            print("These amount won't do, we need a higher number as they are a lot of customers waiting to park")
        else:
            new_garage.set_price()
            if new_garage.ticket_price <= 0:
                print("These amount won't do, we need a higher number as they are a lot of customers waiting to park")
            else:
                print("Perfect! Now let's let these customers in!")
                start = input("Let's open the gate, type in 'open' in your prompt and I will do you the favor of opening the gate: ")
                if start.strip().lower() == "open":
                    print("Welcome to our parking garage! Please take a ticket and enjoy your stay!")
                    new_garage.takeTicket()
                    print("When you are done with your stay, type in 'leave' to leave the garage")
                    exit = input("Waiting on your input... ")
                    if exit.strip().lower() == "leave":
                        new_garage.payForParking()
                        new_garage.leaveGarage()
                        break
                    else:
                        print("I'm sorry you stayed too long, you have to leave now.")
                        new_garage.payForParking()
                        new_garage.leaveGarage()
                        break
                else:
                    print("You have no other choice, I'm opening the gate")
                    start = "open"

run()
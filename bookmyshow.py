class bookmyshow:
    def __init__(self, acc_name, tickets_booked):
        self.acc_name = acc_name
        self.tickets_booked = tickets_booked

    def book_tickets(self, no_of_tickets):
        self.tickets_booked = no_of_tickets + self.tickets_booked


user = bookmyshow("shyam", 10)
user.book_tickets(10)
print(user.tickets_booked)

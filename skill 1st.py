class Person(object):
    # Constructor
    def init(self, Name, From , Destination, Date, Howmany):
        self.Name = Name
        self.From = From
        self.Destination = Destination
        self.Date=Date
        self.Howmany=Howmany
    def display(self):
        print(self.Name);
        print(self.From);
        print(self.Destination);
        print(self.Date)
        print(self.Howmany)
class Employee(Person):
    def __init__(self, Name, From, Destination, Date, Howmany):
        # invoking the init of the parent class
        Person.init(self, Name, From, Destination, Date, Howmany)
a = Employee('hoshita','Vijayawada', 'vaddeswaram', 'july3', 3)
a.display()
print('booking confirmed')
print(" Thankyou For Booking ")
print(" Happy Journey ")
"""
    In this file we have all SOLID principles in a given example .
    SOLID stands for: 1.single Responsibility Principle (SRP)
                      2.Open/Closed Principle (OCP)
                      3.Liskov Substitution Principle(LSP)
                      4.Interface Segregation Principle (ISP)
                      5.D
    Make sure to read the code thoroughly and ask copilot any question that comes to your mind!
    peace :)
"""



# 1.The single Responsibility Principle (SRP) states that a class should have only one reason to change.
# In this example, we will create a simple task manager that adheres to the SRP.
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)


class TaskPresentation:
    @staticmethod
    def display(tasks):
        for task in tasks:
            print(task)


class TaskInput:
    @staticmethod
    def add_task():
        return input("Enter the task you want to add: ")

    @staticmethod
    def remove_task():
        return input("Enter the task you want to remove: ")


#2.The Open/Closed Principle (OCP) states that software entities should be open for extension but closed for modification.
# In this example, we will create a simple task manager that adheres to the OCP.

from  abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
       
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    

class AreaCalculator:
    def area(self, shape):
        return shape.area()

##########################
#3.The Liskov Substitution Principle(LSP) states that objects of a super class should be able to be replaced with objects of a sub class
# without affecting the correctness of the program.
#Here is the example of LSP:

class Bird:
    def fly (self):
        pass


class FlyingBird(Bird):
    def fly(self):
        print("Flying Bird")


class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

class Penguin(NonFlyingBird):
    pass

#########################
#4.The Interface Segregation Principle (ISP) states that clients should not be forced to depend on the interfaces they do not use.
#Here is the example:

class IPrinter:
    def print(self):
        pass

class IScanner:
    def scan(self):
        pass

class ICopy:
    def copy(self):
        pass

class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan (self):
        print("Scanning...")

class Copier(ICopy):
    def copy(self):
        print("Copying...")

class Fax(IFax):
    def fax(self):
        print("Faxing...")


#########################################
#5.Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules;
#both should depend on abstraction
# Here is an example of DIP
from abc import ABC, abstractmethod


class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass


class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f'Sending {message} to {receiver}...')


class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f'Sending {message} to {receiver}...')

class NotificationService:
    def __init__(self, message_service : IMessageService):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)



#########################################################
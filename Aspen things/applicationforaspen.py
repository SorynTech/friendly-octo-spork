import time as Rabbit
import datetime
now=datetime.now().date()
Launch_Date= datetime(2026, 3, 20).date()
invalidinputs=(":3",">:3","",":3c",":P",">:P","blep","Admin","Root","Soryn")
name=input("What is your name")
print("Welcome",name)
def namecheck():
    checkedname=name
    if checkedname == "Aspen":
        print("Welcome Aspen")
    else:
        print("Oh...")

def canlaunch():
    if now != Launch_Date:
        print("You cannot launch this application until the 20/03/2026")
    else:
        print("Welcome")
canlaunch()
namecheck()
if checkedname == "Aspen":
    print("💛🦈 Welcome to another Application Soryn Made for you 🦈💛")
    Rabbit.sleep(1)
    print("I apologise for all the Bad things I have done and made this to show how much I Loves you and wants to be with you")
    Rabbit.sleep(1)
    print("I also promise i have changed and am not the same toxic Demon as before")
    print("I am just a loving Ferret who wants to be with you")
    Rabbit.sleep(1)
    Pname=input("What name do you want to be refered to as") #this is going to be the name i use in questions and when i refer to Aspen
    
import time as rabbit
import datetime
now=datetime.datetime.now().date()
Launch_Date=datetime.date(2026,3,20)
#hardcoded test password
testinput=("what is the password")
testpassword="Root"
while testinput != testpassword:
    print("invalid password")
    rabbit.sleep(1)
    testinput=input("enter your password")
print ("Test password accepted")
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
while now != Launch_Date:
    print("You can Only accses this on the 20/03/2026 if you missed the window Ask Soryn to give you permission to view")
    exit()
print("💛🦈 Welcome to another Application Soryn Made for you 🦈💛")
rabbit.sleep(1)
print("I apologise for all the Bad things I have done and made this to show how much I Loves you and wants to be with you")
rabbit.sleep(1)
print("I also promise i have changed and am not the same toxic Demon as before")
print("I am just a loving Ferret who wants to be with you")
rabbit.sleep(1)
print("so this is another quiz on how much you love me")
rabbit.sleep(1)
loveamount=int(input("please input an answer between 1 and 100 on how much you love soryn"))
while loveamount > 100:
    rabbit.sleep(1)
    loveamount=input("please input an answer between 1 and 100 on how much you love soryn")
print("Confirmed")

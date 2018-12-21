#import wpf
day = ["Sunday", "Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday"]
sundayact = {}
Mondayact = {}
tuesdayact = {}
wendsdayact = {}
thursdayact = {}
fridayact = {}
saturdayact= {}



def menu ():
    print ("Welcome to the daily scheduler")
    x = input("1. add an activity and time" "2. delete an activity""3. change the time""4. Exit")
    if x == "1":
        option1()
    if x == "2":
        option2()
    if x == "4":
        return 0;

def cont (): 
    yn= input("Do you want to continue?")
    print ("You said" + yn)
    if yn == "No":
        return 0
    else:
        return menu()
# to do
# print what day of the wee would you like to do if for number list then print out day selected
# print out list every time a new entry has been added
#scheduler make 2 seperate lists
#the other has activity
#make a menu
#see if python has a switch system
#option if they want to make a list for a specifc day
#print list after every additon
#if something is at the same time in a day pop up error
def option1 ():
    day= input("Which day would you like to add an activity to?")
    print(day())
    if day == "1":
        times()
        activity()
        sundayact[times()] = activity()
        print("What activity?")

def timecheck (key):
    if sundayact[key] == sundayact[key]:
        print ("error you already have something at that time.")
        print("please delete your current activity at that time before adding a new one.")
def printweek():
    print("here is how your week looks so far")
    print(sundayact, Mondayact, tuesdayact, wendsdayact,
          thursdayact, fridayact, saturdayact)
def times():
    y = input("AM or PM?")
    if y == "AM":
        print ("What time?")
        t = input("12:00", "1:00","2:00","3:00", "4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00")
        result = "{} {} ".format(t,y)
        return result
    elif y == "PM":
        t= input("12:00", "1:00","2:00","3:00", "4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00")
        result = "{} {} ".format(t,y)
        return result
def activity():
    x = input("What activity?")
    return x

#def option2():

def delete():
    print("From what day do you want to delete?")
    print("1.Sunday","2. Monday","3.Tuesday","4.Wenesday","5.Thursday","6.Friday","7.Saturday")
    y= input()
    if y == 1:
        print(sundayact)
        x=input("Which activity?")
        if x == sundayact[x]:
            del sundayact[x]
            print(sundayact)
menu()
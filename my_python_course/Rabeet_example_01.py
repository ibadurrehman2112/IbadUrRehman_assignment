import datetime
from itertools import count
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter '1' For Food:\nEnter '2' For Exercise\n"))
        if (c==1):
            value = input("Type Here\n")
            with open("Rabeet-food.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")
        elif(c==2):
            value =input("Type Here\n")
            with open("Rabeet-exercise.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")    
    if k==2:
        c=int(input("Enter '1' For Food:\nEnter '2' For Exercise\n"))
        if (c==1):
            value = input("Type Here\n")
            with open("Ibad-food.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")
        elif(c==2):
            value =input("Type Here\n")
            with open("Ibad-exercise.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")    
    if k==3:
        c=int(input("Enter '1' For Food:\nEnter '2' For Exercise\n"))
        if (c==1):
            value = input("Type Here\n")
            with open("Talmeez-food.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")
        elif(c==2):
            value =input("Type Here\n")
            with open("Talmeez-exercise.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")    
            
def retrive(k):
    if k == 1:
        c=input("Enter '1' For Food\nEnter '2' For Excersice\n")
        if c ==1:
            with open("Rabeet-food.txt") as file:
                for i in file:
                    print(i , end="")
        elif c==2:
            with open("Rabeet-exercise") as file:
                for i in file:
                    print (i ,end="")
    if k == 2:
        c=input("Enter '1' For Food\nEnter '2' For Excersice\n")
        if c ==1:
            with open("Ibad-food.txt") as file:
                for i in file:
                    print(i , end="")
        elif c==2:
            with open("Ibad-exercise") as file:
                for i in file:
                    print (i ,end="")
    if k == 3:
        c=input("Enter '1' For Food\nEnter '2' For Excersice\n")
        if c ==1:
            with open("Talmeez-food.txt") as file:
                for i in file:
                    print(i , end="")
        elif c==2:
            with open("Talmeez-exercise") as file:
                for i in file:
                    print (i ,end="")
        else:
            print("Unvalid Client/Name")
            while True:
                input("Press 0 To 'Start Again'")
                if input ==0:
                    continue
                else:
                    exit("Thanks")

print("Health Management System by Rabeet!!!")
a= int(input("Press 1 for Log\nPress 2 for Retrive\n"))
if a==1:
    b=int(input("Press 1 For Rabeet\nPress 2 For Ibad\nPress 3 Talmeez\n"))
    take(b)
else:
    b=int(input("Press 1 For Rabeet\nPress 2 For Ibad\nPress 3 Talmeez\n"))
    retrive(b)
import datetime
from itertools import count
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter '1' For Food:\nEnter '2' For Exercise\n"))
        if (c==1):
            value = input("Type Here\n")
            with open("Rabeet-food.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")
        elif(c==2):
            value =input("Type Here\n")
            with open("Rabeet-exercise.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")    
    if k==2:
        c=int(input("Enter '1' For Food:\nEnter '2' For Exercise\n"))
        if (c==1):
            value = input("Type Here\n")
            with open("Ibad-food.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")
        elif(c==2):
            value =input("Type Here\n")
            with open("Ibad-exercise.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Sucsessfully Saved In Data")    
    if k==3:
        c=int(input("Enter '1' For Food:\nEnter '2' For Exercise\n"))
        if (c==1):
            value = input("Type Here\n")
            with open("Talmeez-food.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Sucsesfully Saved In Data")
        elif(c==2):
            value =input("Type Here\n")
            with open("Talmeez-exercise.txt" ,"a") as file:
                file.write(str([str(gettime())])+':' +value+'\n')
            print("Successfully Saved In Data")    
            
def retrive(k):
    if k == 1:
        c=input("Enter '1' For Food\nEnter '2' For Excersice\n")
        if c ==1:
            with open("Rabeet-food.txt") as file:
                for i in file:
                    print(i , end="")
        elif c==2:
            with open("Rabeet-exercise") as file:
                for i in file:
                    print (i ,end="")
    if k == 2:
        c=input("Enter '1' For Food\nEnter '2' For Excersice\n")
        if c ==1:
            with open("Ibad-food.txt") as file:
                for i in file:
                    print(i , end="")
        elif c==2:
            with open("Ibad-exercise") as file:
                for i in file:
                    print (i ,end="")
    if k == 3:
        c=input("Enter '1' For Food\nEnter '2' For Excersice\n")
        if c ==1:
            with open("Talmeez-food.txt") as file:
                for i in file:
                    print(i , end="")
        elif c==2:
            with open("Talmeez-exercise") as file:
                for i in file:
                    print (i ,end="")
        else:
            print("Unvalid Client/Name")
            while True:
                input("Press 0 To 'Start Again'")
                if input ==0:
                    continue
                else:
                    exit("Thanks")

print("Health Management System by Rabeet!!!")
a= int(input("Press 1 for Log\nPress 2 for Retrive\n"))
if a==1:
    b=int(input("Press 1 For Rabeet\nPress 2 For Ibad\nPress 3 Talmeez\n"))
    take(b)
else:
    b=int(input("Press 1 For Rabeet\nPress 2 For Ibad\nPress 3 Talmeez\n"))
    retrive(b)
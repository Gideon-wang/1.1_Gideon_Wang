'''
   name=Gideon Wang
   version:4
   date:29/08/2025
   description:assessment
'''
#----------------libraries---------------
#----------------functions---------------
#----------------------------------------
#this function is used to compare the size 
#of two numbers.
#----------------------------------------
def max(num1,num2):
    if num1>num2:
        return(num1)
    else:
        return(num2)
#----------------------------------------
#this function allows users to input their 
#exercise status,calculate the average value
#and make a personalized evalution.
#----------------------------------------
def average(result):
    total=0
    for i in range(result):
        days=i+1
        #keep looping until the user enters the valid running_result      
        while True:
            try:
                running_result=int(input(f"what is your running times in minutes for day{days}:"))#record the times in number
                if running_result>=10 and running_result<=60:#the number range is 10-600 and avoid people using hours as a unit of measure
                    break
                else:
                    print("the number you entered is unrealistic(note that the unit is minutes)")
            except:
                print("you must enter a number")
        list_result.append(running_result)#add the results into the list
        total+=list_result[i]#calculate the total running time
        average=total/len(list_result)#calculate the average running time
    print(f"your results are{list_result} and your average grade is {average}")#print out the reults in list and the average time
    #this loop is to personalize evaluation of user average time    
    if average<=20:
        print("you need to work harder")
    elif average<=40:
        print("please keep up the momentum")
    else:
        print("well done")
#----------------main routine------------
#keep looping until the user enters the valid name
while True:
    name=input("enter your first name:")
    if name.isalpha():#record the name in string
        if len(name)>=2 and len(name)<=10:#check the length of the name
            break
        else:
            print("you must enter a valid name")
    else:
        print("you must enter a string")
#this loop is used to make sure the user is in Year11
while True:
    try:
        age=int(input("enter you age:"))#record the age in number
        if age>=15 and age<=17:
            break
        else:
            print("you must enter your real age")
    except:
        print("you must enter a number")
list_result=[]#create a empty list to fill in information
average(5)#record five days of data using equations
a=max(list_result[0],list_result[1])#use the function to compare sizes one by one
b=max(list_result[2],list_result[3])
c=max(a,b)#using letters instead of results makes the program clearer
d=max(c,list_result[4])
print(f"your best running time is {d}")#print out the best running time

'''
   name=Gideon Wang
   version:3
   date:28/08/2025
   description:assessment
'''
#----------------libraries---------------
#----------------functions---------------
def max(num1,num2):
    if num1>num2:
        return(num1)
    else:
        return(num2)
def average(result):
    total=0
    for i in range(result):
        days=i+1
        while True:
            try:
                running_result=int(input(f"what is your running times in minutes for day{days}:"))
                if running_result>=0 and running_result<=600:
                    break
                else:
                    print("the number you entered is unrealistic")
            except:
                print("you must enter a number")
        list_result.append(running_result)
        total+=list_result[i]
        average=total/len(list_result)
    print(f"your results are{list_result} and your average grade is {average}")
    if average<=30:
        print("you need to work harder")
    elif average<=60:
        print("please keep up the momentum")
    else:
        print("well done")
#----------------main routine------------
while True:
    name=input("enter your name:")
    if name.isalpha():
        break
    else:
        print("you must enter a string")
age=int(input("enter you age:"))
list_result=[]
average(5)
a=max(list_result[0],list_result[1])
b=max(list_result[2],list_result[3])
c=max(a,b)
d=max(c,list_result[4])
print(f"your best running time is {d}")

'''
   name=Gideon Wang
   version:2
   date:26/08/2025
   description:assessment
'''
#----------------libraries---------------
#----------------functions---------------
def average(result):
    total=0
    for i in range(result):
        days=["day1","day2","day3","day4","day5"]
        running_result=int(input(f"what is your running times in minutes for {days[i]} :"))
        list_result.append(running_result)
        total+=list_result[i]
        average=total/len(list_result)
    print(f"your average grade is {average}")
#----------------main routine------------
name=input("enter your name:")
age=int(input("enter you age:"))
list_result=[]
average(5)


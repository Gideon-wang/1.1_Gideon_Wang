'''
   name=Gideon Wang
   version:1
   date:25/08/2025
   description:assessment
'''
#----------------libraries---------------
#----------------functions---------------
def times(result):
    for i in range(result):
        days=["day1","day2","day3","day4","day5"]
        running_result=input("what is your running times in minutes for",days(i),":")
        i+=1
        list_result=[]
        list_result.append(running_result)
#----------------main routine------------
name=input("enter your name:")
age=int(input("enter you age:"))
result=5
times(result)

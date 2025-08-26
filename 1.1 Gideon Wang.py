'''
   name=Gideon Wang
   version:2
   date:26/08/2025
   description:assessment
'''
#----------------libraries---------------
#----------------functions---------------
def times(result):
    for i in range(result):
        days=["day1","day2","day3","day4","day5"]
        running_result=int(input(f"what is your running times in minutes for {days[i]} :"))
        list_result.append(running_result)
#----------------main routine------------
name=input("enter your name:")
age=int(input("enter you age:"))
list_result=[]
times(5)
total=list_result[0]+list_result[1]+list_result[2]+list_result[3]+list_result[4]
print(total)

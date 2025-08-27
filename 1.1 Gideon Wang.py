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
        running_result=int(input(f"what is your running times in minutes for day{days}:"))
        list_result.append(running_result)
        total+=list_result[i]
        average=total/len(list_result)
    print(f"your results are{list_result} and your average grade is {average}")
#----------------main routine------------
name=input("enter your name:")
age=int(input("enter you age:"))
list_result=[]
average(5)
a=max(list_result[0],list_result[1])
b=max(list_result[2],list_result[3])
c=max(a,b)
d=max(c,list_result[4])
print(f"your best running time is {d}")
import random
import time
def getrandomdate(sd,ed):
    print("print random date between",sd,"and",ed )
    randomgen=random.random()
    dateformat='%m/%d/%Y'
    st=time.mktime(time.strptime(sd,dateformat))
    et=time.mktime(time.strptime(ed,dateformat))

    randomtime=st+randomgen*(et-st)
    randomdate=time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("randomdate=",getrandomdate("1/1/2016","12/2/2018"))
x

import math

num = int(input('Enter number: '))
def factor(n):
    return(math.factorial(n))

print('factorial of ', num,'is', factor(num))


# DATE TIME CALENDER
from datetime import date

my_date = date.today()
a =('today is ' ,my_date.day,'-',my_date.month,'-',my_date.year)
print(a)


from datetime import datetime

today = datetime.now()
print('current date time is',today)


from win32com.client import Dispatch


speak = Dispatch("SAPI.Spvoice")
speak.Speak(a)



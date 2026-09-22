import csv
import random as rd
from datetime import datetime,timedelta

#configuration
NO_OF_DAYS=30

rd.seed()

#generate dates
start_date=datetime.now()
#print(timedelta.__doc__)
print(start_date)
print(timedelta(30,2,5,8,6,9))

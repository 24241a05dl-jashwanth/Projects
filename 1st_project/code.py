import csv
#app name
APP ="Instagram"

mins=[] 

with open("digital_behaviour.csv","r",encoding="utf-8",newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        mins.append(int(row["Instagram_Minutes"]))

mins = mins[23:]

total=sum(mins)
div=total/len(mins)
max_value=max(mins)
min_value=min(mins)

count=0
for i in mins:
    if i>div:
        count += 1

print(f"App Name:{APP}",f"Total Minutes:{total}",f"Average Minutes:{div}",f"Max Minutes:{max_value}",f"Min Minutes:{min_value}",f"Count above Average:{count}")


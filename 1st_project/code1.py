import csv
import numpy as np
insta_list=[]
study_list=[]
with open("digital_behaviour.csv","r",encoding="utf-8",newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_list.append(int(row["Study_Minutes"]))

insta_list=insta_list[-7:]
study_list=study_list[-7:]

insta_array=np.array(insta_list)
study_array=np.array(study_list)

total=insta_array.sum()
avg=insta_array.mean()
max_value=insta_array.max()
min_value=insta_array.min()

print(f"Total Instagram Minutes:{total}")
print(f"Average Instagram Minutes:{avg}")
print(f"Maximum Instagram Minutes:{max_value}")
print(f"Minimum Instagram Minutes:{min_value}")

#help(insta_array)
print(f"first day :{insta_array[0]}")
print(f"last day :{insta_array[-1]}")
print(f"third day:{insta_array[2]}")

print(f"First three days:{insta_array[0:3]}")
print(f"last two days:{insta_array[-2::]}")
print(f"days two,three,four:{insta_array[1:4:]}")

#insta_array=[val/60 for val in insta_array]
print(f"Every insta value from min to hours :{insta_array/60}")

print(f"every single day,subtract Instagram minutes from Study minutes:{insta_array-study_array}")

print(f"Each value greater than 100?:{insta_array>100}")

print(f"value where value greater than 100:{insta_array[insta_array>100]}")

print(f"count where value greater than 100:{(insta_array>100).sum()}")
print(f"count where value greater than Average:{(insta_array>avg).sum()}")
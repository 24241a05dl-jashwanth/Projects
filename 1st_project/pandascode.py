import pandas as pd
df=pd.read_csv("digital_behaviour.csv")
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df["Instagram_Minutes"].sum())
# print(df["Instagram_Minutes"].mean())
# print(df["Instagram_Minutes"].max())
# print(df["Instagram_Minutes"].min())
# print(df["Study_Minutes"].sum())
# print(df["Study_Minutes"].mean())
# print(df["Study_Minutes"].max())
# print(df["Study_Minutes"].min())

#Show me only the Instagram minutes column.
# print(df["Instagram_Minutes"])
# print(df[["Date","Instagram_Minutes"]])

# print(df["Instagram_Minutes"].sum())

# print(df["Instagram_Minutes"].mean())

# print(df["YouTube_Minutes"].max())

# print(df[df["Instagram_Minutes"]>100])

# print(df[df["Study_Minutes"]>180])

# print(df[df["Instagram_Minutes"]>df["Study_Minutes"]])

# print(df.sort_values("Instagram_Minutes", ascending=False))

# print(df.sort_values("Instagram_Minutes", ascending=False).head(5))

# print(df.sort_values("Study_Minutes", ascending=False).head(5) )

#print(df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"])

#print(Total_Screen_time)print(df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"])
df["Total_Screen_time"]=(df["Instagram_Minutes"]+df["YouTube_Minutes"]+df["WhatsApp_Minutes"]+df["LinkedIn_Minutes"])
df["Screen_Hours"]=df["Total_Screen_time"]/60
#print(df["Screen_Hours"])
df["Digital_balance"]=df["Study_Minutes"]/df["Total_Screen_time"]


df["Day_Type"]="Normal"
df.loc[df["Total_Screen_time"]>300,"Day_Type"]="Heavy"
#print(df["Day_Type"])

app_total={
    "insta": df["Instagram_Minutes"].sum(),
    "youtube": df["YouTube_Minutes"].sum(),
    "linkedin": df["LinkedIn_Minutes"].sum(),
    "whatsapp": df["WhatsApp_Minutes"].sum()
}
# print(app_total)

# print(max(app_total, key=app_total.get))
# print(df[df["Day_Type"]=="Heavy"]["Day_Type"].count())
# print(df["Digital_balance"].mean())
# print(df["Digital_balance"].idxmax())
# print(df.iloc[26]["Date"])
# print(df["Total_Screen_time"].idxmax())
# print(df.iloc[21]["Study_Minutes"])


df.to_csv("My_Analysis.csv")











    

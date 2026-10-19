import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("My_Analysis.csv")

plt.figure(figsize=(12, 5))

plt.bar(df["Date"], df["Total_Screen_time"], color="steelblue")

plt.title("My Screen Time by Day")
plt.xlabel("Day")
plt.ylabel("Minutes")

plt.tight_layout()
plt.savefig("screen__time.png")
plt.show()
plt.close()
plt.bar(["Instagram","Youtube","Whatsapp","LinkedIn"],[df["Instagram_Minutes"].sum(),df["YouTube_Minutes"].sum(),df["WhatsApp_Minutes"].sum(),df["LinkedIn_Minutes"].sum()],color=["steelblue","steelblue","steelblue","steelblue"])

plt.title("Total Time by App")
#plt.tight_layout()
plt.savefig("compare_apps.png")
plt.show()
plt.close()

plt.plot(df["Date"],df["Study_Minutes"],marker='o',label="Study_mins")
plt.plot(df["Date"],df["Total_Screen_time"],marker='o',label="tot_Screen_time")
plt.legend()
plt.savefig("trend")
plt.show()




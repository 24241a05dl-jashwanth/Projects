import pandas as pd
import numpy as np

df=pd.read_csv("day02_usage.csv")

chat=df["Chat"].to_numpy()
video=df["Video"].to_numpy()
study=df["Study"].to_numpy()
games=df["Games"].to_numpy()
print(len(chat))

print(np.sum(chat))
print(np.sum(video))
print(np.sum(study))
print(np.sum(games))

print(round(np.mean(chat),1))
print(round(np.mean(video),1))
print(round(np.mean(study),1))
print(round(np.mean(games),1))

bal=study-games
bestday=np.argmax(bal)
worstday=np.argmin(bal)
print("Best day for study:",bestday+1)
print("Worst day for study:",worstday+)



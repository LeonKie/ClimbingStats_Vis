import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

myFmt = mdates.DateFormatter('%d.%m.%Y')



# visulaization of the climbing data


df = pd.read_csv('Klettern_Stats.csv',sep=',',dtype=str)
df.columns = ["Date","Time","Grade","Type","Loc"]

df=df[df["Loc"]=="DAV Freimann"]

#SORT_ORDER = {"7-": 0, "7": 1, "7+": 2, "8-":3, "8":4}
SORT_ORDER = ['6','6+','7-','7','7+','8-','8','8+']


grades=list(set(df["Grade"].tolist()))
grades.sort(key=lambda val: SORT_ORDER.index(val))

flashs = []
tops = []
trys = []

for grade in grades:
    flashs.append(df[(df["Grade"] == grade) & (df["Type"] == "Flash")].shape[0])
    tops.append(df[(df["Grade"] == grade) & (df["Type"] == "Top")].shape[0])
    trys.append(df[(df["Grade"] == grade) & (df["Type"] == "Try")].shape[0])
    
# Create stacked bar chart with flashs, tops and trys

fig = plt.figure()
ax = fig.add_subplot(111)

ax.xaxis.set_major_formatter(myFmt)

df_flash = df[df["Type"] == "Flash"]
x_flash=mdates.date2num([datetime.strptime(d, '%d.%m.%Y') for d in df_flash["Date"].tolist()])
y_flash=[SORT_ORDER.index(g) for g in df_flash["Grade"].tolist()]


df_top = df[df["Type"] == "Top"]
x_top=mdates.date2num([datetime.strptime(d, '%d.%m.%Y') for d in df_top["Date"].tolist()])
y_top=[SORT_ORDER.index(g) for g in df_top["Grade"].tolist()]

df_try = df[df["Type"] == "Try"]
x_try=mdates.date2num([datetime.strptime(d, '%d.%m.%Y') for d in df_try["Date"].tolist()])
y_try=[SORT_ORDER.index(g) for g in df_try["Grade"].tolist()]



#print(x_try,df_try["Grade"])

ax.scatter(x_flash,y_flash,color="gray", label="Flash")
ax.scatter(x_top,y_top,color="y",label="Top")
ax.scatter(x_try,y_try,color="r",label="Try")
plt.yticks(range(len(SORT_ORDER)), SORT_ORDER)
plt.grid()
plt.legend()
plt.title("DAV Freimann")
plt.show()


import pandas as pd 
import matplotlib.pyplot as plt

# visulaization of the climbing data


df = pd.read_csv('Klettern_Stats.csv',sep=',',dtype=str)
df.columns = ["Date","Time","Grade","Type","Loc"]


#SORT_ORDER = {"7-": 0, "7": 1, "7+": 2, "8-":3, "8":4}
SORT_ORDER = ['6+','7-','7','7+','8-','8','8+']
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

print(trys,tops,flashs)

ax1 = ax.bar(grades,trys,color='red')
ax2 = ax.bar(grades,tops,bottom=trys, color='orange')
ax3 = ax.bar(grades,flashs,bottom=[tr+to for tr,to in zip(trys,tops)] , color='green')

fig.legend((ax1[0],ax2[0],ax3[0]),('Try','Top','Flash'))

plt.show()

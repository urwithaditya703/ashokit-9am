import matplotlib.pyplot as plt
import pandas as pd
# # x=[1,2,3]
# # y=[10,20,30]
# # plt.plot(x, y, color="red", linestyle="--")
# # plt.xlabel("XAxis Value")
# # plt.ylabel("YAxis Value")
# # plt.title("Line Plot")
# # plt.show()
# # # x=["std11","std2"]
# subject=["Phy","chem","math","bio"]
# marks=[60,70,80,90]
# colors=["gold","orange","red","blue"]
# explode=[0,0.1,0,0.2]
# plt.pie(marks,
#         labels=subject,
#         colors=colors,
#         autopct='%1.4f%%',
#         explode=explode,
#         shadow="true",
#         textprops={'fontsize':10},
#         startangle=90,
#         wedgeprops={'edgecolor':'red'}        )
# plt.title("Marks Pie Chart")
# plt.xlabel("subject")
# plt.ylabel("Marks")
# plt.show()
# marks=[10,20,30,40,50,60,70,80,90,55,73,89,27,30,58,69,79,66,88]
# plt.figure(figsize=(10,6))
# plt.hist(marks, bins=5, color='skyblue', edgecolor='black')  
# plt.title("Marks Pie Chart")
# plt.xlabel("subject")
# plt.ylabel("marks")
# plt.show()

# #Scatter
# students=["std1","std2","std3","std4"]
# Marks=[50,30,70]
# plt.scatter(students, Marks, s=200, color="Red", marker='o')
# plt.grid(True)
# plt.show()
months=['jan','feb','mar','apr','may','jun']
sales=[100,200,300,400,300,500]
plt.fill_between(months,sales)
plt.show

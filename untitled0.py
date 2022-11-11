# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:19:04 2022

@author: DELL
"""

#imporitng libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading data from file
file = pd.read_excel(r'C:\Users\DELL\Desktop\ADS1 Junaid\stock ex (1).xlsx')
#checking all the columns of the data
file.columns
#sperating the exel data and saving it inside variables
total_com = file['Total No. of Listed Companies']
total_com
total_cap = file['Total Listed Capital - Rs']
total_cap
total_mar = file['Total Market Capitalisation - Rs']
total_mar
#now let's plot the graph
plt.figure(figsize= (12,3))
plt.plot(file.loc[:,"Years"],total_mar, color="blue", label="total market capitalization")
plt.plot(file.loc[:,"Years"],total_cap,color = "red" , label="total listed capitals")
plt.plot(file.loc[:,"Years"],total_com,color="green", label="total companies")
plt.grid(linewidth=1)
plt.legend()
plt.xlabel("Years")
plt.ylabel("Analysis")
plt.title("Stock Managment")
#importing all libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading data from an exel sheet
file = pd.read_csv(r'C:\Users\DELL\Desktop\ADS1 Junaid\Q2 (1).csv')
#rearranging data and ploting a graph
file.pivot(index='state',columns='cause of death',values='deaths').plot(kind='bar',stacked =True,figsize = (15,8),width = 0.7)
                   #labelling and giving title to the graph
plt.xlabel('Us states')
plt.ylabel('Recorded deaths')
plt.title('Deaths recorded jan 2020')
#importing all libraries
import pandas as pd
import matplotlib.pyplot as plt
#reading data from an exel sheet
file = pd.read_csv(r'C:\Users\DELL\Desktop\ADS1 Junaid\MOD-Organogram of Staff Roles & Salaries-Royal Air Force Museum (1).csv')
file.head(2)
#creating a new file to saperate the job title column and to count all categories
new_file = file['Generic Job Title'].value_counts().rename_axis('job titles').reset_index(name='counts')
#to print all the data
print(new_file)
#get total of count values
total_count = new_file.counts.sum()
total_count
#to add value with the percentage
def your_autopct_format(prct_value):
# print(prct_value)
    return '{:.4f}%\n{:.0f}'.format(prct_value, total_count*prct_value/100)
#setting our label and values
job_titles = new_file['job titles']
job_titles
counts = new_file['counts']
counts
y_explode = [0,0.1,0,0,0]
#creating our pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(counts,labels=job_titles,autopct=your_autopct_format,explode=y_explode)
plt.title('total members of royal airforce meseum')
plt.legend(loc='center left',prop={'size': 5})

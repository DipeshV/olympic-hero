# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'}, inplace=True)
print(data.head())


# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])

better_event = data['Better_Event'].value_counts().index.values[0]

#print(data.head(5))
print(better_event)

assert data['Better_Event'].value_counts()['Summer'] == 143, "Should be 143"


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter', 'Total_Medals']]

print(top_countries.head(5))

top_countries=top_countries[:-1]

def top_ten(data,column):
    country_list = []
    country_list=list((data.nlargest(10,column)['Country_Name']))
    return country_list


top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10 :\n",top_10, "\n")

common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here

#Create dataframe anmd plot for Summer Event
summer_df = data[data['Country_Name'].isin(top_10_summer)]

#print(summer_df)

plt.figure(figsize=(20,6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

plt.title('Top 10 Summer')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')

#Create the dataframe and plot for Winter Event

winter_df = data[data['Country_Name'].isin(top_10_winter)]

#print(winter_df)

plt.figure(figsize=(20,6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

plt.title('Top 10 Winter')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')

#Create the dataframe and plot for Winter Event

top_df = data[data['Country_Name'].isin(top_10)]

#print(top_df)

plt.figure(figsize=(20,6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])

plt.title('Top 10')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')


# --------------
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])

print(summer_df['Golden_Ratio'].idxmax())

summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print("Top Summer Coutnry: ", summer_country_gold, " with a ratio of %.2f" % summer_max_ratio)

# For Winter List

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio = max(winter_df['Golden_Ratio'])

winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']

print("Top Winter Country: ", winter_country_gold, " with a ratio of %.2f" % winter_max_ratio)

# For Over List

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])

top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(), 'Country_Name']

print("Top Country: ", top_country_gold, " with a ratio of %.2f" % top_max_ratio)


# --------------
#Code starts here

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total'] * 1

print(data_1.head(10))

most_points = max(data_1['Total_Points'])

best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print("The maximum points achieved is: ", most_points, " by ", best_country)


# --------------
#Code starts here

#Subsetting the dataframe
best=data[data['Country_Name']==best_country]
best.reset_index(drop = True, inplace = True)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]


#Plotting bar plot
best.plot.bar(stacked=True)

#Changing the x-axis label
plt.xlabel('United States')

#Changing the y-axis label
plt.ylabel('Medals Tally')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Updating the graph legend
l=plt.legend()
l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))



#Code ends here



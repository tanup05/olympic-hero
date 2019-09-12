# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
#Load the DataFrame
data = pd.read_csv(path)

#Rename the column name from 'Total' to 'Total_Medals'
data.rename(columns = {'Total' : 'Total_Medals'}, inplace=True)

#Display the first 10 records:
data.head(10)


# --------------
#Code starts here

# Create a new column Better_Event that stores 'Summer','Winter' or 'Both' based on the comparision between the total medals won in Summer event and Winter event using np.where function
data['Better_Event'] =  np.where(data['Total_Summer']==data['Total_Winter'],'Both', np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter'))

#Better Event

print("Value counts of each event:\n", data['Better_Event'].value_counts())

better_event = data['Better_Event'].value_counts().idxmax()
print("\nBetter event is:\n", better_event)


# --------------
#Code starts here

#Create a new dataframe subset called 'top_countries' with the columns ['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'] only

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Drop the last row from 'top_countries'(The last row contains the sum of the medals)

top_countries.drop(top_countries.index[-1], inplace=True)

#Function top_ten

def top_ten(df, column_name):
    country_list = []
    top_10_df = df.nlargest(10, column_name)
    country_list = country_list + list(top_10_df['Country_Name'])
    return (country_list)

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

print(top_10_summer, "\n", top_10_winter, "\n", top_10)
print('***'*20)

#function to find commanalities between the lists

def common_countries(top_10_summer, top_10_winter, top_10):
    set_summer = set(top_10_summer)
    set_winter = set(top_10_winter)
    set_total = set(top_10)
    
    common_sum_win = set_summer.intersection(set_winter)
    common = common_sum_win.intersection(set_total)
    return list(common)

common = common_countries(top_10_summer, top_10_winter, top_10)
print(common)


# --------------
#Code starts here

#Subset the dataframe 'data' based on the country names present in the list top_10_summer using "isin()" function on the column Country_Name. Store the new subsetted dataframes in 'summer_df'. Do the similar operation using top_10_winter and top_10 and store the subset dataframes in 'winter_df' & 'top_df' respectively.

summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

#Take each subsetted dataframe and plot a bar graph between the country name and total medal count according to the event (For e.g. for 'summer_df' plot a bar graph between Country_Name and Total_Summer)

fig, (ax) = plt.subplots(3, 1, figsize=(5, 20))

#####
plt.subplot(3, 1, 1)
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'], color='Orange')
plt.xlabel('Country Names')
plt.ylabel('Medal count for summer event')
plt.xticks(rotation=45)
#####
plt.subplot(3, 1, 2)
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'], color='Cyan')
plt.xlabel('Country Names')
plt.ylabel('Medal count for winter event')
plt.xticks(rotation=45)
#####
plt.subplot(3, 1, 3)
plt.bar(top_df['Country_Name'], top_df['Total_Medals'], color='Plum')
plt.xlabel('Country Names')
plt.ylabel('Total medal count')
plt.xticks(rotation=45)

plt.show()


# --------------
#Code starts here

#In the dataframe 'summer_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Summer and Total_Summer.

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

#Find the max value of Golden_Ratio and the country associated with it and store them in summer_max_ratio and summer_country_gold respectively

summer_max_ratio = summer_df['Golden_Ratio'].max()

summer_country_gold = summer_df['Country_Name'].loc[summer_df['Golden_Ratio'].idxmax()]
print(summer_country_gold)
print(summer_max_ratio)

#In the dataframe 'winter_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Winter and Total_Winter.

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']

#Find the max value of Golden_Ratio and the country associated with it and store them in 'winter_max_ratio' and 'winter_country_gold' respectively.

winter_max_ratio = winter_df['Golden_Ratio'].max()

winter_country_gold = winter_df['Country_Name'].loc[winter_df['Golden_Ratio'].idxmax()]
print(winter_country_gold)
print(winter_max_ratio)

#In the dataframe top_df'(created in the previous function) , create a new column Golden_Ratio which is the quotient after dividing the two columns Gold_Total and Total_Medals.

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

#Find the max value of Golden_Ratio and the country associated with it and store them in top_max_ratio' and 'top_country_gold' respectively.

top_max_ratio = top_df['Golden_Ratio'].max()

top_country_gold = top_df['Country_Name'].loc[top_df['Golden_Ratio'].idxmax()]
print(top_country_gold)
print(top_max_ratio)


# --------------
#Code starts here


#Drop the last row from the dataframe(The last row contains the total of all the values calculated vertically) and save the result in 'data_1'

data_1 = data.drop(data.index[146])

#Update the dataframe 'data_1' to include a new column called Total_Points which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point.(i.e. You need to take weighted value of Gold_Total, Silver_Total and Bronze_Total)

def total_points(arg_1, arg_2, arg_3):
    gold_tot = data_1[arg_1]*3
    silver_tot = data_1[arg_2]*2
    bronze_tot = data_1[arg_3]
    return gold_tot+silver_tot+bronze_tot

data_1['Total_Points'] = total_points('Gold_Total', 'Silver_Total', 'Bronze_Total')

#Find the max value of Total_Points in 'data_1' and the country assosciated with it and store it in variables 'most_points' and 'best_country' respectively.

most_points = data_1['Total_Points'].max()
best_country = data_1['Country_Name'][data_1['Total_Points'].idxmax()]

print("The best country is", best_country, "with", most_points)


# --------------
#Code starts here

#Create a single row dataframe called 'best' from 'data' where value of column Country_Name is equal to 'best_country'(The variable you created in the previous task)

best = data[data['Country_Name']==best_country]

#Subset 'best' even further by only including the columns : ['Gold_Total','Silver_Total','Bronze_Total']
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

#Create a stacked bar plot of 'best' using "DataFrame.plot.bar()" function

#Name the x-axis as United States using "plt.xlabel()"

#Name the y-axis as Medals Tally using "plt.ylabel()"

#Rotate the labels of x-axis by 45o using "plt.xticks()"

best.plot.bar(stacked=True, figsize=(8,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()



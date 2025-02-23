
# Import the pandas library
import pandas as pd

# Create a sample dictionary containing data for a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame to display the data
print("Original DataFrame:\n", df)


# Accessing specific columns
# Selecting the 'Name' and 'Age' columns
name_age_df = df[['Name', 'Age']]
print("\nName and Age columns:\n", name_age_df)


# Filtering rows based on a condition
# Selecting rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nRows where Age > 25:\n", filtered_df)


# Adding a new column
# Adding a 'Country' column based on the 'City' column
df['Country'] = ['USA', 'UK', 'France', 'Japan']
print("\nDataFrame with added Country column:\n", df)


# Grouping data and calculating aggregates
# Grouping by 'City' and calculating the average age for each city
grouped_df = df.groupby('City')['Age'].mean()
print("\nAverage age by city:\n", grouped_df)


# Handling missing data
# Introducing a missing value in the 'Age' column
df.loc[1, 'Age'] = None #NaN - Not a Number

#Filling missing values with the mean age
mean_age = df['Age'].mean()
df['Age'].fillna(mean_age, inplace=True)
print("\nDataFrame after handling missing values:\n",df)

#Sorting the DataFrame by Age
df_sorted = df.sort_values(by='Age')
print("\nDataFrame sorted by Age:\n", df_sorted)


#Saving the DataFrame to a CSV file
df.to_csv('output.csv', index=False) #index=False prevents saving row index
print("\nDataFrame saved to output.csv")


#Reading data from a CSV file
df_from_csv = pd.read_csv('output.csv')
print("\nDataFrame read from output.csv:\n", df_from_csv)


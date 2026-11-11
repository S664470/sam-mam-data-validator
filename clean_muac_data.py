import pandas as pd

#Read The CSV file 

df = pd.read_csv('humanitarian_nutrition_camps.csv')
print(df, '\n')

#Print muac with error status
errors = df[(df['muac_cm'] < 11.5) & (df['status'] != 'SAM')]
print("Error: the program detect the following wrong muac status readings....")
print(errors[['child_id', 'camp_name', 'muac_cm', 'status']], '\n')


#Correcting the informatin with loc[]
df.loc[(df['muac_cm'] < 11.5) & (df['status'] != 'SAM'), 'status' ] = 'SAM'
print("Here's the correct readings of muac status...")
print(df)

#Export the cleaned data into excel file
df.to_excel('humanitarian_nutrition_clened_data.xlsx', index=False)

#Confirming the generation of excel file
print('Excel file with cleaned data was generated.')

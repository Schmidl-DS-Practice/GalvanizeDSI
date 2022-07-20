import pandas as pd

#1 look at dataset
df = pd.read_csv("data/hospital-costs.csv")
#1 total charges
df['Total Charge'] = df['Discharges'] + df['Mean Charge']
#2 total cost
df['Total Cost'] = df['Discharges'] + df['Mean Cost']
#3 markup rate
df['Markup Rate'] = df['Total Charge'] / df['Total Cost']
#4 facility with highest/lowest markup rates
markup = df.sort_values(by='Markup Rate', ascending=False)
markup = markup[['Facility Name','Markup Rate']]
markup.head(1)
markup.tail(1)

#out of curiosity
peeps_to_hos= df[['APR DRG Description', 'Discharges']].groupby('APR DRG Description').sum().sort_values(by='Discharges', ascending=False).head(5)

#follow the money
#1 create a new DataFrame named "net".
net = df[['Facility Name', 'Total Charge', 'Total Cost']]
#2 Find the total amount each hospital spent, and how much they charged. 
#(Group your data by Facility names, and sum all the total costs and total charges)


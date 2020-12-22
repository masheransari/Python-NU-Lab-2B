import pandas as pd
import numpy as np

df = pd.read_csv("BL-Flickr-Images-Book.csv")
print(df)

# For printing top 5 entries
df.head()

# For Printing the lowest 5 entries
df.tail()

# Now we want to drop table from our data set so we use drop functions.
to_drop_labels = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver',
                  'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(labels=to_drop_labels, inplace=True, axis=1)
print(df)

# To find the unique identity column so then check from this #is_unique() function
print(df['Identifier'].is_unique)  # True
print(df['Date of Publication'].is_unique)  # False

# Now we can also integrate or assign our unique column with index as a identifier then.

df.set_index(df['Identifier'], inplace=True)

df.head()

# Let Suppose we need to get A specific Row so we use this syntax in DataFrame

print(df.loc[218])

# To Print Specific Row entity using

print(df.loc[218]['Title'])

# For multiple Rows

rows = [472, 480, 218]
data = df.loc[rows]
print(data)

# Now we need to replace str with integer

ext = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(ext.head())
print(df['Date of Publication'].dtype)
# Now the data type is object

df['Date of Publication'] = pd.to_numeric(ext)
print(ext.head())
# for checking the data type of column we use

print(df['Date of Publication'].dtype)
# Now the data type is Float

# Finding keyword from Columns or from Data Set.

pop = df['Place of Publication']
londonEntries = pop.astype(str).str.contains('London')

print(londonEntries)

# To find oxford keyword in data set
print(pop.astype(str).str.contains('Oxford'))


print(df['Place of Publication'].head())


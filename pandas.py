## Create column names during read_csv
df = pd.read_csv(file, names=['MY COLUMN A','MY COLUMN C'])

## filter columns brought in during read_csv
df = pd.read_csv(file, usecols=['MY COLUMN A','MY COLUMN C'])

## Reorder columns by column name
df = df[['A', 'D', 'C', 'B']]

## Get unique values from a column
df['MY COLUMN'].unique()

## Insert column at position
df.insert(3, 'MY COLUMN Z', 'Default Value')

## Return distinct rows based on column value via dropping duplicates
df = df.drop_duplicates(subset ='MY COLUMN', keep = 'first')
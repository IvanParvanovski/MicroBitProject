import pandas as pd

df = pd.read_csv('output.csv', header=None)
header_values = df.iloc[0].tolist()
df = df[1:]
df_cleaned = df[~df.isin(header_values).all(axis=1)]
df_cleaned.columns = header_values
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned.to_csv('cleaned_data.csv', index=False)
print("Duplicates and repeated header rows removed successfully.")
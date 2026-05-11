import pandas as pd

'''clean the data by 
        - removing leading/trailing whitespace, 
        - replacing multiple spaces with a single space, 
        - counting null values, 
        - dropping null values, 
        - changing 'Date' column to 'date' if it exists, 
        - converting it to datetime format if it exists, 
        - and saving the cleaned data to a csv file. 
        Also print the shape of the cleaned data and the first 5 rows of the cleaned data.  '''

def count_null_values(cleaned_data, data_name):
    #count null values in each column    
    null_counts = cleaned_data.isnull().sum()
    print(f"Null values in {data_name}:")
    print(null_counts)
    return cleaned_data

    
def drop_null_values(cleaned_data, data_name):
    if cleaned_data is None:
        print("Warning: Received None instead of a DataFrame!")
        return None
    
    #drop null values in the data
    cleaned_data = cleaned_data.dropna()
    print(f"Shape of data after dropping null values for {data_name}: {cleaned_data.shape}")
    return cleaned_data

def save_cleaned_data(cleaned_data, data_name):
    #save cleaned data to csv file
    cleaned_data.to_csv(f'../data/processed/cleaned_{data_name}.csv', index=True)

    #print the shape of the cleaned data
    print(f"Shape of cleaned {data_name}: {cleaned_data.shape}")

    #print the first 5 rows of the cleaned data
    print(f"First 5 rows of cleaned {data_name}:")
    print(cleaned_data.head())

    return cleaned_data
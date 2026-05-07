import pandas as pd

def load_data(file_path):
    '''load data from a csv file, 
    
    change 'Date' column to 'date' if it exists, 
    
    convert it to datetime format, 
    
    set it as index, and sort the data by date    '''

    df = pd.read_csv(file_path)

    
    #change 'Date' column to 'date' if it exists
    if 'Date' in df.columns:
        df = df.rename(columns={'Date': 'date'})
    
    #convert it to datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    #set 'date' column as index
    df = df.set_index('date')

    #sort the data by date
    df = df.sort_values(by='date')

    #print the shape of the data
    print(f"Shape of data: {df.shape}")

    return df
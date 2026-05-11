import matplotlib.pyplot as plt
def summarize_data(data, data_name):
    '''perform exploratory data analysis (EDA) on the stock market data by
        - summarizing the data by printing the lowest, highest, and average closing price,
        '''
    # Get index of min and max close price
    min_idx = data['Close'].idxmin()
    max_idx = data['Close'].idxmax()

    # Get dates
    min_date = data.loc[min_idx, 'date']
    max_date = data.loc[max_idx, 'date']
    
    #summarize the data
    print(f'=== {data_name} — Key Statistics ===')
    print(f"  Lowest closing price  : ${data['Close'].min():.2f}   on {min_date}")
    print(f"  Highest closing price : ${data['Close'].max():.2f}   on {max_date}")
    print(f"  Average closing price : ${data['Close'].mean():.2f}")

    return data

    
def plot_closing_price(data, data_name):
    '''plot the closing price over time by
        - plotting the closing price over time, 
        - shading the area under the line to make the trend easier to see, 
        - and formatting the y-axis to show dollar values.'''
    
    #plot the closing price over time
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['Close'], label='Closing Price', color='blue')
    # Shade the area under the line to make the trend easier to see
    ax.fill_between(data.index, data['Close'], data['Close'].min() * 0.98,
                alpha=0.08, color='steelblue')

    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    ax.set_title(f'{data_name} — Closing Price Over Time')
    #ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.0f'))
    ax.legend()
    plt.tight_layout()
    plt.show()







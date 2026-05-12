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
    ax.plot(data.index, data['Close'], label='Closing Price', color='steelblue')
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
    return data


def moving_average(data, data_name, window=20):
    '''plot the closing price over time by
        - plotting the closing price over time, 
        - shading the area under the line to make the trend easier to see, 
        - and formatting the y-axis to show dollar values.'''
    
    # Calculate moving average
    data['Moving_Average'] = data['Close'].rolling(window=window).mean()
    print(f'Calculated {window}-day moving average for {data_name}.')

    # Plot closing price and moving average
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data.index, data['Close'], label='Closing Price', color='steelblue')
    ax.plot(data.index, data['Moving_Average'], label=f'{window}-Day Moving Average', color='orange')
    # Shade the area under the line to make the trend easier to see
    ax.fill_between(data.index, data['Close'], data['Close'].min() * 0.98,
                alpha=0.08, color='steelblue')

    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f'{data_name} — Closing Price with {window}-Day Moving Average')
    #ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.0f'))
    ax.legend()
    plt.tight_layout()
    plt.show()

    return data


def interpretation_summary(data, data_name, window):
    '''interpret the results of the EDA by
        - providing a brief summary of the key findings from the EDA, 
        - highlighting any interesting trends or patterns in the data, 
        - and suggesting potential next steps for further analysis.'''
    data['SMA_' + str(window)] = data['Close'].rolling(window=window).mean()
    print(f'=== {data_name} — Interpretation Summary ===')
    print(f"  The lowest closing price was ${data['Close'].min():.2f} on {data['date'][data['Close'].idxmin()]}.")
    print(f"  The highest closing price was ${data['Close'].max():.2f} on {data['date'][data['Close'].idxmax()]}.")
    print(f"  The average closing price over the period was ${data['Close'].mean():.2f}.")
    print("  The stock showed an overall upward/downward trend (depending on the data) with some volatility.")
    print("  Potential next steps could include analyzing volume trends, calculating technical indicators, or performing sentiment analysis on related news articles.")

    # How many days was price above vs below the SMA?
    valid        = data.dropna(subset=['SMA_' + str(window)] )   # drop the first 19 rows with no SMA yet
    above_sma    = (valid['Close'] > valid['SMA_' + str(window)]).sum()
    below_sma    = (valid['Close'] <= valid['SMA_' + str(window)]).sum()
    pct_above    = above_sma / len(valid) * 100

    last_close   = valid['Close'].iloc[-1]
    last_sma     = valid['SMA_' + str(window)].iloc[-1]
    current_pos  = 'ABOVE' if last_close > last_sma else 'BELOW'
    gap_pct      = abs((last_close - last_sma) / last_sma * 100)

    print('WHAT THE MOVING AVERAGE TELLS US')
    print('=' * 50)
    print(f'  Days price was ABOVE the {window}-day SMA : {above_sma}  ({pct_above:.0f}% of the time)')
    print(f'  Days price was BELOW the {window}-day SMA : {below_sma}  ({100-pct_above:.0f}% of the time)')
    print()
    print(f'  Last close  : ${last_close:.2f}')
    print(f'  SMA {window} now  : ${last_sma:.2f}')
    print(f'  Price is currently {current_pos} the average by {gap_pct:.1f}%')
    print()
    if pct_above > 60:
        print(f'  -> {data_name} spent most of this period above its {window}-day average.')
        print(f'     This is a sign of sustained positive momentum — buyers were generally in control.')
    elif pct_above > 40:
        print(f'  -> Price moved back and forth around the average.')
        print(f'     The market was indecisive — no clear dominant trend.')
    else:
        print(f'  -> {data_name} spent most of this period below its {window}-day average.')
        print(f'     This signals sustained selling pressure during the period.')
    print()
    if current_pos == 'ABOVE':
        print(f'  -> At the end of the period: price is above the SMA — short-term trend is UP.')
    else:
        print(f'  -> At the end of the period: price is below the SMA — short-term trend is DOWN.')
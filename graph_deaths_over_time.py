import pandas as pd
import matplotlib.pyplot as plt


def graph_deaths_over_time(data: pd.DataFrame):
    # Convert submission_date to datetime
    data['submission_date'] = pd.to_datetime(data['submission_date'])

    # Create a new DataFrame with submission_date and tot_death
    df_deaths_over_time = data.groupby('submission_date')['new_death'].sum().reset_index()
    df_deaths_over_time.columns = ['submission_date', 'tot_death']

    # Calculate moving averages
    df_deaths_over_time['7_day_avg'] = df_deaths_over_time['tot_death'].rolling(window=7).mean()
    df_deaths_over_time['30_day_avg'] = df_deaths_over_time['tot_death'].rolling(window=30).mean()
    df_deaths_over_time['90_day_avg'] = df_deaths_over_time['tot_death'].rolling(window=90).mean()

    plt.figure(figsize=(12, 8))

    # Actual new deaths (points, orange)
    plt.scatter(df_deaths_over_time['submission_date'], df_deaths_over_time['tot_death'], color='orange',
                label='Actual')

    # 7-day Moving Average (line, dark red)
    plt.plot(df_deaths_over_time['submission_date'], df_deaths_over_time['7_day_avg'], color='darkred',
             label='7-day Moving Average')

    # 30-day Moving Average (line, blue)
    plt.plot(df_deaths_over_time['submission_date'], df_deaths_over_time['30_day_avg'], color='blue',
             label='30-day Moving Average')

    # 90-day Moving Average (line, green)
    plt.plot(df_deaths_over_time['submission_date'], df_deaths_over_time['90_day_avg'], color='green',
             label='90-day Moving Average')

    # Title and labels
    plt.title('COVID-19 Deaths Over Time: 01/22/2020-01/16/2022')
    plt.xlabel('Submission Date')
    plt.ylabel('Total Deaths')

    # Show the legend
    plt.legend()

    # Show the plot
    plt.show()

    # Return the DataFrame
    return df_deaths_over_time























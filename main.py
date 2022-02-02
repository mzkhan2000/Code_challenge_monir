# This is a sample Python script.

# import necessary libraries - Monir
from pathlib import Path
import pandas as pd
import numpy as np
import datetime
from datetime import datetime


class AutomatedTrafficCounter:

    # This is a sample Python script.

    def check_data(data):
        # Use a breakpoint in the code line below to debug your script.
        df = pd.read_csv(data, header=None)

        try:
            if not len(df.columns) == 2:
                raise ValueError('data in this file have more than "datetime" and "cars" columns')
        except (ValueError, IndexError):
            exit('Could not complete request.')

        # add "datetime" and "cars" columns to the dataframe
        df.columns = ["datetime", "cars"]
        # convert the 'datetime' column to datetime format
        df['datetime'] = pd.to_datetime(df['datetime'])
        df.set_index('datetime')

        # Sort column with name datetime if not sorted as date series
        df = df.sort_values(by='datetime')
        # reset the index
        df.reset_index(inplace=True)
        # delete the index
        del df['index']

        return df

    def traffic_count(df):
        # Task 01 code from here
        # sum up cars column in the dataframe to get the number of cars seen in total
        total_number_of_cars = df['cars'].sum()

        # Task 02 code from here
        # A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the
        # number of cars seen on that day

        # convert datetime column to just date and add to dataframe
        df['date'] = pd.to_datetime(df['datetime']).dt.date
        # set 'date' as an index of dataframe
        df.set_index('date')
        # use pandas groupby
        df_car_seen_on_date = df.groupby(["date"]).sum()

        # Task 03: the top 3 half hours with most cars

        # add a column for half hours data to the dataframe
        df['delta'] = df['datetime'].diff().dt.seconds.div(60, fill_value=0)
        # create a dataframe grouped by half hours
        dfm = df.groupby(["delta"])
        dfm = dfm.get_group(30.0)
        dfm = dfm.loc[dfm['cars'].isin(dfm['cars'].nlargest(3))]
        # df_30m_top3 = df_30m_top3
        # reset the index
        dfm.reset_index(inplace=True)
        # delete the index
        del dfm['index']
        # convert the 'datetime' column to datetime format as input
        # df_30m_top3['datetime'] = pd.to_datetime(df_30m_top3['datetime'])
        dfm['date-time'] = pd.to_datetime(dfm['datetime']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        dfm_top3 = dfm

        return total_number_of_cars, df_car_seen_on_date, dfm_top3

    if __name__ == '__main__':
        data = Path("data/traffic_data_ex1.csv")
        # data = Path("/data/traffic_data_ex2.csv")
        df = check_data(data)
        a, b, c = traffic_count(df)

        print("total_number_of_cars:", a)
        print("df_car_seen_on_date:")
        print(b)
        print("Task 03: the top 3 half hours with most cars...")
        print(c)




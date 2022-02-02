# import necessary libraries - Monir
from pathlib import Path
import pandas as pd


class AutomatedTrafficCounter:

    # This is a Python script developed by ABM Moniruzzaman (Monir) for the code test .

    @staticmethod
    def check_data(data):
        # Use a breakpoint in the code line below to debug your script.
        df = pd.read_csv(data, header=None)

        try:
            if df.empty is not False:
                raise ValueError('There is no data in the file')
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

    @staticmethod
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
        dfm['date-time'] = pd.to_datetime(dfm['datetime']).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        dfm_top3 = dfm[['date-time', 'cars']]

        # Task 04: the 1.5 hour period with least cars
        df.set_index('datetime')
        # Timestamp
        time_period = pd.Timedelta("01:30:00")
        period_df = pd.DataFrame(columns=['from_date', 'to_date', 'cars_sum'])
        cars = []
        from_date = []
        to_date = []

        for n in range(1, len(df['datetime'])):
            for m in range(0, len(df['datetime'])):
                if not (df.iloc[n]['datetime'] - df.iloc[m]['datetime']) > time_period:
                    # break
                    if (df.iloc[n]['datetime'] - df.iloc[m]['datetime']) == time_period:
                        # print("From function: 1 and half hours", n, m)
                        nn = n
                        mm = m
                        if cars is not None:
                            car = 0
                        for i in range(mm, nn):
                            car += df.iloc[i]['cars']
                        cars.append(car)
                        from_date.append(df.iloc[m]['datetime'])
                        to_date.append(df.iloc[n]['datetime'])

        # inserting values to the period_df pandas dataframe
        for i in range(0, len(cars)):
            period_df.at[i, 'from_date'] = from_date[i]
            period_df.at[i, 'to_date'] = to_date[i]
            period_df.at[i, 'cars_sum'] = cars[i]

        # Select a pandas dataframe row where the column 'cars_sum' has minimum value
        period_df = period_df[period_df['cars_sum'] == period_df['cars_sum'].min()]

        return total_number_of_cars, df_car_seen_on_date, dfm_top3, period_df


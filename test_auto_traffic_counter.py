from unittest import TestCase
import pandas as pd
from pandas import Timestamp

from auto_traffic_counter import AutomatedTrafficCounter


class TestAutomatedTrafficCounter(TestCase):

    def test_task01(self):
        # this test method tests (checks) that the function named 'task01' in the AutomatedTrafficCounter class -
        # - produces correct results.
        # create a sample dataframe to test function named 'task01' in the AutomatedTrafficCounter class
        d = {'datetime': ['2021-12-01T05:00:00', '2021-12-01T05:30:00', '2021-12-01T06:00:00', '2021-12-02T06:30:00',
                          ], 'cars': [10, 11, 12, 13]}
        df = pd.DataFrame(data=d)
        obg = AutomatedTrafficCounter(df)
        total_number_of_cars = obg.task01()
        expected_total_number_of_cars = 46  # correct total number of cars

        self.assertEqual(total_number_of_cars, expected_total_number_of_cars)

    def test_task02(self):
        # this test method tests (checks) that the function named 'task02' in the AutomatedTrafficCounter class -
        # - produces correct results.
        # create a sample dataframe to test function named 'task02' in the AutomatedTrafficCounter class
        d = {'datetime': ['2021-12-01T05:00:00', '2021-12-01T05:30:00', '2021-12-01T06:00:00', '2021-12-02T06:30:00',
                          ], 'cars': [10, 11, 12, 13]}
        df = pd.DataFrame(data=d)
        obg = AutomatedTrafficCounter(df)
        df = obg.task02()
        df_car_seen_on_date = df['cars'].tolist()

        expected_df_car_seen_on_dates = [33, 13]  # correct numbers of car seen on dates

        self.assertEqual(df_car_seen_on_date, expected_df_car_seen_on_dates)

    def test_task03(self):
        # this test method tests (checks) that the function named 'task02' in the AutomatedTrafficCounter class -
        # - produces correct results.
        # create a sample dataframe to test function named 'task02' in the AutomatedTrafficCounter class
        d = {'datetime': ['2021-12-01T05:00:00', '2021-12-01T05:30:00', '2021-12-01T06:00:00', '2021-12-01T06:30:00',
                          '2021-12-01T07:00:00', '2021-12-01T07:30:00', '2021-12-01T08:00:00', '2021-12-02T15:00:00',
                          ], 'cars': [5, 12, 14, 15, 25, 46, 42, 99]}
        df = pd.DataFrame(data=d)
        obg = AutomatedTrafficCounter(df)
        df = obg.task03()
        cars = df['cars'].tolist()
        datetime = df['date-time'].tolist()

        expected_datetime = ['2021-12-01T07:00:00', '2021-12-01T07:30:00', '2021-12-01T08:00:00']  # correct date-times
        expected_cars = [25, 46, 42]  # correct numbers of car seen on dates

        self.assertEqual(cars, expected_cars)
        self.assertEqual(datetime, expected_datetime)

    def test_task04(self):
        # this test method tests (checks) that the function named 'task02' in the AutomatedTrafficCounter class -
        # - produces correct results.
        # create a sample dataframe to test function named 'task02' in the AutomatedTrafficCounter class
        d = {'datetime': ['2021-12-01T05:00:00', '2021-12-01T05:30:00', '2021-12-01T06:00:00', '2021-12-01T06:30:00',
                          '2021-12-01T07:00:00', '2021-12-01T07:30:00', '2021-12-01T08:00:00', '2021-12-02T15:00:00',
                          ], 'cars': [5, 12, 14, 15, 25, 46, 42, 99]}
        df = pd.DataFrame(data=d)
        obg = AutomatedTrafficCounter(df)
        df = obg.task04()
        from_date = df['from_date'].tolist()
        to_date = df['to_date'].tolist()
        cars = df['cars_sum'].tolist()

        expected_from_date = [Timestamp('2021-12-01 05:00:00')]  # correct from date-times
        expected_to_date = [Timestamp('2021-12-01 06:30:00')]  # correct to date-times
        expected_cars = [31]

        self.assertEqual(from_date, expected_from_date)
        self.assertEqual(to_date, expected_to_date)
        self.assertEqual(cars, expected_cars)

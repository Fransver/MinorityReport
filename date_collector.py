import datetime
import pandas as pd


class DateCollector:

    def get_range_of_dates(self, starting_date):

        today = datetime.date.today()
        dates = pd.date_range(starting_date, today).tolist()

        return dates



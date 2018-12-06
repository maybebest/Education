"""Static Method"""


class Dates:
    """Date class representation"""

    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


date = Dates("03-12-2008")

print(date.get_date(), date.to_dash_date("03/12/2008"),
      Dates.to_dash_date("03/12/2008"))

# 03-12-2008 03-12-2008 03-12-2008

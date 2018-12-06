"""Static Method"""

class Dates:
    """Date class representation"""

    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates):

    def get_date(self):
        return Dates.toDashDate(self.date)


date = Dates("03-12-2008")
date_2 = DatesWithSlashes("03/12/2008")

print(date.get_date(), date_2.get_date())  
# 03-12-2008 03-12-2008

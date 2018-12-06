class Contact(object):
    def __init__(self, age, gender, first_name, last_name, phone_number):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.recent_calls = []
        self.favorite = False

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)
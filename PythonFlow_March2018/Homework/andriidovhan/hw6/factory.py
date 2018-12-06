class GreekGetter(object):

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()


if __name__ == '__main__':
    e, g = get_localizer(language="English"), get_localizer(language="Greek")
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))
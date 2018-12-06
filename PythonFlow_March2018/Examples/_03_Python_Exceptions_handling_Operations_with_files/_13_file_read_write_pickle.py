"""Pickle"""

import pickle

FEEDBACK = {
    'user_1': ["Python is awesome!"],
    'user_2': ["Yeah its great!!"],
}

with open("python_feedback", 'wb+') as FILE:

    pickle.dump(FEEDBACK, FILE)

    FILE.seek(0)

    data = pickle.load(FILE)
    print("Data type: %s; Data is: %s; " % (type(data), data))
    # Data type: <class 'dict'>;
    # Data is: {'user_1': ['Python is awesome!'], 'user_2': ['Yeah its great!!']};

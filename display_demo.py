import six

def display_data(data):
    print("{} from {} backers = {}%!".format(data['pledged'], data['backers'], data['percent']))

def display_happy():
    print(":-)")

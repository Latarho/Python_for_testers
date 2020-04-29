from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).replace("'", "").replace("\\", "").replace("<", "").replace('"', "")

testdata = [Contact(first_name="", middle_name="", last_name="", title="", company="", address="", mobile="", work="", email="", notes="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
            last_name=random_string("last_name", 10), title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), mobile=random_string("mobile", 10), work=random_string("work", 10),
            email=random_string("email", 10), notes=random_string("notes", 10))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
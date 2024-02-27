# 2)Create a class for creating and writing data to a text file. The class must have _enterandexit_ defined.
# _ente_r must use the built in 'open' to open the file and set the file pointer to self.
# _exit_ must close the file pointer on exit.
# If the user entered text contains the word 'bug' then_exit_ must delete the file on exiting.
# Or if any exception has occurred, then also_exit_ must delete the file. (remember to close file before deleting)
# Use a 'with block to execute the logic.


import os
from contextlib import contextmanager

class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    @contextmanager
    def open_file(self):
        try:
            with open(self.filename, 'w') as file:
                yield file
        except Exception as e:
            print(f"An exception occurred: {e}")
            self.delete_file()

    def delete_file(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File '{self.filename}' deleted.")

try:
    with FileWriter("example.txt") as fw:
        with fw.open_file() as file:
            file.write("Some text without 'bug'.")
except Exception as e:
    print(f"An exception occurred: {e}")

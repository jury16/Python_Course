"""
Write your own class MyOpen, the objects of which must support the context manager protocol.
It should work similarly with open ('file.txt', 'w +') as f.
So you can use it like this:
with MyOpen (file.txt ’,’ w + ’) as f:
"""


class MyOpen:
    def __init__(self, file_name, method):
        self.resource = open(file_name, method)

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        self.resource.close()


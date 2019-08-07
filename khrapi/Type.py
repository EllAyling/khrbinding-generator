
class Type(object):
    def __init__(self, api, identifier):
        self.api = api
        self.identifier = identifier
        self.namespace = None
        self.require = None

    def __lt__(self, other):
        return self.identifier < other.identifier

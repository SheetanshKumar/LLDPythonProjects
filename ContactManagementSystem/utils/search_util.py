class Search:

    def __init__(self):
        pass

    def searchInStringPrefix(self, item, st):
        if len(item) > len(st):
            return False

        for i in range(len(item)):
            if item[i] != st[i]:
                return False
        return True


class Set(list):

    def contains(self, elem):
        if self.__contains__(elem):
            return True
        else:
            return False

    def size(self):
        return len(self)

    def add(self, elem):
        if not self.contains(elem):
            self.append(elem)

    def delete(self, elem):
        self.remove(elem)

    def __or__(self, lst):
        new_list = []
        for elem in self:
            new_list.append(elem)
        for elem in lst:
            if not new_list.__contains__(elem):
                new_list.append(elem)
        return new_list

    def __sub__(self, lst):
        new_list = []
        for elem in self:
            new_list.append(elem)
        for elem in lst:
            if new_list.__contains__(elem):
                new_list.remove(elem)
        return new_list

    def __and__(self, lst):
        new_list = []
        for elem in self:
            if lst.__contains__(elem):
                new_list.append(elem)
        return new_list

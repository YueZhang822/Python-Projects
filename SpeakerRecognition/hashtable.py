from collections.abc import MutableMapping


class Flag():
    """
    This is a unique class, which is used later to mark the return value of some functions.
    """
    pass

flag = Flag()


class Hashtable(MutableMapping):
    P_CONSTANT = 37   # polynomial constant, used for _hash

    def __init__(self, capacity, default_value, load_factor, growth_factor):
        """
        Constuctor of the hashtable, which keep track of the capacity/default value/
        load factor/growth factor/ture length/occupied length of the table.
        """
        self._items = [None] * capacity   # Initially all empty
        self.capacity = capacity
        self.default_value = default_value
        self.load_factor = load_factor
        self.growth_factor = growth_factor
        self.true_len = 0   # the number of items that are not deleted
        self.occupied_len = 0   # the number of all items in the hashtable, include deleted ones

    def _hash(self, key):
        """
        This method takes in a string and returns an integer value
        between 0 and self.capacity.
        """
        val = 0
        for letter in key:
            val = self.P_CONSTANT * val + ord(letter)
        return val % self.capacity

    def __setitem__(self, key, val):
        """
        This method takes in a key-value pair and add it into the hashtable.
        """
        index = self._hash(key)
        while self._items[index] and self._items[index][0] != key:
            index += 1
            if index == self.capacity:
                index = 0
        if self._items[index] == None:
            self.true_len += 1
            self.occupied_len += 1
        self._items[index] = (key, val, True)
        # rehash when the occupied rate goes beyond the load factor
        if self.occupied_len / self.capacity > self.load_factor:
            self.rehash()

    def __getitem__(self, key):
        """
        This methos takes in a key and search it in the hashtable. Returns the value of it if 
        it is in the hashtable, otherwise returns the default value.
        """
        def search_through(idx, end):
            while idx < end:
                if not self._items[idx]:
                    return self.default_value
                if self._items[idx][0] == key:
                    return self._items[idx][1]
                idx += 1
            return flag   # return flag means the key has not been searched
        index = self._hash(key)
        res = search_through(index, self.capacity)   # search from hash backwards to the end
        if res != flag:
            return res 
        res2 = search_through(0, index)   # if not been found in the right part, then search from leftmost
        return res2

    def __delitem__(self, key):
        """
        This method takes in a key and delete it from the hashtable if it's in it, otherwise
        raise keyerror. It does not physically delete an item from hashtable, buy just mark
        it with False third tuple value.
        """
        def search_through(idx, end):
            while idx < end:
                if not self._items[idx]:
                    raise KeyError(key)
                if self._items[idx][0] == key:
                    if self._items[idx][2]:
                        self._items[idx] = (key, self.default_value, False)
                        self.true_len -= 1
                        return flag   # return flag means the key has already been searched
                    else:
                        raise KeyError(key) 
                idx += 1
        index = self._hash(key)
        res = search_through(index, self.capacity)   # search from hash backwards to the end
        if res == flag:
            return
        res2 = search_through(0, index)    # if not been found in the right part, then search from leftmost
        if res2 == flag:
            return
        raise KeyError(key)

    def rehash(self):
        """
        This method expand the hashtable to the size of its current size mutiplies the growth_factor.
        And rehashes all the items in the hashtable.
        """
        self.capacity *= self.growth_factor
        table = [None] * self.capacity
        self._items, table = table, self._items
        self.true_len = 0
        self.occupied_len = 0
        for idx, elem in enumerate(table):
            if elem and elem[2]:   # only set these items whose state is True
                self.__setitem__(elem[0], elem[1])

    def __len__(self):
        """
        This method returns the number of items stored in the hashtable, that are not deleted.
        """
        return self.true_len

    def __iter__(self):
        """
        Skipped for this project.
        """
        raise NotImplementedError("__iter__ not implemented")

    def display(self):
        """
        This method defines a way to display the hashtable.
        """
        print(f"Capacity = {self.capacity}")
        for idx, elem in enumerate(self._items):
            if elem and elem[2]:
                print(f"{idx} : {elem}")

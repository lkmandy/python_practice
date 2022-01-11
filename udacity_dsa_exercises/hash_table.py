"""
Write a HashTable class that stores strings in a hash table, where keys are calculated
using the first two letters of the string.
"""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000


    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]


    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                if string in self.table[hash_value]:
                    return hash_value
        return -1


    def calculate_hash_value(self, string):
        """Helper function to calulate a hash value from a string."""
        hv = ord(string[0]) * 100 + ord(string[1])
        return hv
    

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')

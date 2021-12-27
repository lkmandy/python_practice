"""
- Create a function in "Classy" that takes a string as input and adds it to the "items" list.
- Another method should calculate the "classiness" value based on the items.
- The following items have classiness points associated with them:
 "tophat" = 2, "bowtie" = 4, "monocle" = 5
- Everything else has 0 points. Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []
    
    def addItem(self, newItem):
        return self.items.append(newItem)
        
    def getClassiness(self):
        firstClass = {"tophat": 2, "bowtie": 4, "monocle": 5, }
        classiness = 0
        if  len(self.items) > 0:
            for value in self.items:
                if value in  firstClass.keys():
                    classiness += firstClass[value]
                else:
                    classiness += 0
        return classiness

        
# Test cases
me = Classy()

# # Should be 0
print (me.getClassiness())

me.addItem("tophat")

# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("monocle")

# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())
class HashTable:
    def __init__(self):
        self.MAX = 50
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return(h % self.MAX)

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
                

    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
            

test = HashTable()

test["test 1"] = 130
test["test 20"] = 150
test["test 36"] = 309
test["test 42"] = 42
test["test 58"] = 100
test["test 69"] = 0
test["test 70"] = 450
test["test 81"] = 180
test["test 92"] = 360
test["march 6"] = 6
test["march 17"] = 17

print(test["test 1"])
print(test["test 20"])
print(test["test 36"])
print(test["test 42"])
print(test["test 58"])
print(test["test 69"])
print(test["test 70"])
print(test["test 81"])
print(test["test 92"])
print(test["march 6"])
print(test["march 17"])
print('--------------------------------------------------------------------------------')
print(test.arr)
del test["march 17"]
print('--------------------------------------------------------------------------------')

print(test.arr)

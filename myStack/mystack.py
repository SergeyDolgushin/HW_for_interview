class myStack:
    def __init__(self, object):
        self._object = object
    
    def isEmpty(self):
        if (len(self._object)):
            return True
        return False
    
    def push(self, new_item):
        self._object += new_item
    
    def pop(self):
        last_item = self._object[-1]
        self._object = self._object[0:-1]
        return last_item

    def peek(self):
        last_item = self._object[-1]
        return last_item
    
    def size(self):
        size_stack = len(self._object)
        return size_stack

    def __str__(self):
        return self._object


if __name__ == '__main__':

    test_str = 'A'
    string = myStack(test_str)
    print(string.isEmpty())
    print(string)
    print(string.push('2455'))
    print(string)
    

        

    
    

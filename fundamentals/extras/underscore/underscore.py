class Underscore:
    def filter(self, iterable, callback):
        list=[x for x in iterable if callback(x)]
        return list
    def find(self, iterable, callback):
        list=[x for x in iterable if callback(x)]
        return (list)
    def map(self, iterable, callback):
        list=[callback(x) for x in iterable]
        return list
    def reject(self, iterable, callback):
        list=[x for x in iterable if not callback(x)]
        return list

_ = Underscore()
filter = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print("*"*30,"\n",f"result of filter method {filter}")
map = _.map([i for i in range(1,7)], lambda x:x*2)
print("*"*30,"\n",f"result of map method {map}")
find = _.find([i for i in range(1,7)], lambda x:x>4)
print("*"*30,"\n",f"result of find method {find}")
reject = _.reject([i for i in range(1,7)], lambda x: x % 2 == 0)
print("*"*30,"\n",f"result of reject method {reject}")
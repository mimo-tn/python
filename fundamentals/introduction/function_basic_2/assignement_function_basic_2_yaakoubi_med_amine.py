######### 1 ##################
def countdown(i):
    for c in range(i,-1,-1):
        print(c)
countdown(5)
######### 2 ##################
def print_and_return(x):
    print(x[0])
    return x[1]
res = print_and_return([1,2])
print(res)
######### 3 ##################
def  first_plus_length(x):
    return x[0] + len(x)
res = first_plus_length([1,2,3,4,5]) 
print (res)
######### 4 ##################
def values_greater_than_second(x):
    new_list = []
    if len(x) >= 2:
        for element in x:
            if element > x[1]:
                new_list.append(element)
    if len(new_list) >= 2:
        print(len(new_list))
        return new_list
    else:
        return False
res = values_greater_than_second([5,2,3,2,1,4])
print(res)
res = values_greater_than_second([3])
print(res)
######### 5 ##################
def length_and_value(l,v):
    new_list = []
    for i in range(l):
        new_list.append(v)
    return new_list
res = length_and_value(4,7)
print (res)
res = length_and_value(6,2)
print (res)
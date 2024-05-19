new_list = [8,6,4,9,5,2,1,7]
for i in range(len(new_list) - 1):
    min = new_list[i]
    print("****"*20,"\n",f"itiration numer {i}")
    for j in range(i,len(new_list)):
        if new_list[j] < min :
            min = new_list[j]
            new_list[i],new_list[j] = new_list[j],new_list[i]
    print(f"in this itiration this is the result of our sort algorithm {new_list}")
print(f"this is the list sorted {new_list}")
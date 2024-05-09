####### 1 Update Values in Dictionaries and Lists #######
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]["last_name"]="Bryant"
print(students)
sports_directory["soccer"][0]="Andres"
print(sports_directory)
z[0]["y"]=30
print(z)

###### 2 Iterate Through a List of Dictionaries #######
def iterateDictionary(dic):
    new_list = []
    for i in range(len(dic)):
        new_list.append([key + "-" + val for key,val in dic[i].items()])
    return new_list

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
res = iterateDictionary(students) 
for i in res:
    print(i[0] + ", " +i[1])

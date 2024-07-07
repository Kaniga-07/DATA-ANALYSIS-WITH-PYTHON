#create list

my_list = [1,2,3,4,5]
#add
my_list.append(6)
#remove
my_list.remove(3)
#update
my_list[0] = 10

print("Updated List:",my_list)


#create dictionary

my_dict = {'name':'John','age':25,'city':'Delhi'}
#add
my_dict['gender'] = 'Male'
#remove
del my_dict['age']
#update
my_dict['city']='Mumbai'

print("Updated Dictionary :",my_dict)

#create set

my_set = {1,2,3,4,5}
#add
my_set.add(6)
#remove
my_set.remove(3)
#update
my_set.discard(1)
my_set.add(10)

print("Updated set: ",my_set)

# printing sets in python
set_one = {2,4,6}
set_two = {5,7,9}

# concatnation
print(set_one | set_two)

# checking datatype
print(type(set_one),type(set_two))

#printing key and pair values
obj ={1:"cha",2:"ka",3:"la"}
print(obj)

# pusing one more ele into set
obj[4]=("dhu")
print(obj)

# removing ele
obj_remove= obj.pop(2)
print(obj_remove)
print(obj)
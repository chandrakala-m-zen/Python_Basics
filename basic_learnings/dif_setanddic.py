# difference between sets and dictionary

# elements are accessesd by directly
sets = {2,4,6,4,6,4};
print(sets) #{2, 4, 6} to store piece of unique values
print(type(sets))   #<class 'set'>

# in string formate
set_str = {'a','v','b','d','e','f','a','b'};
print(set_str) # {'f', 'v', 'a', 'b', 'd', 'e'}


# Values are accessed by using keys
# to store piece of information
dic = {1:"cha",2:"chi",3:"khi"};
print(dic) #{1: 'cha', 2: 'chi', 3: 'khi'}

# add element to the dictionary
dic[4] = "kheer" 
print(dic) #{1: 'cha', 2: 'chi', 3: 'khi', 4: 'kheer'}

#removing elements from the dictionary
print(dic)
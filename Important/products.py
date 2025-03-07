"""
SORTING DICTIONARIES BY VALUES
sorted() function always sorts dictionaries by keys and returns as a list
if we want to sort by value then we have to use lambda function which helps us to create one line functions:
sorted(my_dict.items(), key=lambda item: item[1])
in here items() returns key, value pairs from my_dict. and item[0] represents keys, item[1] represents value

HOW TO COUNT AN ITEM IN A ARRAY WITH METHOD
my_list.count(item) returns that how many times item number appears in the list

CREATING A LIST WITH UNIQUE VALUES(NO DUPLICATES)
only_items = set(ids) stores every element for once so your list stores only distinct values

IMPORTANT HASH MAP(DICTIONARY) METHODS
my_dicy = {}

my_dict.values() -> returns values
my_dict.items() -> returns key,value pairs
my_dict.keys() -> returns keys

if you want to convert a list to dictionary:
my_list = []
my_dict = dict(my_list)

if you want to convert dictionary to list
my_dict = {}
my_list = list(my_dict)

HOW TO REMOVE AN ELEMENT FROM A LIST BY INDEX
my_list = [10, 20, 30, 40, 50]
del my_list[0:3] #[40,50]
deletes 0. index to 2. index

OR

my_list = my_list[3:]

HOW TO REMOVE SINGLE ELEMENT FROM LIST POP() OR POP(0)
my_list = [10, 20, 30, 40]
my_list.pop() as a default remove the last element of the list which is 40
but if you give an index:
my_list.pop(0) it removes 0. index which is 10

"""


# keys ids, values frequency
def deleteProducts(ids, m):
    counter = {}

    only_elements = set(ids)
    for element in only_elements:
        counter[element] = ids.count(element)

    sorted_counter = sorted(counter.items(), key=lambda item: item[1])  # sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True) descending order

    for i in range(m):
        sorted_counter.pop(0)

    retval = dict(sorted_counter)

    return len(retval)


# ids = [1,1,1,2,3,2,4,5]
ids = [1, 1, 2, 3, 4, 5, 5]
m = 2

print(deleteProducts(ids, m), " distinct ids remained")






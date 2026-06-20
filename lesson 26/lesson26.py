list1=[1,2,3]
list2=['a','b','c']
zipped_list = list(zip(list1,list2))
print(zipped_list)
zipped_reverse=list(zip(list1,reversed(list2)))
print(zipped_reverse)
zipped_dict=dict(zip(list1,list2))
print(zipped_dict)
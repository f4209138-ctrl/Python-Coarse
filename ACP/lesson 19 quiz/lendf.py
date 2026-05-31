def count_matching_strings(string_list):
    count=0
    for string in string_list:
        if len(string)>=2 and string[0]==string[-1]:
            count+=1
    return count
sample_list=['abc','xyz','aba','a']
result=count_matching_strings(sample_list)
print(result)
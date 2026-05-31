def analyze_list(numbers):
    if not numbers:
        return "The list is empty"
    total_sum= sum(numbers)
    average=total_sum/len(numbers)
    largest=max(numbers)
    smallest=min(numbers)
    return total_sum,average,largest,smallest
numbers=[4,12,8,23,25,42,1]
analysis=analyze_list(numbers)
print(analysis)
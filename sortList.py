even = [2,4,6,8]
odd = [1,3,5,7,9]
empty_list = []

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers) #sorted creates new list; .sort doesn't
print(sorted_numbers)
print(numbers)

digits = list("4312419") #creates list of strings compared to list of ints
print(digits)

#more_numbers = list(numbers)
#more_numbers = numbers [:]
more_numbers = numbers.copy()
print(more_numbers)

print (numbers is more_numbers) #false not the same list
print (numbers == more_numbers) #same values

# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)

# even.sort(reverse=True)
# print(even)
# print(another_even) #same because sort does not generate new list (mutable)
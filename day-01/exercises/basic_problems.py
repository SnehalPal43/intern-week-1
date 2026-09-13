#1. Reverse a String

def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello World"))  

#2. Check Palindrome

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar"))  

#3. Largest and Second Largest Number

def find_largest_and_second(numbers):
    largest = max(numbers)
    second_largest = sorted(set(numbers))[-2]
    return largest, second_largest

nums = [10, 25, 8, 40, 15]
l, s = find_largest_and_second(nums)
print("Largest:", l)
print("Second Largest:", s)

#4.remove duplicates

def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))

nums = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates(nums)

print("Original List:", nums)
print("After Removing Duplicates:", result)

#5.duplicate number

numbers = [1, 2, 3, 4, 2, 5, 3]
duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("List:", numbers)
print("Duplicate numbers found:", duplicates)

#6. character frequency

text = "hello"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print("String:", text)
print("Character Frequency:", frequency)

#7.first non-repeating character

text = "swiss"
#Count frequency of each character
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1
#Find the first character with a count of 1
first_non_rep = None
for char in text:
    if frequency[char] == 1:
        first_non_rep = char
        break 

print("String:", text)
print("First Non-Repeating Character:", first_non_rep)

#8.merge sorted arrays

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i = i + 1
        else:
            merged.append(arr2[j])
            j = j + 1
    
    while i < len(arr1):
        merged.append(arr1[i])
        i = i + 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j = j + 1
        
    return merged

array1 = [1, 3, 5]
array2 = [2, 4, 6]

result = merge_sorted_arrays(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Merged Sorted Array:", result)

#9.common elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = []

for item in list1:
    if item in list2:
        if item not in common_elements:  
            common_elements.append(item)

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common_elements)

#10.Stack Implementation using a List LIFO

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("Pushed:", item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty!"
        return self.items.pop()

    def display(self):
        print("Current Stack:", self.items)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

my_stack.display()

print("Popped item:", my_stack.pop())
my_stack.display()

#11.Queue Implementation using a List FIFO 
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print("Enqueued:", item)

    def dequeue(self):
        if len(self.items) == 0:
            return "Queue is empty!"
        return self.items.pop(0)

    def display(self):
        print("Current Queue:", self.items)

my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

my_queue.display()

print("Dequeued item:", my_queue.dequeue())
my_queue.display()

#12.Maximum Subarray Sum
def max_subarray_sum(nums):
    if not nums:
        return 0
        
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Decide whether to add to existing subarray or start fresh
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Track the maximum sum found so far
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray_sum(numbers)
print("Array:", numbers)
print("Maximum Subarray Sum:", result)

#13.Sorting without built-in functions

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", numbers)
sorted_list = bubble_sort(numbers)
print("Sorted List:", sorted_list)

#14.Prime Number Check

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = 11
if check_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")

#15.Factorial
def find_factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

number = 5
result = find_factorial(number)
print("Factorial of", number, "is", result)
# a number is even or odd
def is_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# reverse a string
def reverse_string(s):
    start = 0
    end  = len(s) - 1
    while start < end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1
    return s

# Find the Largest of Three Numbers
def largest_number(arr):
    maxi = arr[0]
    for i in arr:
        maxi = max(maxi, i)
    return maxi

# Check for Palindrome
def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

# Sum of Elements in a List
def sum_of_list_elements(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Count Vowels in a String
def count_vowels(s):
    total = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'i':
            total += 1
    return total

# Fibonacci Series
def fibo_series(n):
    arr = [0, 1]
    j = 2
    while j <= n:
        arr.append(arr[j-1] + arr[j-2])
        j += 1
    return arr

#  Factorial of a Number
def factorial_of_n(n):
    fact = 1
    for i in range (1, n+1):
        fact = fact * i
    return fact

# Remove Duplicates from List
def remove_duplicates_from_list(arr):
    count = {}
    ans = []
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for i in count:
        ans.append(i)
    return ans

# Check Prime Number
def is_prime(n):
    if n < 2: 
        return False
    
    for i in range (2, n):
        if n % i == 0:
            return False

    return True
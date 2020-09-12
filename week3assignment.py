# "in" and "not in" Logical Operators ?
# These logical operators are responsible for checking whether a particular condition is true or not, and then returning the boolean status of the condition
# The in operator checks if a value is in a sequence and not in is responsible for checking if a value is not in a subsequence 
# EXAMPLE : THe code below checks whether the letter "w" is in a word oin the list, then returns the number of words in the list with that particular letter 

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0
for word in items:
    if "w" in word:
        acc_num = acc_num +1
        
        
        
# How does precedence of operators work ?
# In an expression, the Python interpreter evaluates operators with higher precedence first.
# for example, the multiplication operation is interpreted before the addition in a simple equation of addition and multiplication only. 
# Multiplication get evaluated before the addition operation
5 + 5 * 3
# Result: 20
# Parentheses () overriding the precedence of the arithmetic operators
(5 + 5) * 3
# Output: 30


# Conditional Execution statements ? :
# Conditional statements are statements that can be used to check if conditions exist, then return a boolean, and based on the returned boolean, execute a block of code or not
# Conditional operators in ptyhon are if, else, elif



# How does accumulator pattern work ?
# Accumulator pattern refers to the process of iterating and updating a variable 
# Accumulator pattern is often used to count instances of a sequence or of elements in a sequence 
# An EXAMPLE of accumulator pattern can be seen below, counting the number of vowels in each word in the sentence s . 

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.
num_vowels = 0 
for ele in s:
    for vowel in vowels:
        if vowel in ele:
            num_vowels = num_vowels + 1




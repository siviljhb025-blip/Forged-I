
# ==================================
# QUESTION 1: FILTER OUT PRIME NUMBERS
# ==================================

def filter_primes(numbers):
    """
    Takes a list of integers and returns a new list
    with all prime numbers removed.

    Example:
    --------
    >>> filter_primes([2, 3, 4, 5, 6, 7, 8])
    [4, 6, 8]

    Notes:
    ------
    - A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    - Use loop logic to determine primality (no external libraries).
    """
  
    
    for number in numbers:
        if number // number == 1:
            return number
        
    for number in numbers:
        if number// 1 == number:
            return number
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
print(filter_primes(numbers))
            


# ==================================
# QUESTION 2: DRAW A SQUARE
# ==================================

def draw_square(size):
    """
    Draws a square using asterisks ('*') and returns it as a string.

    Example:
    --------
    >>> print(draw_square(3))
    ***
    ***
    ***

    Notes:
    ------
    - Each row should contain exactly `size` number of asterisks.
    - Use '\n' to separate rows.
    - Do not print inside the function; just return the final string.
    """
    # pass  # TODO: implement function logic here

    row = "***"

    for i in row:
        return "***\n***\n***" 
    
print(draw_square("size"))


# ==================================
# QUESTION 3: AFFORDABLE ITEMS
# ==================================

def get_affordable_items(data):
    """
    Takes a list of dictionaries representing store items and
    returns a dictionary of items that are affordable (price < 100).

    Example:
    --------
    >>> data = [
    ... {"name": "Laptop", "price": 120.0, "in_stock": True, "category": "electronics"},
    ... {"name": "Book", "price": 15.0, "in_stock": False, "category": "books"},
    ... {"name": "Phone", "price": 80.0, "in_stock": True, "category": "electronics"}
    ... ]
    >>> get_affordable_items(data)
    {'Book': 15.0, 'Phone': 80.0}

    Notes:
    ------
    - Only include items with a price below R100.
    - Return a dictionary where the key = item name, value = price.
    """
    pass  # TODO: implement function logic here


# ==================================
# BONUS QUESTIONS (Intermediate Practice)
# ==================================

def reverse_words(sentence):
    """
    Takes a sentence string and returns it with the word order reversed.

    Example:
    --------
    >>> reverse_words("The sky is blue")
    'blue is sky The'
    """
    words = sentence.split()
    return " ".join(reversed(words))
   
print(reverse_words("blue is sky The"))
    


def count_vowels(word):
    """
    Counts and returns the number of vowels in a given word.

    Example:
    --------
    >>> count_vowels("forged")
    2

    Notes:
    ------
    - Vowels are: a, e, i, o, u
    - The function should be case-insensitive.
    """
    pass  # TODO: implement function logic here


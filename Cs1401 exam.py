


C4 = int(input("followers?: "))
D4 = int(input("following?: "))
ratio = C4/D4

if  ratio > 1:
  print("solid  can follow")
elif 0.5 <= ratio <= 1:
  print("Average")  
else:
  print("low")  
  
  
def listFromFile(words_file):
  """_summary_

  Args:
      words_file (file): file

  Returns:
      strings of words: strings
  """
  try: 
      with open(words_file,"r") as file:
        word = file.read()
        word_lst = word.split()
      return word_lst 
  except FileNotFoundError:
    print(f"Error: File {words_file} not found.")
    return None

def vowelCounter(word):
    letter = "AEIOUaeiou"
    count = 0
    for char in word:
        if char in letter:
            count += 1
    return count

def wordVowelCountDict(word_list):
    vowelDict = {}
    for word in word_list:
        vowelDict[vowelCounter(word)] = word
    return vowelDict

def main():
    wordList = listFromFile("word.txt") 
    wordNumVowels = wordVowelCountDict(wordList)
    for word, count in wordNumVowels.items():
        print(f"{word} has {count} vowels")

main()
    
print(main())    

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
      

old_list = ['hello', 'world', 'python']
new_list = [obj[:1] + 'x' + obj[2:] if len(obj) > 1 else obj for obj in old_list]
print(new_list)  # Output: ['hxll', 'wxrld', 'pxthon']     

def remove_negative_numbers(numbers_list):
    """
    This function removes negative numbers from a list of numbers.

    Args:
        numbers_list (list): A list of numbers.

    Returns:
        list: A new list of numbers with negative numbers removed.
    """
    for index in range(len(numbers_list) - 1, -1, -1):
        number = numbers_list[index]
        if number < 0:
            numbers_list.pop(index)
    return numbers_list
  
  
def has_m(word):
    """
    This function takes a string word as a parameter and returns a new string with the letter "m" removed,
    provided that the letter "m" does not appear as the first or the last letter in the word.
    If the letter "m" appears as the first or the last letter, the function returns the original word.

    >>> has_m('hello')
    'hello'
    >>> has_m('hamilton')
    'hailton'
    """
    if len(word) < 2:
        return word
    elif word[0] == 'm' or word[-1] == 'm':
        return word
    else:
        return word.replace('m', '', 1)
      
      
def sum_of_digits(n):
    """
    This function takes a positive integer n as input and returns the sum of its digits using recursion.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of the digits of n.

    Examples:
        >>> sum_of_digits(12345)
        15
        >>> sum_of_digits(1000)
        1
        >>> sum_of_digits(7)
        7
    """
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)      


def get_twins_names(twins_data):
    """
    This function takes a list of tuples containing twin names and their year of birth,
    and returns a dictionary of twin names. The names that appear first in the tuple
    are used as keys.

    Args:
        twins_data (list): A list of tuples containing twin names and their year of birth.

    Returns:
        dict: A dictionary of twin names.
    """
    twins_names = {}
    for twin in twins_data:
        twins_names[twin[0]] = twin[1]
    return twins_names
  
  
  

def write_to_file_twins_age(output_file, twins_data, current_year):
    """
    This function takes an output file name, a list of tuples containing twin names and their year of birth,
    and an integer representing the current year or future year. The function writes to file the age of
    each pair of twins in the specified year.

    Args:
        output_file (str): The name of the output file.
        twins_data (list): A list of tuples containing twin names and their year of birth.
        current_year (int): The current year or future year.
    """
    with open(output_file, 'w') as f:
        for twin in twins_data:
            age = current_year - twin[1]
            f.write(f"{twin[0]} and {twin[1]} are {age} years old in {current_year}\n")        
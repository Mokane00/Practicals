words = ["bat","bolt","more","not","now","pit","sand","six","want"]
words_end_t = [word for word in words if word[-1] == "t"]
print(words_end_t)
words_now_e = [word[0] + "e" + word[2:] if len(word) > 1 else word for word in words]
print(words_now_e)


def listFromFile(words_file):
  try:
    with open(words_file,"r") as file:
      word_lst = file.read()
    return word_lst
  except FileNotFoundError:
    print(f"Error: File {words_file} not found.")
    return None
  
  
def vowelCounter(word_lst):
  letter = ["A","E","I","O","U","a","e","i","o","u"]
  count = 0
  for char in word_lst:
    if char in letter:
      count += 1
    return count
  
  
def wordVowelCountDict(word_lst):
  vowelDict = {}
  for word in word_lst:
    vowelDict[vowelCounter(word)] = word
  return vowelDict

def main():
  wordList = listFromFile("word.txt")
  wordNumVowels = wordVowelCountDict(wordList)
  for word, count in wordNumVowels.items():
    print(f"{word} has {count} vowels")
    
    
print(main())


def remove_negative_numbers(numbers_lst):
  """This function removes negative numbers from a list of numbers

  Args:
      numbers_lst (list):list of numbers
  return:
    list without negative numbers    
  """
  for i in range(len(numbers_lst) - 1, - 1, - 1):
    number = numbers_lst[i]
    if number < 0:
      numbers_lst.pop(i)
  return numbers_lst

print(remove_negative_numbers([2,-2,-3,4,3,-10]))



def has_m(word: str):
  """
  This function takes a string word as a parameter and return a new string with letter "m" removed,provided that the letter "m" does not appear as the first or the last letter in the word.If the letter "m" appears as the first or the last letter , the function returns the returns the original word.
  

  Args:
      word (string): string word
  return:
      removes "m" from the string and if the letter "m" starts or end the original string  
  >>> has_m("hello")
  "hello" 
  >>> has_m("hamilton") 
  "hailton"     
  """
  if len(word) < 2:
    return word
  elif word[0] == "m" or word[-1] == "m":
    return word
  else:
    return word.replace("m","",1)
  
  
print(has_m("home")) 
print(has_m("mom"))
print(has_m("consumer"))


def sum_of_digits(n):
  """This function takes a positive integer n as input and return sum of it's digits using recursion

  Args:
      n (int): Positive integer
  Returns:   
      int: The sum of the digits of n
      
  >>> sum_of_digits(12345)
  15
  >>> sum_of_digits(1000)
  1
  >>> sum+of_digits(7)
  7    
  """
  if n < 10:
    return n
  else:
    return (n % 10) + sum_of_digits(n // 10)
  
  
print(sum_of_digits(21))
  

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
  
  # Example data
twins_data = [("Alice", 2001),("Alan",2001),("Bob", 2002),("Robert",2002),("Charlie", 2003),("Charls",2003),("David", 2004),("Dave",2004)]

# Get the dictionary of twin names
twins_names = get_twins_names(twins_data)
print(twins_names)  # Output: {'Alice': '2001', 'Bob': '2002', 'Charlie': '2003', 'David': '2004'}


def write_to_file_twins_age(output_file, twins_data:list, current_year:int):
    """
    This function takes an output file name, a list of tuples containing twin names and 
    and an integer representing the current year or future year. The function writes to 
    each pair of twins in the specified year.

    Args:
        output_file (str): The name of the output file.
        twins_data (list): A list of tuples containing twin names and their year of birth
        current_year (int): The current year or future year.
    """
    with open(output_file, 'w') as f:
        for twin in twins_data:
            age = current_year - twin[2]
            f.write(f"{twin[0]} and {twin[1]} are {age} years old in {current_year}\n") 
        

twins_data2 = [("Mpho","Limpho",1998),("Neo","Lineo",2001),("Khosi","Morena",2012)]

print(write_to_file_twins_age("twins_ages.txt", twins_data2, 2024))
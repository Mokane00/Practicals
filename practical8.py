#a) student_results Function

def student_results(subjects, marks):
    """
    Print subject marks and pass/fail status for each subject.
    
    Parameters:
    subjects (list): List of subject names.
    marks (list): List of corresponding marks for each subject.

    Returns:
    int: Number of subjects passed.
    """
    passed_subjects = 0
    for subject, mark in zip(subjects, marks):
        status = "Pass" if mark >= 50 else "Fail"
        print(f"{subject} {mark} {status}")
        if status == "Pass":
            passed_subjects += 1
    print(f"{passed_subjects} subject(s) passed out of {len(subjects)}")
    return passed_subjects

# Example usage:
student_results(["Maths", "Bio", "Chem"], [45, 52, 65])



#b) convert_currency Function

def convert_currency(values, exchange_rate):
    """
    Convert values into another currency based on exchange rate.

    Parameters:
    values (list): List of values to be converted.
    exchange_rate (float): Exchange rate for conversion.

    Returns:
    list: List of converted values rounded to 2 decimal places.
    """
    converted_values = [round(value * exchange_rate, 2) for value in values]
    return converted_values

# Example usage:
original_values = [100, 200, 300]
exchange_rate = 0.75
converted_values = convert_currency(original_values, exchange_rate)
print(converted_values)


#c) Triangular Numbers List Comprehension


import random

random_numbers = random.sample(range(1, 200), 50)
triangular_numbers = [num for num in random_numbers if (8 * num + 1) % 2 == 1 and (8 * num + 1) ** 0.5 % 1 == 0]
print(triangular_numbers)


#a) Determine if Last Element of Tuple is Even

def last_element_is_even(t):
    """
    Check if the last element of a tuple is even.

    Parameters:
    t (tuple): Input tuple.

    Returns:
    bool: True if last element is even, False otherwise.
    """
    return t[-1] % 2 == 0

# Example usage:
tuple1 = (1, 2, 3, 4, 5)
print(last_element_is_even(tuple1))  # Output: True


#b) Name and Best Mark Function


def best_mark(t):
    """
    Get the name and best mark from a tuple of name followed by marks.

    Parameters:
    t (tuple): Tuple containing name followed by marks.

    Returns:
    tuple: Tuple with name and best mark.
    """
    name = t[0]
    marks = t[1:]
    best_mark = max(marks)
    return (name, best_mark)

# Example usage:
student_tuple = ("Senkatana", 90, 85, 77)
print(best_mark(student_tuple))  # Output: ('Senkatana', 90)


#a) Sum of Positive Integers in Input Line


input_line = input("Enter input line of the form number1+number2: ")
numbers = input_line.split('+')
sum_numbers = sum(int(num) for num in numbers)
print("Sum:", sum_numbers)



#b) String Indexing and Slicing


q = "Paqama ke o qoqele moqoqo o qabolang"
print(q[12:21])  # qoba ebola
print(q[4:15])   # lebo oa qabola
print(q[7:19])   # ke qoqa le molemo

# Capitalize for grammatical correctness
print(q[12].upper() + q[13:21])  # Qoba Ebola
print(q[4].upper() + q[5:15])    # Lebo oa Qabola
print(q[7].upper() + q[8:19])    # Ke Qoqa le Molemo


#c) Word Length Adjustment Function

def adjust_word_length(word, length):
    """
    Adjust the length of a word based on the required length.

    Parameters:
    word (str): Input word.
    length (int): Required length.

    Returns:
    str: Adjusted word.
    """
    if len(word) == length:
        return word
    elif len(word) > length:
        return word[:length]
    else:
        return word + '*' * (length - len(word))

# Example usage:
print(adjust_word_length("Python", 10))  # Output: Python****
print(adjust_word_length("Hello", 3))    # Output: Hel



#d) License Plate Style Determination Program


plate = input("Enter characters for license plate: ")

if len(plate) == 5 and plate[0].isalpha() and plate[1:].isnumeric():
    print("Valid for older style license plate.")
elif len(plate) == 8 and plate[:5].isalpha() and plate[5:].isupper():
    print("Valid for newer style license plate.")
else:
    print("Not valid for either style of license plate.")


#a) Dictionary of Cubic Numbers


cubic_dict = {num: num ** 3 for num in range(1, 11)}
print(cubic_dict)


#a) Dictionary of Cubic Numbers


cubic_dict = {num: num ** 3 for num in range(1, 11)}
print(cubic_dict)


#b) Print Names and Contacts


def print_contacts(names, contacts_dict):
    """
    Print names and corresponding contact numbers.

    Parameters:
    names (list): List of names.
    contacts_dict (dict): Dictionary of contacts.

    """
    for name in names:
        if name in contacts_dict:
            print(f"{name} can be contacted at {contacts_dict[name]}")
        else:
            print(f"{name} cannot be called")

# Example usage:
names_list = ["Limo", "Senkatana"]
contacts = {"Limo": 62123456, "Thabo": 65432178}
print_contacts(names_list, contacts)





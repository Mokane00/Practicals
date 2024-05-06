def txt_from_file(file_name):
    """
    Read text from a file and return it as a string.

    Parameters:
    file_name (str): Name of the file to read.

    Returns:
    str: Text read from the file.
    """
    try:
        with open(file_name, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
      
      
def extract_student_num(text):
    """
    Extract the student number from a string.

    Parameters:
    text (str): Input text containing student number.

    Returns:
    str: Extracted student number.
    """
    student_num = ''.join(filter(str.isdigit, text))
    if len(student_num) != 9:
        print("Error: Student number not found or incorrect format.")
        return None
    return student_num
  
def single_dig_generator(num):
    """
    Generate a single digit from a positive number.

    Parameters:
    num (int): Positive number.

    Returns:
    int: Single digit.
    """
    if num < 10:
        return num
    else:
        digits_sum = sum(int(digit) for digit in str(num))
        return single_dig_generator(digits_sum)
      
def district(num):
    """
    Map a number to a district using a dictionary.

    Parameters:
    num (int): Number representing a district.

    Returns:
    str: District name.
    """
    district_mapping = {
        1: "Maseru",
        2: "Butha-Buthe",
        3: "Leribe",
        4: "Berea",
        5: "Mokhotlong",
        6: "Thaba-Tseka",
        7: "Qacha's Nek",
        8: "Mafeteng",
        9: "Mohale's Hoek",
       10: "Quthing"
    }
    return district_mapping.get(num, "Unknown District")


def main():
    profile_text = txt_from_file("profile.txt")
    if profile_text:
        student_num = extract_student_num(profile_text)
        if student_num:
            district_num = single_dig_generator(int(student_num))
            district_name = district(district_num)
            print(student_num, "is team", district_name)


print(main())             
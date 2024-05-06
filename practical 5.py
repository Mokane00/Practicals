lucky_number = int(input("Enter your lucky number: "))

if lucky_number == 13:
    print("The number 13 is also known as the 'Angel number' in some cultures and symbolize leading with love and compassion like Morena Moshoeshoe did!")
else:
    print(f"Your lucky number is {lucky_number}")
    
positive_number = int(input("Enter a positive number: "))

if positive_number < 10:
    for _ in range(positive_number):
        print("I will master my Python programming skills")
else:
    print(f"I am too confident to repeat the same thing {positive_number} times")
    
# Part C - Algorithm Implementation
believe_in_rights = input("Do you believe in gay rights? (yes/no): ")

if believe_in_rights.lower() == 'yes':
    print("We’re hopeful that your actions are in alignment!")
else:
    assume_exclusion = input("Did you assume gay rights excluded the broad LGBTQI community? (yes/no): ")
    if assume_exclusion.lower() == 'yes':
        print("We apologize for the misunderstanding, all rights matter!")
    else:
        print("My, oh my! We hope you’re open to learning and unlearning.")
        
def age_comment(age):
    if age < 18:
        return "You are too young to make a decision on this matter."
    elif 18 <= age < 30:
        return "You are in a crucial age to shape your opinions and beliefs."
    elif 30 <= age < 50:
        return "You have experienced enough to form informed opinions."
    else:
        return "Your wisdom is valuable in understanding complex issues."

# Example usage:
user_age = int(input("Enter your age: "))
print(age_comment(user_age))                
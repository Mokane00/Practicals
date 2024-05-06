# Define the holidays dictionary
holidays = {
    "March 11": "Moshoeshoe’s Day - This is a day we commemorate Morena Moshoeshoe for his legacy of peace. Coincidentally, he passed away on this day.",
    "October 4": "Independence Day - This day marks our attainment of sovereignty to fully embody the ideals of ‘seMoshoshoe’."
}

# Prompt the user for input
month = input("Enter the month (e.g. March): ")
day = input("Enter the day (e.g. 11): ")

# Check if the entered date is a holiday or not
entered_date = f"{month} {day}"
if entered_date in holidays:
    print(holidays[entered_date])
else:
    print(f"{entered_date} - This day, or indeed any other, presents an opportune moment to contemplate what actions Morena Moshoeshoe would undertake in order to promote the values of peace and love.")
    
    
# a) Positive integers less than 200 which are even and divisible by 5
for num in range(200):
    if num % 2 == 0 and num % 5 == 0:
        print(num)

# b) Count the number 4 in any given list
list1 = [1, 2, 3, 4, 5, 4, 6, 4, 7]
count_4 = list1.count(4)
print(f"Number of 4s in the list: {count_4}")

# c) Sum of numbers in a list less than a certain threshold
given_list = [10, 20, 30, 40, 50, 60]
threshold = 40
sum_below_threshold = sum(num for num in given_list if num < threshold)
print(f"Sum of numbers below {threshold} in the list: {sum_below_threshold}")

# d) Generate a list of numbers divisible by 7 and multiple of 20 between 1500 and 2700
divisible_by_7_and_20 = [num for num in range(1500, 2701) if num % 7 == 0 and num % 20 == 0]
print("Numbers divisible by 7 and multiple of 20 between 1500 and 2700:")
print(divisible_by_7_and_20)

# e) Generate all verses of "99 Bottles of Beer" song
for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more!")


def evaluate_threat(threat):
    if "threatening" in threat and "bigger than you" in threat:
        return "Flee"
    elif "weaker" in threat:
        if "sick" in threat:
            return "Leave it alone"
        elif any(keyword in threat for keyword in ["quills", "poison", "fangs", "razor claws"]):
            return "Back up and go in the other direction"
        elif "smells nice" in threat and "metal jaws" in threat:
            return "Walk on by"
    return "Assess situation"

# Example usage:
threat_description = "threatening and bigger than you"
action = evaluate_threat(threat_description)
print(f"Action to take: {action}")    
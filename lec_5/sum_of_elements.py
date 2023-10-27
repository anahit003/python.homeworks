def sum_of_elements(numbers, exclude_negative=False):
    total = 0
    for number in numbers:
        if not exclude_negative or (exclude_negative and number >= 0):
            total += number
    return total

user_input = input(" list  ")
numbers = [int(num) for num in user_input.split()]

exclude_negative_input = input("negative numbers (yes / no): ").strip().lower()
exclude_negative = exclude_negative_input == "yes"

result = sum_of_elements(numbers, exclude_negative)

print("Sum  (excluding negatives:", exclude_negative, "):", result)

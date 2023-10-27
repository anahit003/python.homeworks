# zuyg kenti cucak
def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers

user_input = input("list: ")
numbers = [int(num) for num in user_input.split()]

even_numbers, odd_numbers = classify_numbers(numbers)

print("Even :", even_numbers)
print("Odd:", odd_numbers)
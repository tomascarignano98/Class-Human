import random
import string

print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))

# Let's generate a password
print("".join(random.choices(string.ascii_letters + string.digits, k=6)))

# Shuffle an array
numbers = [1, 2, 4, 5]
random.shuffle(numbers)
print(numbers)

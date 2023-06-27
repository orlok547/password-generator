import random
import string

def generate_password(length):
	characters = string.ascii_letters + string.digits + string.punctuation
	forbidden_characters = ["\"", "'", "`", "´", "[", "]", "{", "}", "(", ")", ",", ";", ".", ":", "~", "¬", "^", "¨", "ç", "ª", "º"]
	valid_characters = [char for char in characters if char not in forbidden_characters]
	password = ''.join(random.choice(valid_characters) for _ in range(length))
	return password

# Specify the desired password length
while True:
	password_length = int(input("Specify a password length (min 8 - max 25): "))
	if password_length < 8:
		print("Number must be greater than 8.")
	elif password_length > 25:
		print("Number can't be greater than 25.")
	else:
		break

# Generate the password
password = generate_password(password_length)
print(password)
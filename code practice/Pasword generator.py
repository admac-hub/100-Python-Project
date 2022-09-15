import random
import string

total = string.ascii_letters + string.digits + string.punctuation


password_length = 16

password = "".join(random.sample(total, password_length))

print(f"your password is : {password}")
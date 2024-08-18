import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passwords = {}

def generate_password(len_password):
    password = ""
    for _ in range(len_password):
        password += random.choice(chars)
    return password

for i in passwords:
    print(f"{i}: {passwords[i]}")
else:
    print("Ваш менеджер паролей пуст")

while True:
    app = input("\nНазвание приложения, для которого вам нужен пароль: ")
    len_password = int(input("Длина пароля: "))

    passwords[app] = generate_password(len_password)

    for i in passwords:
        print(f"{i}: {passwords[i]}")

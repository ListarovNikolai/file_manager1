import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    # Пример использования
    password_length = 15
    random_password = generate_random_password(password_length)
    print("Сгенерированный пароль:", random_password)

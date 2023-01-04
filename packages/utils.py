from hashlib import sha256


def hide_the_pass(password_plain, login):
    password_hash = sha256(password_plain.encode()).hexdigest()
    password_with_salt = password_hash + login
    return sha256(password_with_salt.encode()).hexdigest()

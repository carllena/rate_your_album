from hashlib import sha256, md5


def hide_the_pass(password_plain, login):
    password_hash = sha256(password_plain.encode()).hexdigest()
    password_with_salt = password_hash + login
    return sha256(password_with_salt.encode()).hexdigest()


def check_fingerprint(login, user_agent, timestamp, fingerprint):
    string = f"{login},{user_agent},{timestamp}"
    if md5(string.encode()).hexdigest() == fingerprint:
        return True
    else:
        return False

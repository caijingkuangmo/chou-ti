def get_random_str(user):
    import hashlib, time
    ctime = str(time.time())

    md5 = hashlib.md5(bytes(user, encoding="utf8"))
    md5.update(bytes(ctime, encoding="utf8"))

    return md5.hexdigest()

def get_random_str2():
    import uuid
    # return uuid.uuid1()
    return uuid.uuid4().__str__()
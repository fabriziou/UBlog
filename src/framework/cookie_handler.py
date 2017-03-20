from hashlib import sha256

SECRET = "c52a080297afefc1d4bf781951eb6735b6496c3af379e4b46d6b941a993f20ed"


def hash_value(value):
    """ Hash value with SECRET key

        :param value:
            String to hash
        :returns:
            String of sha256(SECRET + value)
    """
    return sha256(SECRET + value).hexdigest()


def create_cookie(name, value, path="Path=/"):
    """ Create a cookie and return it

        The valid of the cookie is hashed

        :param name:
            Name of the cookie
        :param value:
            Value of the cookie
        :param path:
            Path where cookie is sent
        :returns:
            Cookie string
    """
    value = str(value)
    hashed_value = hash_value(value)
    content = "%s|%s" % (hashed_value, value)

    return "%s=%s; %s" % (name, content, path)


def read_cookie(content):
    """ Read a cookie and return its value

        None is returned, if the cookie is invalid (hashed value not valid)

        :param content:
            Content of the cookie
        :returns:
            If cookie is valid, we return its value
            Otherwise, we return None
    """
    separator_pos = content.find("|")
    hashed_value = content[:separator_pos]
    value = content[separator_pos + 1:]

    # Check if cookie is valid
    if (hash_value(value) == hashed_value):
        return value

    return None

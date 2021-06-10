from sqlalchemy import TypeDecorator, String
from string import ascii_letters, digits

class StubError(ValueError):
    pass

class HashError(ValueError):
    pass

def validate_stub(stub, strip=False):
    """A function that takes an input stub, validates it and will 
    return an acceptable output stub (or throw an error). If strip, will
    remove all prohibited values and return the validated stub. If not strip,
    will raise ValueError.
    Allowed characters are letters, digits, underscore and hyphen or parentheses.
    Spaces are cast to underscores.
    Case insensitive, stub returned is cast to lowercase"""
    ALLOWED = ascii_letters+digits+'()_-'
    stub = stub.replace(" ","_")
    try:
        output = ''
        for c in tuple(stub):
            if c not in ALLOWED:
                if not strip:
                    raise StubError(f"Invalid Stub. Invalid Character {c}")
                continue
            output += c
        return output.lower()
    except Exception as e:
        raise StubError("Error occured processing stub") from e

class Stub(TypeDecorator):
    impl = String
    cache_ok=False
    def process_bind_param(self, value, dialect):
        return validate_stub(value)
    def compare_against_backend(self, _, conn_type):
        return isinstance(conn_type, String)

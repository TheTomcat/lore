from typing import Type
from sqlalchemy import TypeDecorator, String, Integer

class StubError(ValueError):
    pass

class HashError(ValueError):
    pass

def validate_stub(stub, strip=False):
    """A function that takes an input stub, validates it and will 
    return an acceptable output stub (or throw an error). If strip, will
    remove all prohibited values and return the validated stub. If not strip,
    will raise ValueError.
    Allowed characters are letters, digits, underscore and hyphen.
    Case insensitive."""

    PROHIBITED = '!"#$%&\'()*+,./:;<=>?@[\\]^`{|}~' + '\t\n\r\x0b\x0c'
    # string.punctuation (without - or _)
    stub = stub.replace(" ","_")
    if strip:
        for c in PROHIBITED:
            stub = stub.replace(c,"")
        return stub.lower()
    else:
        if any([c in stub for c in PROHIBITED]):
            raise StubError("Invalid Stub. Invalid characters.")
        return stub.lower()

class Stub(TypeDecorator):
    impl = String
    def process_bind_param(self, value, dialect):
        return validate_stub(value)
    def compare_against_backend(self, _, conn_type):
        return isinstance(conn_type, String)
    
# class TUID(TypeDecorator):
#     impl = Integer
#     def __init__(self, *args, **kwargs):
#         # if "salt" not in kwargs:
#         #     kwargs['salt'] = "not at all secure"
#         self.hashid = hashids.Hashids("not secure")
#         super().__init__(*args, **kwargs)

#     def process_bind_param(self, value, dialect):
#         return self.hashid.encode(value)
#     def process_result_value(self, value, dialect):
#         return self.hashid.decode(value)[0]

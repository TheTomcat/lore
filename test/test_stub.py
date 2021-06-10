from lore.stub import validate_stub, StubError
import unittest
from string import ascii_letters, digits

class StubTest(unittest.TestCase):
    def test_case_sensitivity(self):
        """Test that two stubs with different cases are equal"""
        inpt = "thisISaStub"
        outpt = 'thisisastub'
        self.assertEqual(validate_stub(inpt), outpt)
        self.assertEqual(validate_stub(inpt.lower()), outpt)
    
    def test_space_to_underscore(self):
        'Test that spaces are changed to underscores'
        inpt = 'this is a test'
        outpt = 'this_is_a_test'
        self.assertEqual(validate_stub(inpt), outpt)

    def test_invalid_characters(self):
        """Test that invalid characters are not allowed"""
        inpt = "***"
        self.assertRaises(StubError, validate_stub, inpt)

    def test_stripping_of_invalid_characters(self):
        "Test that passing strip=True supresses errors"
        inpt = "asdf-asdf (asdf)**"
        outpt = 'asdf-asdf_(asdf)'
        self.assertEqual(validate_stub(inpt, strip=True), outpt)
    
    def test_all_allowed_characters(self):
        "Test all allowed characters"
        inpt = ascii_letters + digits + '()-_'
        outpt = inpt.lower()
        self.assertEqual(validate_stub(inpt), outpt)

if __name__ == "__main__":
    unittest.main()
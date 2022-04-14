import os
from dotenv import load_dotenv

def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def test_capitalize_string():
    load_dotenv()
    assert os.environ["XRAY_USERNAME"] == 'Test'

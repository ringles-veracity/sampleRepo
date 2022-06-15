import os
from dotenv import load_dotenv

def test_main():
    load_dotenv()
    print(os.environ["DATABRICKS_VAULT_URL"])
    print(os.environ["DATABRICKS_URL"])
    print(os.environ["TEST_BRANCH"])
    print(os.environ["TEST_SET"])
    assert 'Test' == 'Test'

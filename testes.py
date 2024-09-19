from unittest import *
from unittest.mock import patch

@patch('projeto.get_input', lambda _: 'filme 1') # <- value to be returned by input method
def test_should_be_the_correct_value(self):
    print("teste")
   # assert value == 'film'

if __name__ == "__main__":
    unittest.main()
import unittest
import function

class TestLeadingSubstrings(unittest.TestCase):
    def test_leading_substrings(self):
        """Test the leading_substrings function."""
        inputted = 'bear'
        output_expected = ['b', 'be', 'bea', 'bear']
        self.assertEqual(output_expected, function.leading_substrings(inputted), "The function is not working.")        

if __name__ == '__main__':
    unittest.main()
    

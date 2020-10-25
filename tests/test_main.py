from os import access
from ..main import get_largest_word, transpose_word, execute
import unittest, sys
from io import StringIO
from unittest.mock import patch

class TestMain(unittest.TestCase):
    
    # Positive scenarios
    def test_get_largest_word(self):
        actual = get_largest_word('files/wordlist.txt')
        expected = 'abcde'

        self.assertEqual(expected, actual)

    def test_transpose_word(self):
        actual = transpose_word('nawjif')
        expected = 'fijwan'

        self.assertEqual(expected, actual)

    def test_execute(self):
        sys.argv = ['main.py', 'files/wordlist.txt']
        with patch('sys.stdout', new=StringIO()) as output:
            execute()
        
        actual = output.getvalue().strip()
        expected = 'abcde\nedcba'
        self.assertEqual(expected, actual)

    def test_get_largest_word_with_int_list(self):
        actual = get_largest_word('files/integerlist.txt')
        expected = '78645'

        self.assertEqual(expected, actual)

    # Handled after adding thid test
    def test_transpose_word_with_int(self):
         with self.assertRaises(Exception):
            transpose_word(123)

    def test_execute_with_int_list(self):
        sys.argv = ['main.py', 'files/integerlist.txt']
        with patch('sys.stdout', new=StringIO()) as output:
            execute()
        
        actual = output.getvalue().strip()
        expected = '78645\n54687'
        self.assertEqual(expected, actual)

    def test_get_largest_word_with_float_list(self):
        actual = get_largest_word('files/floatlist.txt')
        expected = '0.004554'

        self.assertEqual(expected, actual)

    def test_transpose_word_with_float(self):
         with self.assertRaises(Exception):
            transpose_word(123.45)

    def test_execute_with_float_list(self):
        sys.argv = ['main.py', 'files/floatlist.txt']
        with patch('sys.stdout', new=StringIO()) as output:
            execute()
        
        actual = output.getvalue().strip()
        expected = '0.004554\n455400.0'
        self.assertEqual(expected, actual)

    def test_get_largest_word_with_escapeseq_list(self):
        actual = get_largest_word('files/escapeseqlist.txt')
        expected = '\\xhh...\tASCII character with hex value hh...'

        self.assertEqual(expected, actual)

    def test_transpose_word_with_escapeseq(self):
        actual = transpose_word('\t\n...\r')
        expected = '\r...\n\t'

        self.assertEqual(expected, actual)            

    def test_execute_with_escapeseq_list(self):
        sys.argv = ['main.py', 'files/escapeseqlist.txt']
        with patch('sys.stdout', new=StringIO()) as output:
            execute()
        
        actual = output.getvalue().strip()
        expected = '\\xhh...\tASCII character with hex value hh...\n...hh eulav xeh htiw retcarahc IICSA\t...hhx\\'
        self.assertEqual(expected, actual)

    def test_get_largest_word_with_nonenglish_list(self):
        actual = get_largest_word('files/nonenglishlist.txt')
        expected = 'Ich möchte Teil von geheimen Arbeiten sein'

        self.assertEqual(expected, actual)

    def test_transpose_word_with_nonenglish(self):
        actual = transpose_word('証券会社の一員になりたい')
        expected = 'いたりなに員一の社会券証'

        self.assertEqual(expected, actual)            

    def test_execute_with_nonenglish_list(self):
        sys.argv = ['main.py', 'files/nonenglishlist.txt']
        with patch('sys.stdout', new=StringIO()) as output:
            execute()
        
        actual = output.getvalue().strip()
        expected = 'Ich möchte Teil von geheimen Arbeiten sein\nnies netiebrA nemieheg nov lieT ethcöm hcI'
        self.assertEqual(expected, actual)

    # Negative Scenarios
    # Handled after adding this test
    def test_get_largest_word_with_empty_file(self):
        actual = get_largest_word('files/emptylist.txt')
        expected = None
        self.assertEqual(expected, actual)

    # Handled after adding this test
    def test_get_largest_word_with_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            get_largest_word('files/empty.txt')

    def test_execute_raise_exception_on_invalid_filepath(self):
        sys.argv = ['main.py', 'test_data.txt']
        with self.assertRaises(IndexError):
            execute()

    def test_execute_raise_exception_on_invalid_arg(self):
        sys.argv = ['main.py']
        with self.assertRaises(IndexError):
            execute()

    def test_get_largest_with_duplicate_words(self):
        actual = get_largest_word('files/duplicatelist.txt')
        expected = "Superior"

        self.assertEqual(expected, actual)

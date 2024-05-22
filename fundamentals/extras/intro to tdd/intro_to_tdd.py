import unittest

def reverseList(list):
    new_list = [list[x] for x in range(len(list)-1,-1,-1)]
    return new_list
def isPalindrome(input_string):
    new_string = ""
    for i in range(len(input_string)-1,-1,-1):
        new_string += input_string[i]
    if(input_string == new_string):
        print(f"{input_string} is palindrom")
    else:
        print(f"{input_string} is not palindrom")
    return new_string
def isPalindrome_True(input_string):
    new_string = ""
    for i in range(len(input_string)-1,-1,-1):
        new_string += input_string[i]
    if(input_string == new_string):
        return True
    else:
        return False
class Tests(unittest.TestCase) :
    
    def test_reverseList_equal_range_10(self):
        list_reveres = [i for i in range(10)]
        list_reveres.reverse()
        self.assertEqual(reverseList([i for i in range(10)]),list_reveres)
    def test_reverseList_equal_range_5(self):
        list_reveres = [i for i in range(5)]
        list_reveres.reverse()
        self.assertEqual(reverseList([i for i in range(5)]),list_reveres)
    def test_reverseList_equal_range_100(self):
        list_reveres = [i for i in range(100)]
        list_reveres.reverse()
        self.assertEqual(reverseList([i for i in range(100)]),list_reveres)
    def test_isPalindrome_equal(self):
        test_string = "racecar"
        self.assertEqual(isPalindrome(test_string),test_string)
    def test_isPalindrome_True(self):
        test_string = "racecar"
        self.assertTrue(isPalindrome(test_string))
    # def test_reverseList_True(self):
    #     list_reveres = [i for i in range(10)]
    #     list_reveres.reverse()
    #     self.assertTrue(reverseList([i for i in range(10)]) == list_reveres)
    # def test_reverseList_notequal(self):
    #     self.assertNotEqual(reverseList([i for i in range(10)]),[i for i in range(10)])

if __name__ == '__main__':
    unittest.main() 


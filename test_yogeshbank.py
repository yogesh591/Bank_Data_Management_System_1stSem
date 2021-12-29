import unittest
import yogeshbank
from tkinter import *
rootval= Tk()
a=hi.SMS(rootval)
class Test_hi(unittest.TestCase):
    def test_search(self):
        array_test = [('1', 'Ram', 'Khadka', '32', 'Dillibazaar', 'Computing'),
                      ('2', 'Shyam', 'Khadka', '32', 'Patan', 'Computing')]
        ex_result = [('2', 'Shyam', 'Khadka', '32', 'Patan', 'Computing')]
        a.entrysearch.delete(0, 'end')
        a.searchbyCB.set('FirstName')
        a.entrysearch.insert(0, 'Shyam')
        ac_result = a.search_item(array_test)
        print("search test")
        print(ac_result)
        self.assertEqual(ex_result, ac_result)

if __name__=='__main__':
    unittest.main()
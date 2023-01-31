import unittest
import importlib.util

class TestCases(unittest.TestCase):
    def import_module_from_file(self, file_path):
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    '''
    array/
    '''
    def test_two_sum(self):
        two_sum_module = self.import_module_from_file("./array/1_two_sum.py")
        s = two_sum_module.Solution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [1, 0])
        self.assertEqual(s.twoSum([3, 2, 4], 6), [2, 1])
        self.assertEqual(s.twoSum([3, 3], 6), [1, 0])
    
    def test_valid_parentheses(self):
        valid_parentheses = self.import_module_from_file("./array/20_valid_parentheses.py")
        s = valid_parentheses.Solution()
        self.assertEqual(s.isValid("()"), True)
        self.assertEqual(s.isValid("()[]{}"), True)
        self.assertEqual(s.isValid("(]"), False)

    '''
    hash_table/
    '''
    def test_first_missing_positive(self):
        first_missing_positive = self.import_module_from_file("./hash_table/41_first_missing_positive.py")
        s = first_missing_positive.Solution()
        self.assertEqual(s.firstMissingPositive([1,2,0]), 3)
        self.assertEqual(s.firstMissingPositive([3,4,-1,1]), 2)
        self.assertEqual(s.firstMissingPositive([7,8,9,11,12]), 1)        
    
    def test_insert_delete_getrandom(self):
        insert_delete_getrandom = self.import_module_from_file("./hash_table/380_insert_delete_getrandom_o1.py")
        s = insert_delete_getrandom.RandomizedSet()
        self.assertTrue(s.insert(1))
        self.assertFalse(s.remove(2))
        self.assertTrue(s.insert(2))
        self.assertIn(s.getRandom(), [1, 2])
        self.assertTrue(s.remove(1))
        self.assertFalse(s.insert(2))
        self.assertEqual(s.getRandom(), 2)

    def test_canConstruct(self):
        can_construct = self.import_module_from_file("./hash_table/383_ransom_note.py")
        s = can_construct.Solution()
        self.assertFalse(s.canConstruct("a","b"))
        self.assertFalse(s.canConstruct("aa","ab"))
        self.assertTrue(s.canConstruct("aa","aab"))

    '''
    linked_list/
    '''
    def test_lru_cache(self):
        pass

    def test_reverse_linked_list(self):
        pass

    '''
    matrix/
    '''
    def test_valid_sudoku(self):
        pass


    '''
    not_in_grind/
    '''
    def test_queue_using_stacks(self):
        pass

if __name__ == '__main__':
    unittest.main()

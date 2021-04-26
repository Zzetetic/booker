import unittest
from booker.lib import calculate_pages


class Test_case_1(unittest.TestCase):

	def test_1(self):
		list_blocks_right = [
		[
		   { 'left_page' : 1,
		     'right_page': 4
		   },
		   { 'left_page' : 2,
		     'right_page': 3
		   }
		 ],
		 [
		   { 'left_page' : 5,
		     'right_page': 8
		   },
		   { 'left_page' : 6,
		     'right_page': 7
		   }
		 ],
		  [
		   { 'left_page' : 9,
		     'right_page': None
		   },
		   { 'left_page' : 10,
		     'right_page': None
		   }
		 ]
		]

		list_blocks_from_function = calculate_pages(10, 1)
		
		self.assertEqual(list_blocks_right, list_blocks_from_function)


if __name__ == '__main__':
    unittest.main() 

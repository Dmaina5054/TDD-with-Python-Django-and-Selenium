from selenium import webdriver
import unittest
# browser = webdriver.Firefox()


# #user go to homepage to checkout app
# browser.get('http://localhost:8000')

# #notice the page title and header mention todo list

# assert 'To-Do' in browser.title
# #invited to enter a to do list
# #type "Buy fancy leather jacket"
# #press enter and show list view
# #1. buy a fancy leather jacket
# #still another text box available to add more items
# #types "Attend Men conference"
# #page updates now two items in list
# #satisfied go to sleep

# browser.quit()

#ADOPT standard unitests python module
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox() 
    def tearDown(self):
        self.browser.quit()
    def badmath(self):
        self.assertEqual(1+1,5)
    #this is logic to test
    def test_can_start_a_list_and_retreive_later(self):
        #User check out new heard todolist app-Homepage
        self.browser.get('http://localhost:8000')
        
        #user notices page title and header with to-do list
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')
    
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
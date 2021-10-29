from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

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
#for our function
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox() 
    def tearDown(self):
        self.browser.quit()

    #this is logic to test
    def test_can_start_a_list_and_retreive_later(self):
        #User check out new heard todolist app-Homepage
        self.browser.get('http://localhost:8000')
        
        #user notices page title and header with to-do list
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text 
        self.assertIn('To-Do',header_text)
        
        #she is prompted to enter a to-d0 item in a textbox
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder','Enter a to-do item')      
        )
        
        #she types "buy a leather jacket"
        inputbox.send_keys('buy leather jacker')
        
        self.fail('Finish the test')
        #when she presses enter, page updates and ne list show
        inputbox.send_keys(keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: buy a leather jacket' for row in rows)
        )
        #there is still a text box inviting her to add an entry
        self.fail('Finish the test!')
        
        #page updates and now has a list of elements
        [...]
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')

from selenium import webdriver
browser = webdriver.Firefox()


#user go to homepage to checkout app
browser.get('http://localhost:8000')

#notice the page title and header mention todo list

assert 'To-Do' in browser.title
#invited to enter a to do list
#type "Buy fancy leather jacket"
#press enter and show list view
#1. buy a fancy leather jacket
#still another text box available to add more items
#types "Attend Men conference"
#page updates now two items in list
#satisfied go to sleep

browser.quit()
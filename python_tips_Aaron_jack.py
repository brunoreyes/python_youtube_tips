# Run functions on the terminal: -i main.py
# 	• Allows me to call functions within a terminal shell
# 	• And gives me access to all functions and variables



import pdb
pdb.set_trace()
	
Add(1, 'two')



# Dependency management sharing is done by virtual environtments:
	Virtualenv venv NameOfFolderEnvIsIn
	
	Source venv/bin/activate
	
	Pip install selenium
	
	Now selenium is installed within the folder


# List comprehension
fruits = [ { 'fruit': 'apple', 'price': '20'},  { 'fruit': 'banana', 'price': '10'} ]

# Print all fruits with a name that starts with a
print([fruit['name'] for fruit in fruits if fruits if fruit['name'][0] == 'a'])

# dictionaries
print({fruit['name']: fruit['price'] for fruit in fruits}
# Setting.    key     &   value      created by looking at each item: fruit

# Lambda Function (a function using different syntax)

# reg function
def add(x,y):
    return x + y


# lambda function
add2 = lambda x,y: x + y





# Problem 1: Lambda functions
sale_price = 29.99
# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2 
# Call the lambda function
print(add_tax(sale_price))


# Problem 2: Register user by validation it's name, email and password
def validate_user(name, email, password):
    '''
    validate_user function will take three parameters: name(str), email(str), password(str).
    '''
    def validate_name(name):
        if type(name) == str:
            return True
        else:
            raise ValueError('Please use str in this function, values other than strings are not allowed.')

    def validate_email(email):
        if type(email) == str and '@' in email and '.' in email[email.index('@'):]:
            return True
        else:
            raise ValueError('Invalid email format. Please provide a valid email.')

    def validate_password(password):
        if type(password) == str and len(password) >= 8:
            return True
        else:
            raise ValueError('Please use str & int and minimum length is 8 characters in this function, values other than strings and integers are not allowed.')

    validate_name(name)
    validate_email(email)
    validate_password(password)
    
    return True

def register_user(name, email, password):
    user = {}
    if validate_user(name, email, password) == True:
        user['name'] = name
        user['email'] = email
        user['password'] = password
        return user
    
register_user('ali', 'alisageneda@gmail.com', 'password123')

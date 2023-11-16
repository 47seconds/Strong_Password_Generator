import secrets
import string

# Defining our characterset.
# In a password, we should have: lowercases, uppercases, numbers, special characters, and password should be of minimum length of 8.

lower_case          = string.ascii_lowercase
upper_case          = string.ascii_uppercase
numbers             = string.digits
special_characters  = string.punctuation

# Now merge these all strings to make a big string that contains all:
MASTER_STRING = lower_case + upper_case + numbers + special_characters

# Defining our generate function:
def GeneratePassword(password_length):
    
    # Password length should be greater than 8
    if password_length < 8:
        print("The desired password length is too short.\nRetry with length greater than or equal to 8.")
        exit()
    
    # Defined our final password string
    PASSWORD = ""
    
    # Concatanation of PASSWORD string with secrets.choice to randomly generate a string of length greater than 8
    for i in range(password_length):
        PASSWORD = "".join([PASSWORD, secrets.choice(MASTER_STRING)])

    return PASSWORD

length_of_password = int(input("Enter the Length of password you want in digits: "))

PASSWORD = GeneratePassword(length_of_password)

print("Generated Password: ", PASSWORD)
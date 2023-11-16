import secrets
import string


# Defining our generate function:
def GeneratePassword(password_length, MASTER_STRING):
       
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

def requirements(is_lower_case, is_upper_case, is_numbers, is_special_characters):
    
    # Defining our characterset.
    # In a password, we can have: lowercases, uppercases, numbers, and special characters.
    lower_case          = string.ascii_lowercase
    upper_case          = string.ascii_uppercase
    numbers             = string.digits
    special_characters  = string.punctuation
    
    # Now we make a master string which will have character set according to user's need, for now its empty:
    MASTER_STRING = ""
    
    # Now according to users requirement, we make MASTER_STRING:    
    if (is_lower_case == "yes") | (is_lower_case == "Yes") | (is_lower_case == "YES") | (is_lower_case == "y") | (is_lower_case == "Y"):
        MASTER_STRING = "".join([MASTER_STRING, lower_case])
    
    if (is_upper_case == "yes") | (is_upper_case == "Yes") | (is_upper_case == "YES") | (is_upper_case == "y") | (is_upper_case == "Y"):
        MASTER_STRING = "".join([MASTER_STRING, upper_case])
    
    if (is_numbers == "yes") | (is_numbers == "Yes") | (is_numbers == "YES") | (is_numbers == "y") | (is_numbers == "Y"):
        MASTER_STRING = "".join([MASTER_STRING, numbers])
    
    if (is_special_characters == "yes") | (is_special_characters == "Yes") | (is_special_characters == "YES") | (is_special_characters == "y") | (is_special_characters == "Y"):
        MASTER_STRING = "".join([MASTER_STRING, special_characters])
    
    # If user don't selects any of the character set for the password
    if (MASTER_STRING == ""):
        print("You need to have atleast 1 character set in your password.\nRetry with selecting atleast one character set.")
        exit()
    
    # We have successfully generated our master string
    return MASTER_STRING

# Asking for length of password to generated
length_of_password    = int(input("Enter the Length of password you want in digits: "))

# Asking for character set to be used in generating password
is_lower_case         = input("Do you want lower cased alphabets in your password? ")
is_upper_case         = input("Do you want upper cased alphabets in your password? ")
is_numbers            = input("Do you want numbers in your password? ")
is_special_characters = input("Do you want special characters in your password? ")

# Generating Master string for password generation
MASTER_STRING = requirements(is_lower_case, is_upper_case, is_numbers, is_special_characters)

# Password Generated
PASSWORD = GeneratePassword(length_of_password, MASTER_STRING)
print("Generated Password: ", PASSWORD)
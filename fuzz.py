import scanner
import random
import string
def fuzz():
    try:
        # Fuzz for valid password
        scanner.isValidPasswordName(generate_random_alphanumeric_string(100))
        print("Test 1 Passed")
    except:
        print("Test 1 failed")

    try:
        # Fuzz for valid username
        scanner.isValidUserName(generate_random_alphanumeric_string(100))
        print("Test 2 Passed")
    except:
        print("Test 2 failed")

    try:
        # Fuzz for valid key
        scanner.isValidKey(generate_random_alphanumeric_string(100))
        print("Test 3 Passed")
    except:
        print("Test 3 failed")   

    try:
        # Fuzz for grabbing YAML files
        scanner.getYAMLFiles(1)
        print("Test 4 Passed")
    except:
        print("Test 4 Failed")  

    try:
        # Fuzz for valid secret
        scanner.checkIfValidSecret(generate_random_alphanumeric_string(100))
        print("Test 5 Passed")
    except:
        print("Test 5 failed") 


def generate_random_alphanumeric_string(length):
    # Create a pool of alphanumeric characters
    alphanumeric_pool = string.ascii_letters + string.digits

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(alphanumeric_pool) for _ in range(length))

    return random_string

if __name__ == '__main__':
    fuzz()

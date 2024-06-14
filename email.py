import re

print('''

 *    ----------------------------------$$\-$$\-----------------$$\---------------------------$$\---------------------------
 *    ----------------------------------\__|$$-|----------------$$-|--------------------------$$-|--------------------------
 *    -$$$$$$\--$$$$$$\$$$$\---$$$$$$\--$$\-$$-|-------$$$$$$$\-$$$$$$$\---$$$$$$\---$$$$$$$\-$$-|--$$\--$$$$$$\---$$$$$$\--
 *    $$--__$$\-$$--_$$--_$$\--\____$$\-$$-|$$-|------$$--_____|$$--__$$\-$$--__$$\-$$--_____|$$-|-$$--|$$--__$$\-$$--__$$\-
 *    $$$$$$$$-|$$-/-$$-/-$$-|-$$$$$$$-|$$-|$$-|------$$-/------$$-|--$$-|$$$$$$$$-|$$-/------$$$$$$--/-$$$$$$$$-|$$-|--\__|
 *    $$---____|$$-|-$$-|-$$-|$$--__$$-|$$-|$$-|------$$-|------$$-|--$$-|$$---____|$$-|------$$--_$$<--$$---____|$$-|------
 *    \$$$$$$$\-$$-|-$$-|-$$-|\$$$$$$$-|$$-|$$-|------\$$$$$$$\-$$-|--$$-|\$$$$$$$\-\$$$$$$$\-$$-|-\$$\-\$$$$$$$\-$$-|------
 *    -\_______|\__|-\__|-\__|-\_______|\__|\__|-------\_______|\__|--\__|-\_______|-\_______|\__|--\__|-\_______|\__|------
 *    ----------------------------------------------------------------------------------------------------------------------
 *    ----------------------------------------------------------------------------------------------------------------------
 *    ----------------------------------------------------------------------------------------------------------------------
 *
''')

def is_valid_email(email):
    """
    Validate an email address based on Google's guidelines.
    Args:
    email (str): The email address to validate.
    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    # Define the regex for the local part
    local_part_regex = (
        r'^[a-zA-Z0-9._%+-]+'
    )
    domain_part_regex = (
        r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    try:
        local_part, domain_part = email.rsplit('@', 1)
    except ValueError:
        return False
    
    # Check if the local part is valid
    if not re.match(local_part_regex, local_part):
        return False
    
    # Check if the domain part is valid
    if not re.match(domain_part_regex, domain_part):
        return False
    
    # Check the length of each part
    if len(local_part) > 64 or len(domain_part) > 255:
        return False
    
    # Additional check: local part cannot have consecutive dots
    if '..' in local_part:
        return False
    
    # Additional check: local part cannot start or end with a dot
    if local_part[0] == '.' or local_part[-1] == '.':
        return False
    
    return True

def main():
    """
    Main function to interact with the user and validate email addresses.
    """
    print("Email Validation Checker")
    print("Enter 'exit' to quit the program.\n")

    while True:
        email = input("Please enter an email address to validate: ").strip()
        
        if email.lower() == 'exit':
            print("Exiting the Email Validation Checker. Goodbye!")
            break
        
        if is_valid_email(email):
            print(f"'{email}' is a valid email address.\n")
        else:
            print(f"'{email}' is not a valid email address.\n")

if __name__ == "__main__":
    main()

# Email_validation_cml.py
# Email Validation Checker

This is a simple Python script designed to validate email addresses based on Google's guidelines. The script checks various criteria to ensure the validity of an email address and provides user interaction through the console.

## Features

- **Validation Criteria**:
  - Ensures the email contains exactly one '@' symbol.
  - Validates the local part (before '@') for allowed characters using a regular expression.
  - Validates the domain part (after '@') for allowed characters and structure using a regular expression.
  - Checks that the local part is no longer than 64 characters.
  - Checks that the domain part is no longer than 255 characters.
  - Ensures no consecutive dots in the local part.
  - Ensures the local part does not start or end with a dot.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding standards.

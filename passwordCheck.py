def check_password(password: str):
    # Open 'passwords.txt' in read mode
    with open('passwords.txt', 'r') as file:
        # Read all lines into a list of strings, each representing a common password
        common_passwords = file.read().splitlines()

    # Loop through each common password with an index, starting at 1
    for i, common_password in enumerate(common_passwords, start=1):
        # Check if the user's password matches any common password
        if password == common_password:
            print(f'{password}: Common password found❌ (# {i})')
            return # Exit the function if a match is found

    # If no match is found, print that the password is unique
    print(f'{password}: Unique password✅')

# Main function to prompt for the password
def main():
    user_password = input('Enter a password: ')
    
    # Check if input is empty
    if not user_password:
        print("Error: Please enter a valid password.")
        return # Exit the function without further processing

    check_password(user_password)

# Run the main function only if the script is executed directly
if __name__ == '__main__':
    main()

import zipfile

def is_zip_encrypted(zipFilePath):
    try:
        with zipfile.ZipFile(zipFilePath, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if zip_info.flag_bits & 0x1:
                    return True
            return False
    except zipfile.BadZipFile:
        return False


def main():
    # Get the target file path from the user in folderpath variable
    folderpath = input('Path to the file: ')
    folderpath = folderpath.strip()

    # Checks if the file is password encrypted
    if (not is_zip_encrypted(folderpath)):
        # Notifies if the zipped file/folder is not password encrypted
        print('The zipped file/folder is not password protected! You can successfully open it!')

    # Else:
    else:
        # Initialize a variable result with zero. '0' will indicate Failure, while '1' will indicate Success
        result = 0  
        # Initialize a variable attempts to keep the count of passwords tried
        attempts = 0  

        # Uncomment to build a character array including all numbers,lowercase letter, uppercase letters and special characters. Total 10+26+26+33 = 95 characters
        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_', '&', ';', '"', '?', '`', "'", '\\']

        print("Brute Force Started...")

        # Check if result is 0  
        if (result == 0):
            # Print Checking for 4 character password...
            print("Checking for 4 character password...")
            # Loop through each character in characters to create loop for 4th position
            for i in characters:
                # Create an inner loop to loop through characters to create loop for 3rd position
                for j in characters:
                    # Create an inner loop to loop through characters to create loop for 2nd position
                    for k in characters:
                        # Create an inner loop to loop through characters to create loop for 1st position
                        for l in characters:
                            # Concatenate characters from the array to make a 4 character password combination and store it in variable guess
                            guess = str(i) + str(j) + str(k) + str(l)
                            # Encodes the password combination and store it back in guess
                            guess = guess.encode('utf8').strip()
                            # Increment the attempts by 1
                            attempts += 1
                            # Add try block
                            try:
                                # Access the zipfile in folderpath in read mode
                                with zipfile.ZipFile(folderpath, 'r') as zf:
                                    # Use extractall() method on zipfile and pass guess string as pwd 
                                    zf.extractall(pwd=guess)
                                    # Decode the guess string
                                    guess = guess.decode('utf8').strip()
                                    # Set result variable to 1 on success
                                    result = 1 
                                    # Break the loop as correct guess is found 
                                    break  
                            # Except block    
                            except:
                                # Pass the loop iteration
                                pass
                        # If the password is found break from j for loop   
                        if result == 1:
                            break 
                    # If the password is found break from k for loop
                    if result == 1:
                        break  
                # If the password is found break from l for loop
                if result == 1:
                    break  

        # Finally, if the password is not found even after applying all possible combination of characters upto 4 character length, notify the user as below, else print congratulations
        if (result == 0):
            message = f"Sorry, password not found. A total of {attempts} possible combinations tried. Password is not of 4 characters."
            print(message)

        else:
            message = f"Congratulations!!! Password found after trying {attempts} combinations.\nThe password is {guess}."
            print(message)

main()

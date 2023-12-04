# -------------------
# Install PyPDF2 library using below command
# pip3 install 'PyPDF2<3.0'

# Dictionary Attack
# --------------------

import PyPDF2 as pd


def main():
    # Get the target file path from the user and use strip() method and store it in filename variable
    filename = input('Path to the file: ')
    filename = filename.strip()
    # Call open() function and pass it filename and 'rb', store result in file variable
    file = open(filename, 'rb')
    # Call pd.pdfFilereader(file) to read pdf and store it in pdfReader variable
    pdfReader = pd.PdfFileReader(file)

    attempts = 0

    # Add if condition to checks if the file is password encrypted
    if not pdfReader.isEncrypted:
        # Print 'The file is not password protected! You can successfully open it!'
        print('The file is not password protected! You can successfully open it!')
    # Else:
    else:
        # Use open() function to read wordlist.txt and store result in wordListFile
        wordListFile = open('wordlist.txt', 'r', errors='ignore')
        # USe read() and lower() method on wordListFile to convert each character to lowercase and store result in body variable
        body = wordListFile.read().lower()
        # Use split('\n') method on body to get words and store the list in words variable
        words = body.split('\n')

        # loop through each index in words list
        for i in range(len(words)):
            # get words[i] in word
            word = words[i]
            # Print f'Trying to decode password by: {word}'
            print(f'Trying to decode password by: {word}')
           
            # Use pdfReader.decrypt(word) to get the result
            result = pdfReader.decrypt(word)
            # Check if result is 1
            if result == 1:
                # Print f"Congratulations!!! The password is {word}."
                print(f"Congratulations!!! The password is {word}.")
                # break the loop
                break

            # Else check if result is 0
            elif result == 0:
                # Increment attempts variable by 1
                attempts += 1
                # Print f'Passwords attempts: {str(attempts)}'
                print(f'Passwords attempts: {str(attempts)}')
                # Continue to next iteration of the loop
                continue

main()

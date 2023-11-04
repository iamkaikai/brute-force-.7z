import py7zr
import itertools

# Ask the user for the path to the .7z file
archive_path = input('Enter the path to the .7z file: ')
digit_length = input('Enter the length of the password digits: ')

# This will generate all combinations of 4 digits ranging from 0000 to 9999
passwords = itertools.product('0123456789', repeat=int(digit_length))

# Attempt to open the archive with each password
for password_tuple in passwords:
    password = ''.join(password_tuple)
    print(f'trying password: {password}')
    try:
        with py7zr.SevenZipFile(archive_path, mode='r', password=password) as z:
            z.extractall()
        print(f'Success! The password is {password}')
        break
   
    except FileNotFoundError:
        print(f"The file at {archive_path} was not found. Please check the path and try again.")
        break
   
    except Exception as e:
        if str(e) == 'Corrupt input data':
            continue
        print(f'An unexpected error occurred: {e}')
        break
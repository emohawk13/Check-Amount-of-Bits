def convert_size(size_bytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    for suffix in suffixes:
        if size_bytes < 1024.0:
            return "%3.1f %s" % (size_bytes, suffix)
        size_bytes /= 1024.0

def get_menu():
    while True:
        print("Menu:")
        print('1. Convert One Number')
        print('2. Subtract Two Numbers')
        print('3. Add Two Numbers')
        print('0. To exit the applictaion.')
        choice = input("Enter a choice to continue: ")

        if choice == '1':
            single_number()
        elif choice == '2':
            sub_numbers()
        elif choice == '3':
            add_numbers()
        elif choice == '4':
            print("Exiting...")
            break

def single_number():
    file_size_bytes = int(input("Enter the file size in bytes: "))
    file_size_str = convert_size(file_size_bytes)
    print("File size:", file_size_str)

def sub_numbers():
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))
    total = num1 - num2
    convert = convert_size(total)
    print('File size: ', convert)

def add_numbers():
    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))
    total = num1 + num2
    convert = convert_size(total)
    print('File size: ', convert)

if __name__ == "__main__":
    get_menu()

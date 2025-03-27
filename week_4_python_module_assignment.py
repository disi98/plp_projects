# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_write_file(original_file, new_file):
    try:
        with open(original_file, 'r') as file:
            data = file.read()
            print(data)
            with open(new_file, 'w') as new_file:
                new_file.write(data)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You don't have permission to access this file.")
    except Exception as e:
        print("An error occurred.")
        print(e)





def main():
    original_file = input("Enter the name of the file to read: ")
    new_file = input("Enter the name of the file to write: ")
    read_write_file(original_file, new_file)


if __name__ == "__main__":
    main()
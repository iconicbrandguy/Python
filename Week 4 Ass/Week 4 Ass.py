with  open("myInput.text", "r") as file:
    content = file.read()
    print(content)

upperCase = content.upper()

with open("output.txt", "w") as file:
    file.write(upperCase)

def read_file():
    filename = input("Enter the file filename you want to read")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"En unexpected error occurred: {e}")

# Run the function
read_file()
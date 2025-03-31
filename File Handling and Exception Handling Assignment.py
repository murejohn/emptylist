ef modify_file_content(input_filename, output_filename):
    try:
        # Open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (example: make it uppercase and add a line)
        modified_content = content.upper() + "\nModified by Grok!"
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Success! Modified content written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}' or write to '{output_filename}'.")
    except IOError:
        print("Error: An I/O error occurred while handling the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Get filename from user
input_filename = input("Enter the name of the file to read: ")
output_filename = "modified_" + input_filename  # Creates a new filename

# Call the function with user input
modify_file_content(input_filename, output_filename)
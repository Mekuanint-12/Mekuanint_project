def modify_file_content(content):
    """
      managing files efficiently in Python, 
      ensuring error-free code that gracefully handles unexpected issues.
      Mastering files and exception handling
    """
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        # Add line number and convert to uppercase
        modified_line = f"{i}: {line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def main():
    print("=== File Modifier Program ===")
    print("This program reads a file, modifies its content,")
    print("and writes the modified version to a new file.\n")
    
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        print(f"Successfully read {input_filename}")
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Get output filename from user
        output_filename = input("Enter the name for the new modified file: ")
        
        # Write to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Successfully created modified file: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'. It may be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
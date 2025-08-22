def read_and_write_modified():
    try:
        filename = input("Enter the filename to read: ")
        
        # Try to open the input file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Example modification: convert all text to uppercase
        modified_lines = [line.upper() for line in lines]
        
        # Specify the output filename
        output_filename = "modified_" + filename
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        
        print(f"File '{filename}' has been read and modified content saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except IOError:
        print(f"Error: Cannot read from or write to file '{filename}'. Please check your permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_write_modified()

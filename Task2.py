# Step 1: Write user input to a file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Append additional data to the same file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)

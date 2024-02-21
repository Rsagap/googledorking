# Path to the file from which even lines will be removed
file_path = 'googledorks'

# Read the file and store lines in a list, skipping even lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Filter out even lines (keeping odd lines)
odd_lines = [line for index, line in enumerate(lines, start=1) if index % 2 != 0]

# Write the odd lines back to the file, effectively removing even lines
with open(file_path, 'w') as file:
    file.writelines(odd_lines)

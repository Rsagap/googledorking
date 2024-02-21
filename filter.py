import re

# Define the regular expression pattern to find content within the specified part
pattern = r'<a href="[^"]*">(.*?)<\/a>'

# Open the text file and read its contents
with open('GHDb.html', 'r') as file:
    content = file.read()

    # Find all matches of the pattern in the content
    matches = re.findall(pattern, content)

    # Print the matches
    for match in matches:
        print(match)


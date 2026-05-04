text = "  hello world python  "

print("Original String:", text)

# Remove spaces
print("After strip():", text.strip())

# Convert case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())

# Replace words
print("After replace():", text.replace("world", "Python"))

# Split string
print("After split():", text.split())

# Find substring
print("Index of 'world':", text.find("world"))

# Count occurrences
print("Count of 'o':", text.count("o"))

# Check start and end
print("Starts with 'hello':", text.strip().startswith("hello"))
print("Ends with 'python':", text.strip().endswith("python"))
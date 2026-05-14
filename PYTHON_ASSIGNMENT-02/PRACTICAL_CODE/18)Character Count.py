# Input string
text = "python"

# Count characters
count = {}

for i in text:
    count[i] = text.count(i)

print(count)
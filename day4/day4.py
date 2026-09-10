# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'

concatenated_string = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

str5 = 'Coding'
str6 = 'For'
str7 = 'All'

concatenated_string2 = str5 + ' ' + str6 + ' ' + str7

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.

cut_string = company[7:]  # Slicing from index 7 to the end

print(cut_string)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.find("Coding"))  # Returns the index of the first occurrence of "Coding"

# Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding', 'Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
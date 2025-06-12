#day 4

    #1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
str5 = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4
print(str5)
    #2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str1="coding"
str2="for"
str3="all"
str4 = str1 + ' ' + str2 + ' ' + str3
print(str4)
    #3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
    #4. Print the variable company using _print()_.
print(company)
    #5. Print the length of the company string using _len()_ method and print it.
print(len(company))
    #6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())
    #7. Change all the characters to lowercase letters using _lower()_ method.
print(company.lower())
    #8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print(company.capitalize())
print(company.title())
print(company.swapcase())
    #9. Cut(slice) out the first word of _Coding For All_ string.
first_word = company[0:6]
print(first_word)
    #10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))  
print(company.index("Coding")) 
    #11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
    #12. Change Python for Everyone to Python for All using the replace method or other methods.
str2 = "Python for Everyone"
print(str2.replace("Everyone", "All"))
    #13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
    #14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))
    #15. What is the character at index 0 in the string _Coding For All_.
print(company[0])
    #16. What is the last index of the string _Coding For All_.
print(company[-1])  # Last character
    #17. What character is at index 10 in _Coding For All_.
print(company[10])  
    #18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = ''.join(word[0].upper() for word in str2.split())
print(acronym)  # Output: PFE
    #19. Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_cfa = ''.join(word[0].upper() for word in company.split())
print(acronym_cfa)  # Output: CFA
    #20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))  # Output: 0
    #21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))  # Output: 7
    #22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))  # Output: 15
    #23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))  # Output: 30
    #24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))  # Output: 38
    #25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find('because')
end_index = sentence.rindex('because') + len('because')
sliced_phrase = sentence[start_index:end_index]
print(sliced_phrase)  # Output: because because because
    #26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = sentence.find('because')
print(first_occurrence)  # Output: 30
    #27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[first_occurrence:first_occurrence + len('because because because')]
print(sliced_phrase)  # Output: because because because
    #28. Does '\'Coding For All' start with a substring _Coding_?
print(company.startswith('Coding'))  # Output: True
    #29. Does 'Coding For All' end with a substring _coding_?
print(company.endswith('coding'))  # Output: False
    #30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
trailing_spaces = '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
cleaned_string = trailing_spaces.strip()
print(cleaned_string)  # Output: '&nbsp;&nbsp; Coding For All'
    #31. Which one of the following variables return True when we use the method isidentifier():   
        #    - thirty_days_of_python
    #32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)  # Output: Django # Flask # Bottle # Pyramid # Falcon
    #33. Use the new line escape sequence to separate the following sentences.
sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sentences)  
    #34. Use a tab escape sequence to write the following lines.
tabbed_lines = "Name\tAge\tCountry\nJohn\t25\tUSA\nAlice\t30\tCanada"
print(tabbed_lines)
    #35. Use the string formatting method to display the following:
radius= 10
area = 3.14 * radius ** 2
formatted_string = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(formatted_string)  # Output: The area of a circle with radius 10 is 314.0 meters square.
    #36. Make the following using string formatting methods:
a = 8
b = 6 
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("%d %% %d = %d" % (a, b, a % b))  # Note: %% escapes the percent symbol
print("%d // %d = %d" % (a, b, a // b))
print("%d ** %d = %d" % (a, b, a ** b)) 
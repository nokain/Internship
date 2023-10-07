DS2309


#Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Sample Text- 'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:

def replace_chars_with_colon(input_string):
    
    replaced_string = input_string.replace(' ', ':').replace(',', ':').replace('.', ':')
    return replaced_string

sample_text = 'Python Exercises, PHP exercises.'

result = replace_chars_with_colon(sample_text)
print(result)


# In[2]:


#Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.

import re

def find_words_starting_with_a_or_e(input_string):
    
    pattern = r'\b[aeAE]\w+\b'

    matching_words = re.findall(pattern, input_string)

    return matching_words

sample_text = "An apple and an elephant are in the garden."

result = find_words_starting_with_a_or_e(sample_text)
print(result)


# In[22]:


#Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

import re

def find_words_at_least_4_chars(input_string):
   
    pattern = re.compile(r'\b\w{4,}\b')

    matching_words = pattern.findall(input_string)

    return matching_words

sample_text = "How are you doing this morning."

result = find_words_at_least_4_chars(sample_text)
print(result)


# In[21]:


#Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

import re

def find_words_with_specific_lengths(input_string):
    
    pattern = re.compile(r'\b\w{3,5}\b')

    matching_words = pattern.findall(input_string)

    return matching_words

sample_text = "This is the table we have been looking for."

result = find_words_with_specific_lengths(sample_text)
print(result)


# In[25]:


#Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output:
#example.com
#hr@fliprobo.com
#github.com
#Hello Data Science World
#Data Scientist



import re

def remove_parentheses(strings_list):
 
    pattern = re.compile(r'[()]')

    cleaned_strings = [pattern.sub('', s) for s in strings_list]

    return cleaned_strings

sample_list = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

result = remove_parentheses(sample_list)
print(result)


# In[45]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.


import re

def remove_parentheses_area(strings_list):
    
    pattern = re.compile(r'\([^)]*\)')

    modified_strings = [pattern.sub('', string) for string in strings_list]

    return modified_strings

sample_list = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

modified_list = remove_parentheses_area(sample_list)

for item in modified_list:
    print(item)


# In[46]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

import re

def split_string_into_uppercase(text):
   
    result = re.findall('[A-Z][a-z]*', text)
    return result

sample_text = "ImportanceOfRegularExpressionsInPython"

result = split_string_into_uppercase(sample_text)
print(result)


# In[47]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re

def insert_spaces_between_words_with_numbers(text):
    
    result = re.sub(r'([0-9])([A-Z])', r'\1 \2', text)
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result = insert_spaces_between_words_with_numbers(sample_text)
print(result)


# In[48]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

import re

def insert_spaces_between_words_with_capitals_or_numbers(text):
    
    result = re.sub(r'([A-Z0-9])([A-Z])', r'\1 \2', text)
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result = insert_spaces_between_words_with_capitals_or_numbers(sample_text)
print(result)


# In[60]:


#Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

#Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.
#Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. 
#Please contact us at hr@fliprobo.com for further information. 
#Expected Output: 
#['xyz@domain.com', 'xyz.abc@sdomain.domain.com']
#['hr@fliprobo.com']

Note- Store given sample text in the text file and then extract email addresses.


import re

def extract_email_addresses(text):

    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    email_addresses = re.findall(pattern, text)

    return email_addresses

sample_text = "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. Please contact us at hr@fliprobo.com for further information."

extracted_emails = extract_email_addresses(sample_text)

for email in extracted_emails:
    print(email)


# In[63]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

def is_valid_string(s):
  
    pattern = r'^[a-zA-Z0-9_]+$'

    match = re.match(pattern, s)

    return match is not None

test_strings = ["Hello6838", "Good_evening", "My_String123!", "12345", "_underscore_", ""]

for test_string in test_strings:
    if is_valid_string(test_string):
        print(f"'{test_string}' is a valid string.")
    else:
        print(f"'{test_string}' is not a valid string.")


# In[65]:


#Question 12- Write a Python program where a string will start with a specific number. 

def starts_with_number(string, number):
 
    return string.startswith(str(number))

# Test cases
test_strings = ["12345abc", "56789xyz", "abc12345", "999abc"]

specific_number = 12345  
for test_string in test_strings:
    if starts_with_number(test_string, specific_number):
        print(f"'{test_string}' starts with the number {specific_number}.")
    else:
        print(f"'{test_string}' does not start with the number {specific_number}.")


# In[66]:


#Question 13- Write a Python program to remove leading zeros from an IP address

def remove_leading_zeros(ip_address):
   
    octets = ip_address.split(".")

    cleaned_octets = [str(int(octet)) for octet in octets]

    cleaned_ip = ".".join(cleaned_octets)

    return cleaned_ip

ip_address = "192.001.002.003"

cleaned_ip = remove_leading_zeros(ip_address)

print(f"Original IP address: {ip_address}")
print(f"Cleaned IP address: {cleaned_ip}")


# In[71]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947
#Note- Store given sample text in the text file and then extract the date string asked format.

import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b'

dates = re.findall(pattern, text)

for date in dates:
    print(date)


# In[73]:


#Question 15- Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

def search_words(text, words):
    found_words = []
    for word in words:
        if word in text:
            found_words.append(word)
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_words = ['fox', 'dog', 'horse']

found_words = search_words(sample_text, searched_words)

if found_words:
    print("Found words:", found_words)
else:
    print("No words found.")


# In[75]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'

def search_and_find_location(text, pattern):
    found_locations = []
    start = 0

    while start < len(text):
        index = text.find(pattern, start)
        if index == -1:
            break
        found_locations.append(index)
        start = index + 1

    return found_locations

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_word = 'fox'

found_locations = search_and_find_location(sample_text, searched_word)

if found_locations:
    print(f"'{searched_word}' found at positions:", found_locations)
else:
    print(f"'{searched_word}' not found in the text.")


# In[77]:


#Question 17- Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.

def find_substrings(text, pattern):
    found_positions = []
    start = 0

    while start < len(text):
        index = text.find(pattern, start)
        if index == -1:
            break
        found_positions.append(index)
        start = index + 1

    return found_positions

sample_text = 'Python exercises, PHP exercises, C# exercises'

pattern = 'exercises'

found_positions = find_substrings(sample_text, pattern)

if found_positions:
    print(f"'{pattern}' found at positions:", found_positions)
else:
    print(f"'{pattern}' not found in the text.")


# In[79]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

def find_occurrences_and_positions(text, pattern):
    occurrences = []
    positions = []
    start = 0

    while start < len(text):
        index = text.find(pattern, start)
        if index == -1:
            break
        occurrences.append(pattern)
        positions.append(index)
        start = index + 1

    return occurrences, positions


sample_text = 'Python exercises, PHP exercises, C# exercises, Python exercises'

pattern = 'exercises'

found_occurrences, found_positions = find_occurrences_and_positions(sample_text, pattern)

if found_occurrences:
    print(f"'{pattern}' found {len(found_occurrences)} times at positions:", found_positions)
else:
    print(f"'{pattern}' not found in the text.")


# In[81]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

from datetime import datetime

def convert_date_format(input_date):
    try:
      
        date_obj = datetime.strptime(input_date, '%Y-%m-%d')

        formatted_date = date_obj.strftime('%d-%m-%Y')

        return formatted_date
    except ValueError:
        return "Invalid date format"

input_date = "2023-10-01"

formatted_date = convert_date_format(input_date)

print(f"Original date: {input_date}")
print(f"Converted date: {formatted_date}")


# In[83]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
#Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
#Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']


import re

def find_decimal_numbers(text):
    
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')

    decimal_numbers = pattern.findall(text)

    return decimal_numbers

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

found_numbers = find_decimal_numbers(sample_text)

print(found_numbers)



# In[3]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

import re

def separate_and_print_numbers(text):
    
    pattern = re.compile(r'\b\d+\b')
    
    matches = pattern.finditer(text)

    for match in matches:
        number = match.group()
        start_position = match.start()
        end_position = match.end()
        print(f"Number: {number}, Start Position: {start_position}, End Position: {end_position}")

sample_text = "I bought my car $3500. The quantity is 10."

separate_and_print_numbers(sample_text)


# In[4]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950

import re

def extract_maximum_numeric_value(text):

    pattern = r'\b\d+\b'

    numeric_values = [int(match) for match in re.findall(pattern, text)]

    if numeric_values:
        maximum_value = max(numeric_values)
        return maximum_value
    else:
        return None

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

maximum_value = extract_maximum_numeric_value(sample_text)

if maximum_value is not None:
    print(f"Maximum numeric value: {maximum_value}")
else:
    print("No numeric values found in the text.")



# In[5]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python

import re

def insert_spaces_between_capital_words(text):
   
    pattern = r'([A-Z][a-z]*)'

    formatted_text = re.sub(pattern, r' \1', text)

    if formatted_text.startswith(' '):
        formatted_text = formatted_text[1:]

    return formatted_text

sample_text = "RegularExpressionIsAnImportantTopicInPython"

formatted_text = insert_spaces_between_capital_words(sample_text)

print(formatted_text)


# In[7]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

import re

# Sample text
sample_text = "I bought My house Yesterday."

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, sample_text)

print(matches)


# In[8]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world


import re

def remove_continuous_duplicates(sentence):
    
    pattern = r'\b(\w+)(?:\s+\1)+\b'

    cleaned_sentence = re.sub(pattern, r'\1', sentence)

    return cleaned_sentence

sample_text = "Hello hello world world"

cleaned_text = remove_continuous_duplicates(sample_text)

print(cleaned_text)


# In[9]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

import re

def ends_with_alphanumeric(input_string):

    pattern = r'^.*[a-zA-Z0-9]$'

    if re.match(pattern, input_string):
        return True
    else:
        return False

input_string = "Morning"

result = ends_with_alphanumeric(input_string)

if result:
    print(f"The string '{input_string}' ends with an alphanumeric character.")
else:
    print(f"The string '{input_string}' does not end with an alphanumeric character.")


# In[10]:


#Question 27-Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

import re

def extract_hashtags(text):
    
    pattern = r'#\w+'
    
    hashtags = re.findall(pattern, text)

    return hashtags

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = extract_hashtags(sample_text)

print(hashtags)



# In[11]:


#Question 28- Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

import re

def remove_unicode_symbols(text):

    pattern = r'<U\+[0-9A-Fa-f]+>'

    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

cleaned_text = remove_unicode_symbols(sample_text)

print(cleaned_text)


# In[14]:


#Question 29- Write a python program to extract dates from the text stored in the text file.
#Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
#Note- Store this sample text in the file and then extract dates.

import re

def extract_dates(text):
    
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'

    dates = re.findall(pattern, text)

    return dates

sample_text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."

extracted_dates = extract_dates(sample_text)

print(extracted_dates)



# In[15]:


#Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

import re

def remove_words_between_lengths(text):
    try:
       
        pattern = re.compile(r'\b\w{2,4}\b')

        cleaned_text = pattern.sub('', text)
        
        cleaned_text = ' '.join(cleaned_text.split())

        return cleaned_text
    except TypeError:
        return ""

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

cleaned_text = remove_words_between_lengths(sample_text)

print(cleaned_text)


# In[ ]:





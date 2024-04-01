"""
Task 1: Advanced Data Extraction
Problem Statement:
    - Develop a script to extract specific information from a formatted text. The text contains data entries delimited by semicolons and formatted as 'Key: Value'. Extract the value corresponding to a specific key.
        - Successfully extract the 'Occupation' value from the text.
        - Implement a regex pattern that accurately targets and captures the desired data.
"""
import re
text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

text_pattern = r"Name: (.*?); Age: (.*?); Occupation: (.*?); Location: (.*?)$"
find_occupation = re.findall(text_pattern, text)
occupation = find_occupation[0][2]
print(f"Occupation: {occupation}")


"""
Task 2: URL Validator
Problem Statement:
    - Write a Python program to validate a list of URLs. A valid URL should start with 'http://' or 'https://', followed by a domain name.
    
Expected Outcome:
    - Correctly identify and categorize valid and invalid URLs from the list.
    - Use regex to validate the format of each URL.    
"""


def validate_url(url):
    url_pattern = r"(http://)|(https://)(\w)+\.[A-Za-z]{2,}"
    if re.match(url_pattern, url):
        return True
    else:
        return False


def process_urls(url_list):
    valid_urls = []
    invalid_urls = []
    for url in url_list:
        try:
            if validate_url(url):
                valid_urls.append(url)
            else:
                invalid_urls.append(url)
        except Exception as e:
            print(f"Error processing url {url}: {e}")
    return valid_urls, invalid_urls


# Sample url list
urls = ["https://example.com", "www.example.com", "http://test.com"]
valid, invalid = process_urls(urls)
print("Valid Urls:", valid)
print("Invalid Urls:", invalid)


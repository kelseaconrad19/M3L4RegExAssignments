"""
Task 1: Product Description Keyword Tagging
    - Problem Statement:
        - You have a list of product descriptions. Your task is to tag each product based on keywords in the description. For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.
    - Expected Outcome:
        - Efficiently tag each product with the appropriate category ('Electronics', 'Apparel', 'Home & Kitchen') using regex to identify relevant keywords.
        - Use regex to match specific product-related keywords in each description.
"""
import re


def analyze_description(desc):
    electronics_pattern = r"\b(smartphone|screen|\d+GB)\b"
    apparel_pattern = r"\b(cotton|t-shirt|size)\b"
    home_and_kitchen_pattern = r"\b(kitchen|home|knife)\b"
    try:
        if re.search(electronics_pattern, desc, re.IGNORECASE):
            return "Electronics"
        elif re.search(apparel_pattern, desc, re.IGNORECASE):
            return "Apparel"
        elif re.search(home_and_kitchen_pattern, desc, re.IGNORECASE):
            return "Home and Kitchen"
    except Exception as e:
        print(f"Error analyzing comment: {e}")


descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

for description in descriptions:
    tags = analyze_description(description)
    print(f"Tag: {tags} | Description: {description}")

"""
Task 2: Pricing Format Standardization
    - Problem Statement:
        - You have a string containing various price formats from an international e-commerce site. Standardize all prices to the format 'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.
    - Expected Outcome:
        - Convert all price formats in the string to a standardized 'USD XX.XX' format.
        - Use re.sub() to perform the necessary replacements and format transformations.        
"""

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
price_pattern = r"\$(\d+\.\d{2})|(\d+\.\d{2})\s?USD|(\d+\.\d{2})\$"

correct_format = r"USD \1\2\3"

formatted_price = re.sub(price_pattern, correct_format, price_data)

print(formatted_price)



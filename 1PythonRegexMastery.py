"""
Task 1:
    - You are given a piece of code that is intended to extract email addresses from a given text. However, the code contains errors and does not function as expected. Your task is to identify and correct these errors.
"""
import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)


"""
Task 2:
    - You have a log file represented as a string, containing timestamps and messages. Write a script to reformat the timestamps from 'MM-DD-YYYY' to 'YYYY-MM-DD' and anonymize any usernames mentioned in the log (format: '@username').
    - Expected Outcome:
        - Correctly reformat the date in each log entry.
        - Replace all instances of '@username' with '[ANONYMIZED USER]'.
        - Use re.sub() effectively to achieve the desired text manipulations.
"""


def standardize_dates(log):
    log = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\1-\2", log)
    return log


def anonymize_users(log):
    log = re.sub(r"@[a-zA-Z._%+-]{2,}", '[ANONYMIZED USER]', log)
    return log


def format_log(log_entries):
    try:
        log_entries = standardize_dates(log_entries)
        log_entries = anonymize_users(log_entries)
        return log_entries
    except Exception as e:
        print(f"Error formatting log: {e}")
        return log_entries


log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."

formatted_log = format_log(log_data)
print(formatted_log)


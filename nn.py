import re
import json

# The Regex: Captures (Timestamp) ... (Username) ... (IP)
# \S+ means "any character that isn't a space" (perfect for names and IPs)
log_pattern = re.compile(r'(\w{3}\s+\d+\s\d{2}:\d{2}:\d{2}).*Failed password for (?:invalid user )?(\S+) from (\S+)')

failed_attempts = []

try:
    with open('auth.log', 'r') as f:
        for line in f:
            match = log_pattern.search(line)
            if match:
                # We pull the specific groups from the regex match
                entry = {
                    "timestamp": match.group(1),
                    "username": match.group(2),
                    "ip_address": match.group(3)
                }
                failed_attempts.append(entry)

    # Output results as JSON
    with open('failed_logins.json', 'w') as json_file:
        json.dump(failed_attempts, json_file, indent=4)
        
    print(f"Successfully processed {len(failed_attempts)} failed attempts.")

except FileNotFoundError:
    print("Error: 'auth.log' not found. Please ensure the file exists.")
except PermissionError:
    print("Error: You don't have permission to read this file.")

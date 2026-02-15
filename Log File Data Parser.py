import re

IPpattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

with open('Sample Log File.txt', 'r') as f:
    contents = f.read()

    matches = IPpattern.finditer(contents)

    for match in matches:
        print("The IPs are:" , match.group())
        
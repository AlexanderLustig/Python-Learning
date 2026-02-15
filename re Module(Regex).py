import re

text_to_search = '''
asdkfha[owefefa
ASFAOISDFAN[SREIOF]]
Dave Martin
615-555-7164
173 Main St., Springfield, IL 62704
davemartin@bogusemail.com
05/12/1988

Charles Harris
800-555-5669
969 High St., Atlantis, GA 30301
charlesharris@bogusemail.com
08/30/1975

Maggie Smith
561*555*5843
712 Oak St., Gotham, NY 10001
maggie_smith82@my-work.net
10/01/2002

Mr. Robinson
123.555.1234
444 Sky Ln., Metropolis, DE 19901
robinson.mister@provider.org
12-25-1995

Ms Davis
900-555-7788
1212 Cedar Rd., Star City, WA 98101
davis.ms@university.edu
01.01.2020

Mrs. Robinson
800-555-0000
555 Broadway, New York, NY 10012
mrs_robinson@example.com
11/11/1911

cat
mat
bat
pat
'''

sentence = 'Start a sentence and then bring it to an end'

#print('\tTab')
#print(r'\tTab')

# pattern = re.compile(r'555')
#pattern = re.compile(r'.')
#pattern = re.compile(r'\.')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')
#pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d')
# pattern = re.compile(r'[a-zA-Z]')
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'[^b]at')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')



matches = pattern.finditer(text_to_search)

with open('data45.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

# for match in matches:
#     print(match)

#print(text_to_search[556:559])
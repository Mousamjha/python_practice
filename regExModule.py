import re

text = "I am learning Python, Python is powerful language"
pattern = "Python"
result = re.finditer(pattern, text)
for x, i in enumerate(result):
    pass
    # print(x, i)

# print(result)
impFunctions = [x for x in dir(re) if '__' not in x or '_'not in x]
# print(impFunctions)

data = "I saw dog running behind cat and cat climbed but dog couldn't 30 ft tall TREES"
pattern = re.compile("dog | cat", re.IGNORECASE)
match_iter = re.finditer(pattern, data)
count = 0
for i, match in enumerate(match_iter):
    # print(match)
    # print(f"{i+1} appearance of {match.group()} found, starting from {match.start()} and ends at {match.end()}")
    count = count + 1
# print("Total matches: ", count)

str_pattern = r"[^a-zA-Z ']"
# print(re.findall(str_pattern, data, re.IGNORECASE))

password = "ABCD"#input("Enter Password: ")
pattern_pass = r"[0-9A-Z]"
pass_contain = re.findall(pattern_pass, password)
# print("Entered Password: ", password)
if pass_contain:
    # print("Valid Password")
    pass
else:
    # print("Try strong password")
    pass

data_1 = "I saw dog running behind cat and cat climbed but dog couldn't 30 ft tall TREES"
pattern_1 = r'\bcat\b'
allMatch = re.finditer(pattern_1, data_1)

data_2 = "My birth date is on 1983-08-16"
pattern_2 = r"\d{4}-\d{2}-\d{2}"
match_2 = re.findall(pattern_2, data_2)
# print(match_2)

data3 = "Hello World"
pattern_3 = r'l+'
match_3 = re.findall(pattern_3, data3)
# print(match_3)

data_4 = "My email ids are mousamjha@gmail.com and mousamjha8@gmail.com"
pattern_4 = r'\w+@\w+\.\w+'
match_4 = re.findall(pattern_4, data_4)
print(match_4)

data_5 = "call me at 123-456-7890 or 1234567890"
pattern_5 = r'\d{3}-?\d{3}-?\d{4}'
match_5 = re.findall(pattern_5, data_5)
print(match_5)

urls = ["http://www.abc.com", "https://www.abc.net", "htttp:\\wwww.abc.com"]
url_pattern = r'https?://\w+\.\w+.\w+'
correctUrls = []
for url in urls:
    rightUrl = re.match(url_pattern, url)
    print(rightUrl)
    if rightUrl:
        correctUrls.append(rightUrl.group())
# print(correctUrls)        


emailList = ["abc-123@google.com", "abc.123", "abc.123@hotmail.com", "abc_123", "abc_123@yahoomail"]
def validEmails(emails: list):
    validEmails = []
    rePattern = r"\w+_?\.?\d+?@\w+\.\w+"
    for email in emails:
        matches = re.match(rePattern, email)
        print(matches)
        if matches:
            validEmails.append(matches.group())
    return validEmails

data6 = validEmails(emailList)
print(data6)
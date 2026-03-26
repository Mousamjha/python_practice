# import re

# string = "25-03-01 is the hot summer day, on 2025-08-1 the day was cooler"
# pattern = r"\d+-\d+-\d+"
# date_val = re.findall(pattern=pattern, string=string)
# # print(date_val)


# string2 = "The cat jumped over the lazy dog"
# pattern2 = re.compile("cat|dog", re.IGNORECASE)
# match_iter = re.finditer(pattern2, string2)
# for ele in match_iter:
#     pass
#     # print(f"-:- {ele} -:- {ele.group()} -:- {ele.start()} -:- {ele.end()}")


# string3 = """The string has 999
# and another 333"""
# pattern3 = re.compile(r'\d+$', re.MULTILINE)
# match3 = re.findall(pattern3, string3)
# # print(match3)

# string4 = "color and colour are same"
# pattern4 = re.compile(r'\w{4}u?\w')
# match4 = re.findall(pattern4, string4)
# # print(match4)

# string5 = "call me at 123-456-7890 or 1234567890"
# pattern5 = r'\d+-?\d+-?\d+-?'
# match5 = re.findall(pattern5, string5)
# # print(match5)


# string6 = ['http://www.google.com', 'https://www.google.com', 'htt://wwww.google.com', 'htp://www.google.com']
# pattern6 = r'https?://\w{3}\.\w+\.\w+'
# validUrl = []
# for url in string6:
#     match6 = re.match(pattern6, url)
#     if match6:
#         validUrl.append(match6.group())
# # print(validUrl)        

# string7 = "Mousam: Mobile No = 8981022553 and email-id: mousamjha8@gmail.com"
# pattern7 = r'\d{10}|\w+@\w+\.\w+'
# match7 = re.findall(pattern7, string7)
# # print(match7)


# htmlEle = '<a href="www.google.com">Click Me</a>'
# patt = r'<a href="([^"]+)">[^<]+</a>'
# print(re.findall(patt, htmlEle))



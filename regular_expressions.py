import re

patterns = ['Sridhar', 'blue']
text = 'Hello, my name is Sridhar!!! and the color is blue. Whats you fav color?'

for pattern in patterns:
    print(f"Searching for '{pattern}' in below text: \n {text}")

    if re.search(pattern , text):
        print('Match found')
    else:
        print('No match found')

#search
match = re.search(patterns[0], text) 
print(type(match))
print(match.start())
print(match.end())
print(match.group())
print(match.span())

#split
split = '@'  
text1 = 'my email addresses are blue@gmail.com and red@yahoo.in'
print(re.split(split, text1))

#findall
print(re.findall(split, text1))
print(len(re.findall(split, text1))) #getting the length

#patterns
#repetation syntax
patterns2 = ['az*', 'az+', 'az?', 'az{3}', 'az{3,4}']
text2 = 'azzzzz....azazazaz.....aaaaazzzzz....aaaaaaz'

def repetative_systax(patterns2, text2):
    for pattern2 in patterns2:
        print(f'Searching the text using the pattern: {pattern2}')
        print(re.findall(pattern2, text2),'\n')


repetative_systax(patterns2, text2)

#character sets
patterns3 = ['[az]', 'a[az]', 'a[az]+']
repetative_systax(patterns3, text2)

#exclusion
#carat symbol
print(re.findall('[^!?,. ]+', text))

#character ranges
#we can use a 'dash'(-) 
dash_pattern = ['[a-z]','[A-Z]','[a-zA-Z]','[a-z][A-Z]']
repetative_systax(dash_pattern,text)


text = "My telephone number is 999-666-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print('area code: ', results.group(1))

#pipe operators
print(re.search(r"man|woman","This man was here."))
print(re.search(r"man|woman","This woman was here."))

#wildcard characters
#You can use a simple period .
print(re.findall(r".at","The cat in the hat sat here."))
print(re.findall(r".at","The bat went splat")) #see the difference in single period and mutiple periods
print(re.findall(r"...at","The bat went splat"))

#Starts with and Ends With

print(re.findall(r'\d$','This ends with a number 2')) # Ends with a number

print(re.findall(r'^\d','1 is the loneliest number.')) # Starts with a number

phrase2 = "there are 3 numbers 34 inside 5 this sentence."
print(re.findall(r'[^\d]',phrase2))
print(re.findall(r'[^\d]+',phrase2)) #use + symbol to get the sentence back

hypetext = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print(re.findall(r'[\w]+-[\w]+',hypetext))

#Parenthesis for Multiple Options
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text11 = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)', text11))
print(re.search(r'cat(fish|nap|claw)', texttwo))
print(re.search(r'cat(fish|nap|claw)', textthree))


import re

'''phonenumber=input('Write a phonenumber with the form +xx xxx xx xx xx : \n')
pattern=r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
p=re.compile(pattern)

print(p.match(phonenumber))'''

number=input ('Write a positive or negative number without any spaces : \n')
pattern1=r'-?[1-9][0-9]*'
#pattern2=r'\-\d*'
p1=re.compile(pattern1)
#p2=re.compite(pattern2)

print(p1.match(number))
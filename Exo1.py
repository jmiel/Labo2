phonenumber=input('Write a phonenumber with the form +xx xxx xx xx xx')
pattern=r'\+\d{2} \d{3} \d{2} \d{2} \d{2}'
p=re.compile(pattern)

print(p.match(phonenumber))
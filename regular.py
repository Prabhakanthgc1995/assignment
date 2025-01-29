import re
email_data= "kanth <kanth@gmail.com>, sunil <sunil@gmail.com>"
result= re.search(r"kanth", email_data)
print(result)

result= re.search(r"kan", email_data)
print(result)

result= re.search(r"suni", email_data)
print(result)

result= re.search(r"prabha", email_data)
print(result)

result= re.search(r"kant[a,b]", email_data)
print(result)

result= re.search(r"kan[a-z]{1}", email_data)
print(result)

result= re.search(r"kan[a-z]{2}", email_data)
print(result)


result= re.findall(r"kan[a-z]{2}", email_data)
print(result)

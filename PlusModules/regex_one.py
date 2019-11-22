import re

given_string='indix'
pattern='^i...a$'
verify_match=re.match(pattern,given_string)
print(verify_match)

#[ind] - i -match 
#   id=math 
# inx= 
# ... =  ab none 
#+ 
# ab+c - ab
# ? -= ab?c - nonabc

string='hello....  i am learning 89 python 12 programming'
pattern_search='\d+'
result=re.findall(pattern,string)
print(result)

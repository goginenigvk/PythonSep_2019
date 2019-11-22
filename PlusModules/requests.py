
import requests
req_obj=requests.get('https://api.github.com')
print(req_obj.status_code) 
req_obj.content
req_obj.cookies
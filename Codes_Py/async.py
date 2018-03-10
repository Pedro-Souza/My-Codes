import asyncio
import time

async def helo_word(name: str):
    print('Olá, {}'.format(name))



loop = asyncio.get_event_loop()
tasks = []

start = time.time()
for name in ['pedro', 'souza', 'goku']:
    task = asyncio.ensure_future(helo_word(name))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('Conclusion: {}'.format(end - start))

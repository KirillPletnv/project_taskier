import asyncio
import aiohttp

from aiohttp import ClientSession
import functools

import time
from typing import Callable, Any

def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'Функция {func} завершилась за {total:.4f} c')
        return wrapped
    return wrapper


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return (result.status, url)

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        #url = 'https://www.example.com'
        #status = await fetch_status(session, url)
        #status2 = await fetch_status(session, 'https://www.google.com')
        #status3 = await fetch_status(session, 'https://www.vk.ru')
        urls = ['https://www.example.com', 'https://www.google.com', 'https://www.vk.ru', 'https://derfuhrer.pythonanywhere.com']
        status_codes = [fetch_status(session, url) for url in urls]
        ##status_code = await asyncio.gather(*status_codes)
        for final_task in asyncio.as_completed(status_codes):
            print(await final_task)
        #print(f'Состояние для {urls[0]} было равно {status_codes[0]}')
        #print(f'Состояние для status2 было равно {status_codes[1]}')
        #print(f'Состояние для status3 было равно {status_codes[2]}')



asyncio.run(main())




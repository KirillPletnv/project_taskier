import asyncio
from asyncio import CancelledError
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



async def hello_world_message():
    await asyncio.sleep(3)
    return 'Hello world!'

@async_timed()
async def main():
    are = asyncio.create_task(delay(8))
    are2 = asyncio.create_task(delay(2))
    message = await hello_world_message()
    print(message)
    try:
        result = await asyncio.wait_for(delay(9), timeout=4)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Cancel Task')
    await are
    await are2


@async_timed()
async def delay(delay_seconds: int):
    print(f'Засыпаю на {delay_seconds} секунд')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} секунд окончен')
    return delay_seconds

async def delay_min(delay_seconds: 2):
    print(f'Засыпаю на {delay_seconds} секунд')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} секунд окончен')
    return delay_seconds




asyncio.run(main())
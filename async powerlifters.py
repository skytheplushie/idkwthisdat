import asyncio


async def start_strongman(name, power):
    balls = 1
    print(f'Силач {name} с силой {power} начал соревнования.')
    while balls < 6:
        print(f'Силач {name} поднял мяч с номером {balls}')
        await asyncio.sleep(delay=1)
        balls += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    first_task = asyncio.create_task(start_strongman('Liverpool', 3))
    second_task = asyncio.create_task(start_strongman('Manchester', 4))
    third_task = asyncio.create_task(start_strongman('Doberman', 5))
    await first_task
    await second_task
    await third_task

asyncio.run(start_tournament())
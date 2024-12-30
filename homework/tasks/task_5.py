import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float):
    # Функция принимает на вход корутину, которую необходимо запустить,
    # однако иногда она выполняется
    # слишком долго, это время необходимо
    # ограничить переданным на вход количеством секунд.
    #
    # Тест проверяет, что каждая переданная корутина была запущена, и все они
    # завершились за заданное
    # время.
    #
    try:
        # Ограничиваем время выполнения корутины
        await asyncio.wait_for(coro, timeout=max_execution_time)
    except asyncio.TimeoutError:
        print(f"Корутина выполнялась дольше {max_execution_time} секунд")


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time, но
    # корутин на вход приходит несколько.

    wrapped_coros = [asyncio.wait_for(coro, timeout=max_execution_time) for coro in coros]

    try:
        # Запускаем все корутины параллельно и ждем их завершения или отмены
        await asyncio.gather(*wrapped_coros)
    except asyncio.TimeoutError:
        print(f"Хотя бы одна корутина выполнялаьс {max_execution_time} секунд")

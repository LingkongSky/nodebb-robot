import asyncio
import datetime

from task import tasks


async def inputs(array):

    time_type = array['time_type']
    times = array['time']

    if time_type == 'routine':
        while True:
            await tasks(array)
            await asyncio.sleep(int(times))  #

    elif time_type == 'everyday':

        current_time = datetime.datetime.now().strftime("%H:%M")
        wait_time = calculate_wait_time(times, current_time, 'everyday')
        await asyncio.sleep(wait_time)
        while True:
            await tasks(array)
            await asyncio.sleep(86440)  # 每隔一天执行一次

    elif time_type == 'everymonth':

        current_date = datetime.datetime.now().strftime("%d-%H:%M")
        wait_time = calculate_wait_time(times, current_date, 'everymonth')
        await asyncio.sleep(wait_time)
        while True:
            await tasks(array)
            await asyncio.sleep(2591920)  # 每隔一个月执行一次
    elif time_type == 'once':
        # 获取当前时间 计算目标时间差 睡眠 然后对比执行
        current_date = datetime.datetime.now().strftime("%m-%d-%H:%M")
        wait_time = calculate_wait_time(times, current_date, 'once')
        await asyncio.sleep(wait_time)
        await tasks(array)


def calculate_wait_time(times, current_time, time_type):
    if time_type == 'everyday':
        target_time = times
        target_time_parts = target_time.split(':')
        current_time_parts = current_time.split(':')
        target_seconds = int(target_time_parts[0]) * 3600 + int(target_time_parts[1]) * 60
        current_seconds = int(current_time_parts[0]) * 3600 + int(current_time_parts[1]) * 60
        if target_seconds <= current_seconds:
            wait_time = (24 * 3600 - current_seconds) + target_seconds
        else:
            wait_time = target_seconds - current_seconds
        return wait_time
    elif time_type == 'everymonth':
        target_date = times
        target_date_parts = target_date.split('-')
        current_date_parts = current_time.split('-')
        target_days = int(target_date_parts[0])
        current_days = int(current_date_parts[0])
        if target_days <= current_days:
            wait_time = (30 - current_days) + target_days
        else:
            wait_time = target_days - current_days
        return wait_time * 24 * 3600

    elif time_type == 'once':
        target_date = times
        target_date_parts = target_date.split('-')
        target_date_parts1 = target_date_parts[2].split(':')
        time1 = target_date_parts[0] * 2592000 + target_date_parts[1] * 86400 + target_date_parts1[0] * 3600 + \
                target_date_parts1[1] * 60

        current_date_parts = current_time.split('-')
        current_date_parts1 = current_date_parts[2].split(':')
        time2 = current_date_parts[0] * 2592000 + current_date_parts[1] * 86400 + current_date_parts1[0] * 3600 + \
                current_date_parts1[1] * 60

        wait_time = time1 - time2
        if wait_time > 0:
            return wait_time
        else:
            return wait_time + 31536000

import requests
import asyncio
import logging
import time
from threading import Thread
from multiprocessing import Process
from aiohttp import ClientSession
from pathlib import Path, PurePath


logging.basicConfig(encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


img_dir = Path('./imgs')


def download_img(url: str):
    start_time = time.time()
    if not img_dir.exists():
        img_dir.mkdir(parents=True)
    response = requests.get(url)
    filename = img_dir.joinpath(PurePath(url.split('/')[-1]))
    with open(filename, "wb") as f:
        f.write(response.content)
    logger.info(f'Download {filename} completed in {(time.time() - start_time):.2f} seconds')


async def download_async_img(url: str):
    start_time = time.time()
    if not img_dir.exists():
        img_dir.mkdir(parents=True)
    async with ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = img_dir.joinpath(PurePath(url.split('/')[-1]))
            with open(filename, "wb") as f:
                f.write(content)
            logger.info(f'Download {filename} completed in {(time.time() - start_time):.2f} seconds')


def created_thread(urls: list):
    
    start_time = time.time()
    threads = []
    for url in urls:
        thread = Thread(target=download_img, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    logger.info(f'Task completed in {(time.time() - start_time):.2f} seconds')


def created_multi(urls: list):

    start_time = time.time()
    processes = []
    for url in urls:
        process = Process(target=download_img, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    logger.info(f'Task completed in {(time.time() - start_time):.2f} seconds')
    

def created_async(urls: list):
    start_time = time.time()
    async def created_tasks(urls: list):
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_async_img(url))
            tasks.append(task)
        await asyncio.gather(*tasks)
    asyncio.run(created_tasks(urls))    
    logger.info(f'Task completed in {(time.time() - start_time):.2f} seconds')  
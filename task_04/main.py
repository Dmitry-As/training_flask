import argparse
from get import created_thread, created_multi, created_async


test_urls = ['https://www.firefallphotography.com/wp-content/uploads/2018/11/2018-Bisti-10-08-08449.jpg',
            'https://www.fabsite.org/misc/bsd-daemonette/Ceren-Ercen.jpg',
            'http://4everstatic.com/pictures/850xX/art/movies/bender-bending-rodriguez,-futurama-159767.jpg',
            'https://upload.wikimedia.org/wikipedia/en/0/02/Homer_Simpson_2006.png',
            'https://content.eveonline.com/www/newssystem/media/67273/1/Vargur_Thumb.jpg'
            ]


def parse():
    
    parser = argparse.ArgumentParser(description='Загрузка изображений с сайта')
    parser.add_argument('urls', help='url for download', nargs='*', default=test_urls)
    args = parser.parse_args()

    urls = args.urls
    
    print(f'Загрузка с помощью threading.')
    created_thread(urls)

    print(f'Загрузка с помощью multiprocessing')
    created_multi(urls)

    print(f'Загрузка с помощью asyncio')
    created_async(urls)


if __name__ == "__main__":
    parse()
import time
import concurrent.futures
from PIL import Image, ImageFilter


def process_image(img_name):

    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed')

def main():

    img_names = [
    'cat1.jpg',
    'cats.jpg',
    'cats2.jpg',
    'sunflowers.jpg',
    'turtle1.png',
    'turtleHR1.jpg',
    'turtleHR2.jpg',
    'turtleHR3.jpg',
    'turtleHR4.jpg',
    'turtleHR5.jpg',
    ]

    t1 = time.perf_counter()

    size = (200, 200)

# for img_name in img_names:


    # with concurrent.futures.ProcessPoolExecutor() as executor:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, img_names)

    t2 = time.perf_counter()

    print(f'Finished in {t2 - t1} seconds')


if __name__ == '__main__':
    main()
import multiprocessing
import os
import time
from PIL import Image
from multiprocessing import Pool

def worker(image_name):
    img = Image.open(image_name)
    img = img.rotate(-90, expand=True)
    img = img.resize((800, 600), Image.LANCZOS)
    img = img.convert('L')
    img.save(f"processed/out_{os.path.basename(image_name)}")

def create_test_images():
    os.makedirs("test_images", exist_ok=True)
    for i in range(10):
        img = Image.new('RGB', (1920, 1080), color=(i*25, 100, 200))
        img.save(f"test_images/img_{i}.jpg")

if __name__ == "__main__":
    create_test_images()
    images = [f"test_images/img_{i}.jpg" for i in range(10)]
    
    # ПОСЛЕДОВАТЕЛЬНО
    os.makedirs("processed", exist_ok=True)
    start = time.time()
    for img in images:
        worker(img)
    end = time.time()
    print(f"Последовательно: {end-start:.4f} секунд")
    
    # ПАРАЛЛЕЛЬНО
    import shutil
    shutil.rmtree("processed")
    os.makedirs("processed", exist_ok=True)
    
    start = time.time()
    with Pool(4) as pool:
        pool.map(worker, images)
    end = time.time()
    print(f"Параллельно: {end-start:.4f} секунд")
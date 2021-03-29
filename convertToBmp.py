from PIL import Image
import os
import time

def main():
    filepath = "/share/Ewan/UnprocessedImages/"
    x = 0
    images = os.listdir(filepath)
    proceed = False
    sizes = [os.stat(os.path.join(filepath, image)).st_size for image in images]
    while not proceed:
        time.sleep(0.1)
        new_sizes = [os.stat(os.path.join(filepath, image)).st_size for image in images]
        proceed = new_sizes == sizes
        sizes = new_sizes
    with open("/home/pi/code/e-paper/processed_images.txt", "r+") as file:
        processed_images = file.read().splitlines()
        for image in images:
            if image in processed_images:
                continue
            x += 1
            try:
                img = Image.open(os.path.join(filepath, image))
                img = img.convert("I")

                size = 296, 128
                img.thumbnail(size, Image.ANTIALIAS)
                thumb_size = img.size

                new_img = Image.new("1", size, color=1)
                new_img.paste(img, ((size[0]-thumb_size[0])//2, (size[1]-thumb_size[1])//2))
                new_img.save(os.path.join("/share/Ewan/ProcessedImages", os.path.splitext(image)[0]+".bmp"))
                file.write(image + "\n")
                print(image)
            except Exception as e:
                print(e)
        


if __name__ == "__main__":
    main()
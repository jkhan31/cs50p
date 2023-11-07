import os, sys
from PIL import Image, ImageOps

images = []
shirt = "shirt.png"

def main():
    check_num_args()
    check_image_extensions()
    overlay_image()


# check for 2 command-line arguments
def check_num_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return

# check valid image extensions
def check_image_extensions():
    exts = [".jpg",".jpeg",".png"]
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])
    if ext1[1].lower() not in exts:
        sys.exit("Invalid input")
    elif ext2[1].lower() not in exts:
        sys.exit("Invalid output")
    elif ext1[1].lower() != ext2[1].lower():
        sys.exit("Input and output have different extensions")
    else:
        try:
            image_in = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")

# resize input image
def resize_image():
    # get shirt.png size
    s = Image.open(shirt)
    shirt_size = s.size
    #print(f"shirt size: {shirt_size}")

    # open input image
    image_in = Image.open(sys.argv[1])
    #image_size = image_in.size
    #print(f"image size: {image_size}")

    # resize input image size to match shirt.png size
    return ImageOps.fit(image_in, shirt_size)
    #resized_image_size = resized_image.size
    #print(f"resized image size: {resized_image_size}")

def overlay_image():
    # open shirt.png
    s = Image.open(shirt)

    #resize input image
    resized_image = resize_image()

    # overlay image
    resized_image.paste(s, s)

    # save overlayed image
    resized_image.save(sys.argv[2])

if __name__ == "__main__":
    main()
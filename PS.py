from PIL import Image


def ps(image):
    img = Image.open(image)

    img.show()

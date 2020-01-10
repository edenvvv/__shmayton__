from PIL import Image


def ps(image):
    """Opens editing software with the requested image"""
    img = Image.open(image)

    img.show()

import PIL.Image


ASCII_CHARS = ["@", "#", "5", "%", "[", "*", "+", ":", ";", ",", "."]

def resize_image ( image, new_width = 100) :
    width, height = image.size
    aspect_ratio = height/width
    new_height = int (new_width*aspect_ratio)
    new_image = image.resize((new_width, new_height))
    return new_image

def gray_scale ( image ) :
    return image.convert("L")

def image_to_ascii(path) :
    path = input("Enter the path to the image: ")
    try: 
        image = PIL.Image.open(path)
    except: 
        print ("File Path Not found")
        
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path, new_width=100):
    
    image = Image.open(image_path)

    
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  
    image = image.resize((new_width, new_height))

    
    image = image.convert("L")

    
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // (255 // (len(ASCII_CHARS) - 1))] for pixel in pixels)

    
    ascii_str = "\n".join(ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width))

    return ascii_str


image_path = input("Entrez le chemin de l'image : ")
ascii_art = image_to_ascii(image_path)


print(ascii_art)
with open("output.txt", "w") as f:
    f.write(ascii_art)

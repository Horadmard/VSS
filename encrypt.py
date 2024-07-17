from PIL import Image

def text_to_image(text, output_image_path):
    # Convert the text to ASCII values
    ascii_values = [ord(char) for char in text]
    
    # Determine the dimensions of the image
    width = int(len(ascii_values) ** 0.5) + 1
    height = (len(ascii_values) + width - 1) // width
    
    # Create an image with the determined dimensions
    image = Image.new("L", (width, height))
    pixels = image.load()
    
    # Set the pixels of the image to the ASCII values
    for i, value in enumerate(ascii_values):
        x = i % width
        y = i // width
        pixels[x, y] = value
    
    # Save the image
    image.save(output_image_path)

# Example usage
# text_to_image("This is a Secret code!!", "output_image.png")

from PIL import Image

def image_to_text(input_image_path):
    # Open the image
    image = Image.open(input_image_path)
    pixels = image.load()
    width, height = image.size
    
    # Read the ASCII values from the image
    ascii_values = []
    for y in range(height):
        for x in range(width):
            ascii_values.append(pixels[x, y])
    
    # Convert ASCII values to characters
    chars = [chr(value) for value in ascii_values if value != 0]
    
    # Join the characters to form the original text
    text = "".join(chars)
    return text

# Example usage
original_text = image_to_text("output_image.png")
print(original_text)

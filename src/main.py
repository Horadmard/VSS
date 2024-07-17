import encrypt
import decrypt


if __name__ == '__main__':

    while (True):

        print('What do you wanna do?\n \
        1. Encrypt Text into an Image\
        2. Decrypte an Image and reach to a Text\
        3. Do nothing, Thanks for nothing!')

        choice = int(input())

        if choice == 1:
            plain_text = input('Your massage:')
            image_name = input('Image name:')
            encrypt.text_to_image(plain_text, image_name+'.png')

        elif choice == 2:
            image_name = input('Image name:')
            print(decrypt.image_to_text(image_name+'.png'))

        elif choice == 3:
            break

        else:
            print('Invalid!')

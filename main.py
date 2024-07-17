import encrypt, decrypt


if __name__ == '__main__':

    print('What do you wanna do?\
    1. Encrypt Text into an Image\
    2. Decrypte an Image and reach to a Text\
    3. Do nothing, Thanks for nothing!')


    while(True):

        choice = int(input())
        
        if choice == 1:
            plain_text = input('Your massage:')
            image_name = input('Image name:')
            encrypt.text_to_image('{plain_text}', '{image_name}')

        elif choice == 2:
            image_name = input('Image name:')
            decrypt.image_to_text('{image_name}')

        elif choice == 3:
            break
        
        else:
            print('Invalid!')
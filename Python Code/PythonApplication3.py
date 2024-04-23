import os
import openai
import base64
import datetime

openai.api_key = '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'

prefix = 'C:/Users/E.Mazarakis/Desktop/DALLE_IMAGES/image'  #Directory path of saved images
suffix = '.png'                                             # Type of saved image

class OpenAIImageError(Exception):
    pass

def get_user_input():
    prompt = input("Enter the prompt: ")
    size_option = input("Enter 1 for 1024x1024, 2 for 512x512, or 3 for 256x256:  ")
    if size_option == '1':
        size = '1024x1024'
    elif size_option == '2':
        size = '512x512'
    elif size_option == '3':
        size = '256x256'
    else:
        print("Invalid option! Using default size 1024x1024")
        size = '1024x1024'
    num_images = int(input("Enter the number of images: "))
    return prompt, size, num_images



def generate_image(prompt, num_images, size, format):
    # must catch the errors.
    try:
        res = openai.Image.create(
            prompt = prompt,
            n = num_images,
            size = size,
            response_format = format
        )
        return res
    except openai.error.OpenAIError as e:
        raise OpenAIImageError("OpenAI API Error: " + str(e))
    except Exception as e:    
        raise OpenAIImageError("An unexpected error occurred: " + str(e))


def save_image(res, size, prefix, suffix):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    for i in range(0, len(res['data'])):
        b64 = res['data'][i]['b64_json']
        filename = f'{prefix}_{size}_{timestamp}_{i}_{suffix}'
        print('Saving file ' + filename)
        with open(filename, 'wb') as f:
            f.write(base64.urlsafe_b64decode(b64))
      
def main():
    while True:
        try:
            prompt, size, num_images = get_user_input()
            response = generate_image(prompt, num_images, size, 'b64_json')
            save_image(response, size, prefix, suffix)
        except  OpenAIImageError as e:
            print("Error:", e)
            print("Exiting program.")
            break
        

if __name__ == "__main__":
    main()
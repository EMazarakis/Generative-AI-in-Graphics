# pip install openai [version openai 1.23.2]
# imports
from openai import OpenAI, OpenAIError  # OpenAI Python library to make API calls
import requests                         # used to download images
import os                               # used to access filepaths
import datetime                         # used to name the filename of the image
from PIL import Image  # used to print and edit images

# initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "YOUR-API-KEY-HERE"))

# set a directory to save DALL·E images to
image_dir_name = "C:/XXX/YYY/Desktop/DALLE_IMAGES/"
image_dir = os.path.join(os.curdir, image_dir_name)

# Type of saved image
suffix = '.png'    
MODEL = "dall-e-2"  # supported sizes for 256x256, 512x512, or 1024x1024

# Custom exception class for OpenAI image errors
class OpenAIImageError(Exception):
    pass

# Function to get user input (prompt, size, number of images)
def get_user_input():
    prompt = input("Enter the prompt: ")
    size_option = input("Enter 1 for 1024x1024, 2 for 512x512, or 3 for 256x256:  ")
    if size_option == '1':
        size = "1024x1024"
    elif size_option == '2':
        size = "512x512"
    elif size_option == '3':
        size = "256x256"
    else:
        print("Invalid option! Using default size 1024x1024")
        size = "1024x1024"
    num_images = int(input("Enter the number of images: "))
    return prompt, size, num_images


# Function to generate image using OpenAI API
def generate_image(prompt, num_images, size, format, m):
    # must catch the errors.
    try:
        generation_response = client.images.generate(
            model = m,
            prompt = prompt,
            n = num_images,
            size = size,
            response_format=format,
        )
        return generation_response
    except OpenAIError as e:
        raise OpenAIImageError("OpenAI API Error: " + str(e))
    except Exception as e:    
        raise OpenAIImageError("An unexpected error occurred: " + str(e))
    

# Function to save image data to files
def save_image(res, size, prefix, suffix):
     # Generate timestamp for unique filenames
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    for i, image in enumerate(res.data):    # response.data is a list of JSON objects with the urls of each generated image.
        # Construct filename
        generated_image_name = f'image_{size}_{timestamp}_{i}_{suffix}'
        generated_image_filepath = prefix + generated_image_name
        generated_image_url = res.data[i].url                        # extract image URL from response
        generated_image = requests.get(generated_image_url).content  # download the image        

        # Save image data to file
        print('Saving file ' + generated_image_filepath)
        with open(generated_image_filepath, "wb") as image_file:
            image_file.write(generated_image)  # write the image to the file
            


# Main function to run the program      
def main():
    while True: # Setting a loop, so the user can generate images indefinitely
        try:
            prompt, size, num_images = get_user_input()     #ask user for the input
            response = generate_image(prompt, num_images, size, "url", MODEL)   #create the images
            save_image(response, size, image_dir, suffix)                       #save the images to local disk
        except  OpenAIImageError as e:
            print("Error:", e)
            print("Exiting program.")
            break
        
# Entry point of the script
if __name__ == "__main__":
    main()
    

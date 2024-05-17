# Official GitHub repo: https://github.com/openai/CLIP

# First you need to install the following 2:
# pip install -U torch torchvision
# pip install -U git+https://github.com/openai/CLIP.git

# Import all the appropriate libraries.
from pickle import FLOAT
import torch
import clip
from PIL import Image   #PIL: Python Imaging Library. It's a library in Python that adds support for opening, manipulating, and saving many different image file formats
from torchvision.transforms import RandomEqualize
import csv
import time
import numpy as np
from collections import defaultdict


# If you want to see all the available models.
available_models = clip.available_models()
print("All the available models of CLIP family are: ", available_models)

##########################################################################
# All the relevant variables for the image file name.
##########################################################################
# Here is the directory prefix where the model images are hosted.
prefix_path = "C:/Users/E.Mazarakis/Desktop/000.Produced_Images/"

# The folder name for each model's images.
prefix_models = ["001.Stable_Diffusion", "002.DALLE_2", "003.Pix_Art_a"]

# The folder name containing images of the appropriate size. 
prefix_size = ["001.512_512","002.1024_1024"]

# The folder name of eash taksk type
prefix_task = ["001.Colouring", "002.Counting", "003.Conflicting", "004.Text", "005.Positional", "006.Faces"]

# Abbreviations of the model names
models_abbr = ["SD","DL", "PA"]

# The size (width, height) of each image
img_sizes = ["512", "1024"]

# The name of each task type of the benchmark
tasks = ["coloring", "counting", "conflicting", "text", "positional", "faces"]

# The number of images for each task type that we check
NUM_OF_IMAGES = 12

##########################################################################
##########################################################################
# Our benchmark
##########################################################################
# Create a tuple of triples with three values each
my_benchmark_tuple = (
    ("coloring", "A red colored car", 1),
    ("coloring", "A black colored car", 2),
    ("coloring", "A pink colored car", 3),
    ("coloring", "A navy blue colored car", 4),
    ("coloring", "A red car and a white sheep", 5),
    ("coloring", "A blue bird and a brown bear", 6),
    ("coloring", "A green apple and a black backpack", 7),
    ("coloring", "A green cup and a blue cell phone", 8),
    ("coloring", "A red pencil in a green cup on a blue table", 9),
    ("coloring", "An office with five desks and seven colorful chairs", 10),
    ("coloring", "An orange bird scaring a blue scarecrow with a red pirate hat", 11),
    ("coloring", "A photo of two pink football balls and three green basketball balls on a bench", 12),
    ("counting", "One tennis ball on the court", 1),
    ("counting", "Three people crossing  the street", 2),
    ("counting", "Two monkeys eating banana", 3),
    ("counting", "Bench in a park with two backpacks on it", 4),
    ("counting", "Nine children doing a circle dance around a Christmas tree", 5),
    ("counting", "An office desk with six laptops on it", 6),
    ("counting", "Person holding  four toy pyramids", 7),
    ("counting", "Five photograph prints are hanging to dry in a dark room", 8),
    ("counting", "Person carrying a stack of twelve books", 9),
    ("counting", "Two people juggling ten balls together", 10),
    ("counting", "Birthday cake with exactly twenty candles on it", 11),
    ("counting", "Office room with fifteen chairs", 12),
    ("conflicting", "A zebra without strips", 1),
    ("conflicting", "A penguin in a city", 2),
    ("conflicting", "Rainbow colored Ferrari", 3),
    ("conflicting", "A giraffe kissing a monkey", 4),
    ("conflicting", "A panda inside a cup of tea", 5),
    ("conflicting", "A giraffe inside a car", 6),
    ("conflicting", "An ant under the sea", 7),
    ("conflicting", "A motorcycle inside an oven", 8),
    ("conflicting", "A polar bear on the desert", 9),
    ("conflicting", "A man walking on the ceiling", 10),
    ("conflicting", "A fish eating a pelican", 11),
    ("conflicting", "A horse riding  an astronaut in the forest", 12),
    ("text", "A sign that says 'Hello'", 1),
    ("text", "A sign that says 'World'", 2),
    ("text", "A sign that says 'Hello World'", 3),
    ("text", "A sign that says 'World Hello'", 4),
    ("text", "A sign that says 'Speed limit 45'", 5),
    ("text", "A sign that says 'Do not pass !'", 6),
    ("text", "A sign that says 'No pedestrians !'", 7),
    ("text", "A sign that says 'No overtaking !'", 8),
    ("text", "A sign that says 'No Goods materials'", 9),
    ("text", "A sign that says 'No hazardous materials'", 10),
    ("text", "A sign that says 'You must not turn Right!'", 11),
    ("text", "A sign that says 'Maximum speed limit 80 km'", 12),
    ("positional", "A train on top of a surfboard", 1),
    ("positional", "A wine glass on top of a dog", 2),
    ("positional", "A bicycle on top of a boat", 3),
    ("positional", "An umbrella under a spoon", 4),
    ("positional", "A car on the left of a bus", 5),
    ("positional", "A black apple on the right of  a green backpack", 6),
    ("positional", "A carrot on the left of a broccoli", 7),
    ("positional", "A pizza on the right of a suitcase", 8),
    ("positional", "A cat on the right of a tennis racket", 9),
    ("positional", "A stop sign on the right of a refrigerator", 10),
    ("positional", "A sheep to the right of a wine glass", 11),
    ("positional", "A zebra to the right of a fire hydrant", 12),
    ("faces", "Face of a man with a goatee", 1),
    ("faces", "Face of an angry teacher", 2),
    ("faces", "Face of a kid with a tiger make-up", 3),
    ("faces", "Face of an old lady with blue hair and a wide smile", 4),
    ("faces", "A bald man doing a handstand", 5),
    ("faces", "Face of a woman with brown hair looking over her shoulder", 6),
    ("faces", "Sad face of a blonde girl holding a popped balloon", 7),
    ("faces", "Face of a weightlifting white hair Olympic gold medalist lifting 120kg with a referee next to it encouraging him", 8),
    ("faces", "The face of a soldier with camouflaged face painting obscured by leaves", 9),
    ("faces", "A face of a man with a beard with water splashing onto his face", 10),
    ("faces", "A dark messy hair boy rolling his tongue with blue light shinning on his face", 11),
    ("faces", "A young kid with dark eye bags standing in front of her grandma with wrinkles looking at the sky", 12)
)

# Convert the tuple of triples into a dictionary with keys as tuples of (key, number)
my_benchmark_dict = {(key, number): value for key, value, number in my_benchmark_tuple}

##########################################################################
##########################################################################

# This function calculate the clip score between an image and a prompt
def calculate_clip_score(path_to_image, prompt):
    """
    Parameters
    ----------
    path_to_image : str
        A string which is the path to the image file.
    
    prompt : str
        A string that we want to see as far as it is related to the image.
    
    Returns
    -------
    similarity_score: float
        computes the dot product between image and text.
    """
    # Load the pre-trained CLIP model and the image
    # preprocess: A torchvision transform that converts a PIL image into a tensor that the returned model can take as its input
    model, preprocess = clip.load('ViT-L/14@336px')  # Returns the model and the TorchVision transform needed by the mode
    try:    
        image = Image.open(path_to_image, "r") # Opens and identifies the given image file & returns and Image object.
    except IOError as e:
        # Handle IO errors (e.g., file not found, cannot read file)
        print("An error occurred during the opening of the image file:", e)
    except Exception as e:
        # Handle other exceptions
        print("An unexpected error occurred during the opening of the image file:", e)

    # Preprocess the image and tokenize the text
    #Convert a PIL image to tensor and then in this tensor add a dimension, a batch dimension
    image_data = preprocess(image).unsqueeze(0)  #image_input is a torch.Tensor object
    text_data = clip.tokenize([prompt]) # Returns a two-dimensional tensor containing the resulting tokens, the tokenized representation of given input string(s)
    
    # Move the inputs to GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    image_data = image_data.to(device)    # Move the image_input (tensor) to the specified device (CPU or GPU) 
    text_data = text_data.to(device)      # Move the text_input (tensor) to the specified device (CPU or GPU)
    model = model.to(device)              # Move the CLIP model to the specified device (CPU or GPU)

    # Generate embeddings for the image and text
    # Forward propagate input data through the network without computing gradients, thus saving memory and computation.
    with torch.no_grad():   
        image_attr = model.encode_image(image_data) # Given a batch of images, returns the image features encoded by the vision portion of the CLIP model.
        text_attr = model.encode_text(text_data)    # Given a batch of text tokens, returns the text features encoded by the language portion of the CLIP model.

    # Normalize the features
    # dim = -1: The operation will be performed along the last dimension of the tensor. 
    # keepdim = True: The output tensor will have the same number of dimensions as the input tensor, with one of the dimensions having a size of 1.
    # .norm(): Computes the L2 (Frobenius norm /Euclidean norm) norm along the last dimension of a tensor while retaining the dimensionality of the tensor.
    image_attr = image_attr / image_attr.norm(p='fro', dim=-1, keepdim=True) # Normalizes each feature vector, ensuring that each vector has unit length in the feature space
    text_attr = text_attr / text_attr.norm(p='fro', dim=-1, keepdim=True)    # Normalizes each feature vector, ensuring that each vector has unit length in the feature space
    
    # Calculate the cosine similarity to get the CLIP score
    # matmul: matrix multiplication between tensors. 
    # text_attr.T: Transpose the text_attr tensor
    similarity_score = torch.matmul(image_attr, text_attr.T).item() # Returns a scalar value from the multiplication of tensors.
   
    return similarity_score


# Main function to run the program  
def main():
    
    # File path to write the scores
    score_file = "C:/Users/E.Mazarakis/Desktop/clip_scores_file.csv"
    metrics_file = "C:/Users/E.Mazarakis/Desktop/clip_metrics_file.csv"

    # We will store all the values on a list as tuple of six elements, in order to calculate then Mean  and Median
    image_text_values_list = []

    # Record the start time
    start_time = time.time()
    
    print("Calculate CLIP Score:")
    print("For: " + str(len(prefix_models)) + " text-to-image model(s).")
    print("For: " + str(len(img_sizes)) + " image size(s).")
    print("For: " + str(len(tasks)) + " task type(s).")
    print("For: " + str(NUM_OF_IMAGES) + " image(s).")
    print("Total number of CLIP scores: " + str(len(prefix_models)*len(img_sizes)*len(tasks)*NUM_OF_IMAGES))
    
    
    # Write score data to the file
    with open(score_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model', 'Size', 'Task', 'Image', 'Prompt', 'CLIP_Score'])  # Write header

        # This for loop creates the file name of each image and the corresponding prompt and call the function to calculate the CLIP score
        for i in range( len(prefix_models) ):      # For the 3 models (Stable Diffusion, DALL-E 2, Pix-Art-a)
            for j in range( len(img_sizes) ):      # For the 2 sizes (512, 1024)
                for k in range( len(tasks) ):      # For the 6 task type
                    for l in range( NUM_OF_IMAGES ):    # For the 12 images
                
                        # Example of a file path: "C:/Users/E.Mazarakis/Desktop/000.Produced_Images/001.Stable_Diffusion/001.512_512/001.Colouring/001.SD_512_coloring_1.png"
                        image_file_path = prefix_path + prefix_models[i] + "/" + prefix_size[j] + "/" + prefix_task[k] + "/" + ("0" if (l+1) > 9 else "00") + str(l+1) + "." + models_abbr[i] + "_" + img_sizes[j] + "_" + tasks[k] + "_" + str(l+1) + ".png"
                
                        # For a certain task type we get the appropriate prompt
                        # Access values by key and number for the benchmark dictionary
                        text = tasks[k] + ": " + my_benchmark_dict[(tasks[k], (l+1) )]
                    
                        # Call the function in order to calculate the similarity score between the image and text
                        CLIP_SCORE = calculate_clip_score(image_file_path,  text) 
                        #print(image_file_path + "|" + text + "|" + str(format(CLIP_SCORE, '.4f'))) #format(CLIP_SCORE, '.4f').replace('.', ',')
                        
                        # Everything listed below is to be written in a file.
                        model = models_abbr[i]  # For which model do we compute the CLIP Score
                        size = img_sizes[j]     # For which image size do we compute the CLIP Score
                        task_type = tasks[k]    # For which task type do we compute the CLIP Score
                        photo = ("0" if (l+1) > 9 else "00") + str(l+1) + "." + models_abbr[i] + "_" + img_sizes[j] + "_" + tasks[k] + "_" + str(l+1) + ".png" # For which image do we compute the CLIP Score
                        prompt = my_benchmark_dict[(tasks[k], (l+1) )]   # For which prompt do we compute the CLIP Score
                        score =  format(CLIP_SCORE, '.4f')     # This is the requested value, truncated to 4 decimal digits              
                        
                        # Define a tuple of six values
                        temp_tuple = (model, size, task_type, photo, prompt, score)
                        
                        # Add the tuple to the list
                        image_text_values_list.append(temp_tuple)
                        
                        # Write data row in the file
                        writer.writerow([model, size, task_type, photo, prompt, score.replace('.', ',')])  
                        
                    
                    print("------------------------------------------------------------------------")
    

    ######################################################################################################################################
    # Compute Mean, Median for each task across all sizes, models
    # Define the indices of values within each tuple
    model_index = 0 
    size_index = 1
    category_index = 2 
    value_index = 5  
    
    # Initialize dictionaries to store means and medians for each task
    means_dict = defaultdict(list)
    medians_dict = defaultdict(list)
    std_dict = defaultdict(list)

    for model, size, category, _, _, value in image_text_values_list:
        key = (model, size, category)    
        means_dict[key].append(float(value))
        medians_dict[key].append(float(value))
        std_dict[key].append(float(value))
    
    # Calculate means and medians for each combination
    means_result = {}
    medians_result = {}
    std_result = {}
    
    for key, values in means_dict.items():
        means_result[key] = np.mean(values)

    for key, values in medians_dict.items():
        medians_result[key] = np.median(values)

    for key, values in std_dict.items():
        std_result[key] = np.std(values)

    # Write metrics data to the file
    with open(metrics_file, mode='w', newline='') as file:
        metrics_writer = csv.writer(file)
        metrics_writer.writerow(['Model', 'Size', 'Task', 'Mean', 'Mean%', 'Median', 'Median%', 'Std', 'Std%' ])  # Write header

        # Print means and medians for each combination
        for key in means_result:
            #Model:key[0], Size: key[1], Category: key[2]
            
            # Write data row in the file
            metrics_writer.writerow([ key[0], key[1], key[2], format(means_result[key], '.4f').replace('.', ','), format(means_result[key]*100, '.4f').replace('.', ','), format(medians_result[key], '.4f').replace('.', ','), format(medians_result[key]*100, '.4f').replace('.', ','), format(std_result[key], '.4f').replace('.', ','), format(std_result[key]*100, '.4f').replace('.', ',') ]) 
        

    # Record the end time
    end_time = time.time()

    # Calculate the duration
    duration = (end_time - start_time)/60
    print("------------------------------------------------------------------------")
    print("CLIP scores computed on:  ", duration, "minutes")
    print("Scores has been written to ", score_file)
    print("Metrics has been written to ", metrics_file)
    print("Sum-Up has been written to ", sum_up_file)
    print("------------------------------------------------------------------------")


# Entry point of the script
if __name__ == "__main__":
    main()


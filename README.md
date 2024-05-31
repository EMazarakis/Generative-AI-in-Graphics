# Generative-AI-in-Graphics
A summary of the master thesis with title: **Evaluation of three text-to-image Gen AI models**

The structure of the thesis is mentioned in the following image:
![Thesis organization](/images/000.Thesis_Organization.png)



The aim of this thesis is to focus on Generative AI algorithms, in order to list and classify the available Generative AI algorithms and applications that can be exploited in the scientific fields of Graphics.

We first provide all the necessary definitions commonly used around the AI, Generative AI, Generative AI model. 
This is the necessary background we need to be able to understand what is mentioned in this thesis. 
Then we talk about some fundamental deep learning architectures that used on generative AI models. Thereafter, we describe the implementation phases of a Generative AI models. 
Then we offer a classification of some of the advanced GAI algorithms.
The categorization of the models have been done based on the generated content, output.

In the subsequent chapter, we elucidate the three models under scrutiny, namely, the prevalent open-source frameworks (Stable Diffusion and Pix-Art-α), alongside the commercial counterpart, DALL-E 2. These models share three common hyperparameters: prompt, height, and width, thus guiding our experimental setup. Subsequently, we conducted model executions based on these parameters. To conduct a human evaluation of these models, we present a benchmark comprising six task-types, each consisting of twelve prompts.

In the conclusive third chapter of this thesis, the outcomes of the human evaluation stemming from the implementation of Generative AI models for graphics are presented. Additionally, notable discoveries pertaining to these three models within the graphics domain are discussed.


# Evaluation
We perform an assessment on three text-to-image Gen AI models, the most common open-source (Stable Diffusion, Pix-Art-α), and commercial (DALL-E 2) models. 
The assessment that we do is: qualitative and quantitative.
These models have 3 common hyperparameters: prompt, height, width. 
For the evaluation of these three models, we provide a benchmark of six task-types with twelve prompts of each task type.

## Generative AI models for evaluation
We assess three models, the DALL-E 2, Stable Diffusion and Pix-Art-α

### DALL-E 2
This folder contains the python code files. In order to create DALL-E 2 images through openai API we used the file [python-dalle-api-call](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/DALL-E%202/PythonApplication5.py) 

### Stable Diffusion
This folder contains the installation instructions of the stable diffusion v.1.5 model and of the relevant web-ui in order to execute the model. [stable disffusion](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/Stable%20Diffusion/Installation_Instructions.md)

### Pix-Art-α
This folder contains all the relevant urls in order to use the model [Pix-Art-α](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/Pix-Art-%CE%B1/Model_Demo.md) .

## Benchmarking
We provide a multi-task benchmark for evaluating the text-to-image models. Our benchmark contains a suite of tasks over multiple applications that capture a model’s ability to handle different features of a text prompt.
Our benchmark contains:
1. colouring task: The prompt is used to examine the ability of the image generation system to generate images that have colouring concepts.
2. counting task: The prompt is used to examine the ability of the image generation system to generate images that have counting concepts.
3. conflicting task: The prompt is used to examine the ability of the image generation system to generate images that have conflicting concepts.
4. text task: The prompt is used to examine the ability of the image generation system to generate images that have texting concepts.
5. positional task: The prompt is used to examine the ability of image generation systems to generate images with accurate positional information.
6. faces task: The prompt is used to examine the ability of image generation systems to generate images with accurate facing information.


## Assessment
### Qualitative Assessment
Each task type contains 12 prompts. Our evaluation protocol consists of human ratings. 
For each prompt, the rater is shown images which are from DALLE-2, from Stable Diffusion, and from Pix-Art-α. 
The human rater will be asked one question:
1. How well does the image represent the text caption: [Text Caption] ?
   - Question subjectively evaluates image-text alignment.

For each question, the rater is asked to select from rating between 1(worst) and 5(best).

We aggregate scores from 17 raters, the evaluated images were 432 (17 raters x 3 models x 2 sizes x 6 tasks x 12 prompts = 7344 ratings)

:point_right: To see and download the prompts of the benchmarking you can go to: [Benchmarking](Benchmarking/benchmark.csv).


### Quantitative Assessment
Each task type contains 12 prompts. Our evaluation protocol consists of the CLIP score.
The score is the cosine similarity between the prompt and the generated image.
The code that we used in order to produce the scores can be found:

# Generative Images
The folder [Produced Images](https://github.com/EMazarakis/Generative-AI-in-Graphics/tree/main/Generative%20Images) contains per model, size and task type the generative images in which we did human evaluation.
The folder contains sub-folder per model:
1. PA = Pix-Art-α
2. DL = DALL-E 2
3. SD = Stable diffusion

The structure of the folder is
1. PA
   - 512 
     - 001.Colouring
     - 002.Counting
     - ....
   - 1024
     - 001.Colouring
     - 002.Counting
     - ....
2. DL
   - 512 
     - 001.Colouring
     - 002.Counting
     - ....
   - 1024
     - 001.Colouring
     - 002.Counting
     - ....
2. SD
   - 512 
     - 001.Colouring
     - 002.Counting
     - ....
   - 1024
     - 001.Colouring
     - 002.Counting
     - ....
    

# Latex Files
All the relevant latex files for the master thesis is under the directory [latex](https://github.com/EMazarakis/Generative-AI-in-Graphics/tree/main/Latex%20Files)

# Master Thesis
:point_right: To see and download the master thesis you can go to: [Master Thesis](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/Master%20Thesis/Master_Thesis_en.pdf).

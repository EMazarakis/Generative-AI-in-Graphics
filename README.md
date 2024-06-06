# Generative-AI-in-Graphics
A summary of the master thesis with title: **Evaluation of three text-to-image Gen AI models**

The structure of the thesis is mentioned in the following image:
![Thesis organization](/images/000.Thesis_Organization.jpg)


# Abstract
This master's thesis delves into the cutting-edge domain of Generative Artificial Intelligence (AI) with a primary focus on graphics applications. The study explores various deep learning techniques, including Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs), Diffusion Models, and Transformers. These methods have revolutionized the field by enabling the generation of realistic and high-quality content, ranging from images to entire 3D-scenes.
The investigation begins with an exploration of Variational Autoencoders, emphasizing their role in capturing latent representations of data. Subsequently, the research transitions to Generative Adversarial Networks, discussing their adversarial training process for generating authentic content. Additionally, the study reviews Diffusion Models, which excel in probabilistic generative modeling, and Transformers, renowned for their success in sequential data generation tasks.
A significant portion of the thesis is dedicated to the execution and evaluation of three models (DALL-E 2, Stable Diffusion, Pix-Art-α) in the graphics domain based on some parameters. Executing generative models through Python code or running them locally through an interface empowers users to harness advanced AI techniques. Furthermore, the evaluation of these models involves both qualitative and quantitative processes. This enables the creation of diverse, high-quality content, revolutionizing applications in various domains seamlessly.
The findings highlight the transformative impact of these generative models on the field of graphics, showcasing their ability to create immersive and novel visual content through the amalgamation of sophisticated deep learning techniques.


# Assessing text-to-image models
We perform an assessment on three text-to-image Gen AI models, the most common open-source (Stable Diffusion, Pix-Art-α), and commercial (DALL-E 2) models. 
The assessment that we do is: qualitative and quantitative.
These models have 3 common hyperparameters: prompt, height, width. 
For the evaluation of these three models, we provide a benchmark of six task-types with twelve prompts of each task type.

## Assessing Models
We assess three models, DALL-E 2, Stable Diffusion and Pix-Art-α

### DALL-E 2
This folder contains the python code files. In order to create DALL-E 2 images through openai API we used the file [python-dalle-api-call](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/DALL-E%202/PythonApplication5.py) 

### Stable Diffusion
This folder contains the installation instructions of the stable diffusion v.1.5 model and of the relevant web-ui in order to execute the model. [stable disffusion](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/Stable%20Diffusion/Installation_Instructions.md)

### Pix-Art-α
This folder contains all the relevant urls in order to use the model [Pix-Art-α](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/Pix-Art-%CE%B1/Model_Demo.md) .

## Benchmarking Tasks
We provide a multi-task benchmark for evaluating the text-to-image models. Our benchmark contains a suite of tasks over multiple applications that capture a model’s ability to handle different features of a text prompt.
Our benchmark contains:
1. colouring task: The prompt is used to examine the ability of the image generation system to generate images that have colouring concepts.
2. counting task: The prompt is used to examine the ability of the image generation system to generate images that have counting concepts.
3. conflicting task: The prompt is used to examine the ability of the image generation system to generate images that have conflicting concepts.
4. text task: The prompt is used to examine the ability of the image generation system to generate images that have texting concepts.
5. positional task: The prompt is used to examine the ability of image generation systems to generate images with accurate positional information.
6. faces task: The prompt is used to examine the ability of image generation systems to generate images with accurate facing information.

A whole list of benchmark prompts can be found on the [Benchmarking](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/Benchmarking/benchmark.csv) folder. 

## Assessment Techniques
There are two methods for evaluating generative AI models. First approach is the qualitative method that entails examing the generated data through human evaluation. Alternatively, the other approach involves quantitative method, where numerical scores are calculated based on certain criteria.

### Qualitative Assessment
Each task type contains 12 prompts. Our evaluation protocol consists of human ratings. 
For each prompt, the rater is shown images which are from DALLE-2, from Stable Diffusion, and from Pix-Art-α. 
The human rater will be asked one question:
1. How well does the image represent the text caption: [Text Caption] ?
   - Question subjectively evaluates image-text alignment.

For each question, the rater is asked to select from rating between 1(worst) and 5(best).

We aggregate scores from 17 raters, the evaluated images were 432 (17 raters x 3 models x 2 sizes x 6 tasks x 12 prompts = 7344 ratings)

:point_right: To see and download the prompts of the benchmarking you can go to: [Benchmarking](Benchmarking/benchmark.csv).

:point_right: You can find the human evaluation results, including both rater responses and analysis on [Human Evaluation](https://github.com/EMazarakis/Generative-AI-in-Graphics/tree/main/Human%20Evaluation) folder.

### Quantitative Assessment
To asess the similarity between an image and the prompt, we calulate the CLIP score, which represents the cosine similarity of the embeddings generated by the model for the image and the text.To accomplish this, python code snippet has been written based on the official repo of openai.

:point_right:  All the relevant info for the CLIP, such as the python code, the results of the python code (CLIP Scores) and the relavant analysis based on the results can be found on [CLIP](https://github.com/EMazarakis/Generative-AI-in-Graphics/tree/main/CLIP) folder.


## Results
The result of the qualitative assessment (human evaluation) for the 512-sized images.
![HumanEvaluation512](/images/030.512_Human_Norm_Scores.PNG)

The result of the qualitative assessment (human evaluation) for the 1024-sized images.
![HumanEvaluation1024](/images/031.1024_Human_Norm_Scores.PNG)



## Conclusion
We proposed two ways of evaluating text-to-image generative models, human evaluation and clip score metric. Our proposed benchmark allows for testing individual competencies and limitations of the different generative models.

Initially, in the human evaluation, the commercial model DALL-E 2 demonstrates superior performance compared to the other two free models for 512-sized images. DALL-E 2 excels in the tasks of coloring, counting, faces, and text. It effectively understands and reproduces the specified colors and the number of objects. Additionally, it performs very well in the faces task. However, it should be noted that faces are not accurately reproduced when they are not explicitly mentioned in the prompt, and the pupils of the eyes are not always rendered correctly. Furthermore, although its performance in text tasks decreases, it remains higher than that of the other two models. When the image size is increased to 1024, DALL-E 2 continues to outperform the other two models, now excelling in five tasks instead of four as with the 512-sized images.

Pix-Art-α is the second-best model based on the human evaluation of 512-sized images. It performs well in two categories: conflicting and positional. This indicates that it understands and accurately reproduces conflicting themes present in the prompt, as well as the spatial arrangement of objects within the image. When the image size is increased to 1024, Pix-Art-α remains the second-best model. However, it excels only in the conflicting task, suggesting that the change in image size negatively affects its performance in the positional task. 

Stable Diffusion does not perform well in any of the six categories for either 512-sized or 1024-sized images. This indicates poor alignment between the prompts and the generated images.

Additionally, in the CLIP score metric, we observe that the commercial model DALL-E 2 exhibits the best text-image alignment among the three models for the 512-sized images. It achieves the highest score in three tasks: coloring, faces, and text. Furthermore, Pix-Art-α emerges as the second-best model based on the CLIP score, demonstrating good performance in the conflicting and positional tasks. Stable Diffusion excels only in one task, which is counting. Moreover, in the 1024-sized images, DALL-E 2 continues to perform as the best model among the three. It performs well in four tasks: conflicting, counting, positional, and text. Pix-Art-α remains the second-best model based on the CLIP metric, performing well in two tasks: coloring and faces. On the other hand, Stable Diffusion shows poor performance in all tasks.
Understanding the limitations is critical for picking the suitable model for each task and application, advancing the quality of generative models, and aligning their performance with human goals.


# Generative Images
The folder [Generative Images](https://github.com/EMazarakis/Generative-AI-in-Graphics/tree/main/Generative%20Images) contains per model, size and task type the generated images in which we did quantitative and qualitative evaluation.
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

:point_right: A synopsis of the master thesis can be found on [PPT presentation](https://github.com/EMazarakis/Generative-AI-in-Graphics/blob/main/PPT%20Presentation/Master%20Thesis%20presentation.pdf)

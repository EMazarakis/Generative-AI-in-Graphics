# Stable Diffusion installation instructions on windows machine

## Local PC specifications
* Processor: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz   2.42 GHz
* Installed RAM: 24,0 GB
* System Type: 64-bit operating system, x64-based processor
* OS: Windows 10 Enterprise

## Installation instructions
To run the stable diffusion model locally on our pc we must do the following:

1. First, we have to install git on our pc. We can download it from the following link: [git](https://git-scm.com/downloads)
2. Then we have to install the python 3.10.6 to our pc. We can download it from the following link: [python 3.10.6](https://www.python.org/downloads/release/python-3106/)
   - Don’t forget to click:  Add python XX to PATH.
3. Then we have to install the stable diffusion webui to our pc. We can clone the repository from the following link: [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
4. We go to the above link and copy the url. We open a **cmd** and run the following command:
   - git clone  https://github.com/AUTOMATIC1111/stable-diffusion-webui.
5. Then we have to install the model. We can download it from the following link: [stable diffusion model](https://huggingface.co/runwayml/stable-diffusion-v1-5)
   - From this page we download the v1-5-pruned-emaonly.ckpt.
6. Once the model download has finished, we have to added it to the following folder of the cloned repository: C:\Users\YOUR_NAME\stable-diffusion-webui\models\Stable-diffusion\.
7. Then we must run the file **webui** (windows batch file) which is inside the following folder: C:\Users\YOUR_NAME\stable-diffusion-webui.
   - Due to the fact that our pc has AMD 64, we can take an error: Torch is not able to use GPU.
8. Then we go to **webui-user** (windows batch file), and go to edit: We need to add the following:
   - git pull
   - set COMMANDLINE_ARGS= --skip-torch-cuda-test --precision full --no-half
9. Then we run the **webui-user** (windows batch file).
10. After the run, the url of the web-ui will open automatically or you can take it through the cmd window.
11. The wub-ui is as the following image:
12. ![web-ui](/images/stable diffusion webui.PNG)


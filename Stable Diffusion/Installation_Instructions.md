# Stable Diffusion installation instructions on windows machine

To run the stable diffusion model locally on our pc we must do the following:

1. First, we have to install git on our pc. We can download it from the following link: [git](https://git-scm.com/downloads)
2. Then we have to install the python 3.10.6 to our pc. We can download it from the following link: [python 3.10.6](https://www.python.org/downloads/release/python-3106/)
   - Don’t forget to click:  Add python XX to PATH.
3. Then we have to install the stable diffusion webui to our pc. We can clone the repository from the following link: [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
4. We go to the above link and copy the url. We open a **cmd** and run the following command:
   - git clone  https://github.com/AUTOMATIC1111/stable-diffusion-webui.
6. Then we have to install the model. We can download it from the following link: [stable diffusion model](https://huggingface.co/runwayml/stable-diffusion-v1-5)
   - From this page we download the v1-5-pruned-emaonly.ckpt.
7. Once the model download has finished, we have to added it to the following folder of the cloned repository: C:\Users\YOUR_NAME\stable-diffusion-webui\models\Stable-diffusion\

# nnU-net
The methods used are based on the public framework published at: https://github.com/MIC-DKFZ/nnUNet/tree/master/nnunetv2. Some customized trainers have been used. They were developed by Ander Elkoroaristizabal https://github.com/ander-elkoroaristizabal/nnunet-ms-segmentation.

# Added folders
* [results](https://github.com/cgalau97/nnUNet/tree/master/results): Contains figures and JSON with the metrics of the relevant experiments.
* [own_scripts](https://github.com/cgalau97/nnUNet/tree/master/own_scripts): Contains a [Python Notebook](https://github.com/cgalau97/nnUNet/blob/master/own_scripts/Data_Processing.ipynb) with the different pieces of code used to process the cases for the different experiments and a [couple of functions](https://github.com/cgalau97/nnUNet/blob/master/own_scripts/metrics_parser.py) to calculate the metrics necessary for the results.
* [CUSTOM](https://github.com/cgalau97/nnUNet/tree/master/nnunetv2/training/nnUNetTrainer/variants/CUSTOM): This folder contains the alternative trainer classes developed by Ander Elkoroaristizabal. In this file, I modified the epochs before stopping the training process to 30.
* Additionally, the file [nnUNetTrainer.py](https://github.com/cgalau97/nnUNet/blob/master/nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py) was modified so the computational cost was affordable. More details are explained in the memory.

  

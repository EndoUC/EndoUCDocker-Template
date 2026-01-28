# EndoUCDocker-Template

This document provides a template guide Docker submission instructions for the Endo-UC Challenge. (88IMPORTANT: One Task = One Docker Container**)

# Overview

- Same input images for all tasks
- One task per Docker container
- Inference only (no training)
- One CSV output per Task

# Input Structure

**Input files** 
When running your Docker container, input files will be mounted into a directory called **/input** that expects images

/input/images/
- img_001.png
- img_002.png

# Output Structure

**Output files**
When running your Docker container, an output directory will be mounted as a directory called /output

/output/results.csv

Results file (.csv file):

**Task 1**:  ```id,mes_score_0_3```

**Task 2**:  ```id,uceis_score```

**Task 3**:  ```id,caption```

# Docker Execution

 ```docker run -v /input:/input -v /output:/output ```


# Local Testing
 ```docker build -t endouc_submission  ```

 ## 🧠 Where to Implement Your Model

All participant code must be implemented inside:

src/inference.py

Participants are required to provide **inference code only**.

- The code must load the final trained model from `/checkpoints`
- The code must read images from `/input/images`
- The code must write predictions to `/output/results.csv`


 
 ```docker run -v example_input:/input -v example_output:/output endouc_submission ```





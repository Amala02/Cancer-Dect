# Cancer Dect
---
This is a model that can detect the probability of a cancerous cell from: 
- Brain scans
- Skin images
Currenlty, I am focusing on improving the accuracy of both skin cancer as well as brain cancer detection.
### About the Model
State-of-the-art YoLov8 Model used for training images of brain tumors. Dataset used can be found in the given kaggle link: [Click here](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset). 
[Skin cancer](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic).
The model makes use of instance segmented dataset for a better detection of cancerous cells. 
### Running the Model
You can try running the model and the app built using Streamlit in Python by installing the requirements.txt file. 
First, clone the repository in your local device. 
Ensure required modules are installed. 

Run the following code to start the streamlit app:

```
streamlit run cancer-detect.py
```

You're ready to go!

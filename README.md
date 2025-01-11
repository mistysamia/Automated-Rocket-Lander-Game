# Neural Network Rocket Game Training and Testing

This project involves training and testing a neural network model for the Rocket Game. Follow the steps below to set up the files, train the model, and integrate it with the game.

---

## Step 1: Dataset and File Setup

  **Unzip and Load Files**:  
      1. Unzip the `Dataset.csv.zip` file.
      2. Place the following files in the same folder:
        
        - `Dataset.csv`
        - `Neural_Network_Data_Train_Rocket_Game.ipynb`
        - `Neural_Network_Data_Test_Rocket_Game.ipynb`

## Step 2: Fnding Hyperparameters and Model Training 

**Train the Model**:  
   Run the training file for each hyperparameter obtained from MATLAB until the optimal hyperparameters are identified.

   ### Instructions for Training:
   1. Open `Neural_Network_Data_Train_Rocket_Game.ipynb`:
      - Update the **Import Libraries** section with the correct file path.
      - After execution, `NormaliseDataforTest.csv` and `Normalize.csv` files will be saved in the same folder.
   2. In the **Getting the Weights** section, save the updated weights:
      - Input layer weights: `weights_input_hidden`
      - Output layer weights: `weights_hidden_output`

   ### Find the Hyperparameters:
   1. Create a folder to find the Hyperparameters in **MATLAB**
   2. Use the `Normalize.csv` file generated in the previous step.  
      Place it in the same folder as `Neural_Network_Matlab_toolbox_Script.m`.
   3. Run `Neural_Network_Matlab_toolbox_Script.m` in MATLAB to determine optimal hyperparameters:
      - **Neuron Number**
      - **Lambda Value**
      - **Learning Rate**
      - **Momentum Value**
 > **Note**: Select the hyperparameters that provide the **Best Performance**, characterized by a **Lower RMSE Value** and achieved within **fewer epochs**.
---

## Step 2: Testing the Model

1. Open `Neural_Network_Data_Test_Rocket_Game.ipynb`:
   - Update the **Import Libraries** section with the path to `NormaliseDataforTest.csv`.
   - Provide the correct updated weights and Hyperparameters in the **Declaring Input Layer, Output Layer, Weights** section.

2. Run the file and validate the model:
   - Ensure the RMSE value for the test dataset is close to the RMSE value from the training dataset.  
   - If RMSE values are close, the model is trained successfully. Otherwise, repeat the training process.

---

## Step 3: Game Setup

1. **Download the Game File**:
   
     Download the required game files [here](https://drive.google.com/drive/folders/1bGAeSXdoBgnuq01MAQWKVm6vQPHrBNDo).

2. **Update the Neural Network Holder**:
   - Open the `NeuralNetHolder.py` file and update it with the provided code.
   - Replace the **Lambda Value** in the file with the one trained for your model.
   - Replace the **weights** with your updated weights from the training process.

---

## Final Steps

After completing all steps, run the game. The trained neural network should now effectively interact with the Rocket Game.

---

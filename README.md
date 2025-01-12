# Rocket Lander Game

This project focuses on designing, training, and testing a neural network model for the Rocket Lander Game, aiming to develop an automated system where the rocket can land autonomously by identifying and navigating to a safe landing area. The goal is to ensure the rocket lands without hitting unsafe terrain or obstacles.

The game will randomly generate a landing zone along with unsafe terrains, challenging the rocket to land safely. Initially, players will manually control the rocket to gather data by successfully completing the task. This data will then be used to train a neural network model capable of mimicking the task autonomously.

---
## Environment Setup
   
   - Download the required game files [here](https://drive.google.com/drive/folders/1bGAeSXdoBgnuq01MAQWKVm6vQPHrBNDo).
   - If the Operating System is **Mac** then, open the `GameLoop.py` file and update it with the provided code.

     
   - **Run the Setup**:  
        1.   Open the terminal.  
        2.  Navigate to the `Scripts` folder and activate the virtual environment:  
      ```bash
      .\activate
      cd ../../
      pip install -r .\requirements.txt
      python .\Main.py
        ```

## Dataset Collection     
  1. The game should be run.  
  2. Navigate to the `Data Collection` option.  
  3. The game must be won to collect the data.  
  4. Once the data collection is completed, a file named `ce889_dataCollection.csv` will be generated.  
      This file will contain the collected data with 4 columns. 


## Automated Game Execution
### Step 1: Dataset and File Setup

**Unzip and Load Files**:  
1. Unzip the `Dataset.csv.zip` file.  
2. Place the following files in the same folder:  
   - `Dataset.csv`  
   - `Neural_Network_Data_Train_Rocket_Game.ipynb`  
   - `Neural_Network_Data_Test_Rocket_Game.ipynb`  


### Step 2: Finding Hyperparameters and Model Training 

**Train the Model**:  
   Run the training file for each hyperparameter obtained from MATLAB until the optimal hyperparameters are identified.

   #### Instructions for Training:
   1. Open `Neural_Network_Data_Train_Rocket_Game.ipynb`:
      - Update the **Import Libraries** section with the correct file path.
      - After execution, `NormaliseDataforTest.csv` and `Normalize.csv` files will be saved in the same folder.
   2. In the **Getting the Weights** section, save the updated weights:
      - Input layer weights: `weights_input_hidden`
      - Output layer weights: `weights_hidden_output`
   3. In the **Normalization** section, save the min and max values for:  
      - `x-axis` and `y-axis`  
      - `x-vector` and `y-vector` 

   #### Find the Hyperparameters:
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

### Step 3: Testing the Model

1. Open `Neural_Network_Data_Test_Rocket_Game.ipynb`:
   - Update the **Import Libraries** section with the path to `NormaliseDataforTest.csv`.
   - Provide the correct updated weights and Hyperparameters in the **Declaring Input Layer, Output Layer, Weights** section.

2. Run the file and validate the model:
   - Ensure the RMSE value for the test dataset is close to the RMSE value from the training dataset.  
   - If RMSE values are close, the model is trained successfully. Otherwise, repeat the training process.

---

### Step 4: Game Setup

1. Open the `NeuralNetHolder.py` file and update it with the provided code.

2. Replace the **Lambda Value** in the file with the one trained for your model.
3. Replace the **weights** with your updated weights from the training process.
4. Replace the following values in the file:  
     - `self.min_vals` with the minimum values of `x_axis` and `y_axis`.  
     - `self.max_vals` with the maximum values of `x_axis` and `y_axis`.  
     - `self.min_vector` with the minimum values of `x_vector` and `y_vector`.  
     - `self.max_vector` with the maximum values of `x_vector` and `y_vector`.
5. Run the Game.
6. Navigate to the `Neural Network` option.  

---

### Final Steps

By completing the outlined steps, the data collection process will be finalized, and the automated rocket will successfully land by identifying the target area. This demonstrates the effectiveness of the trained neural network in achieving the desired outcome.

---

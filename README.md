NITT-PROJECT: AI-Based Thermal System Analysis
📋 Overview

This project was developed as part of the NIT-T Internship, focusing on the application of Artificial Intelligence and Machine Learning for thermal system modeling and efficiency prediction.
It integrates data-driven modeling, experimental dataset handling, and streamlit-based visualization for simulation and performance evaluation.

🚀 Features

📊 Dataset Generation & Preprocessing: Automatically cleans and structures experimental thermal data.

🧩 Machine Learning Model Creation: Builds regression models to predict performance metrics (e.g., efficiency).

🔍 Model Training & Evaluation: Uses advanced ML algorithms to ensure accurate predictions.

🧠 Real-time Prediction: Predicts outcomes using custom user inputs.

💻 Interactive Streamlit App: Provides a user-friendly interface for visualization and analysis.

🗂️ Project Structure
NITT-PROJECT/
│
├── data/                     # Experimental or generated datasets
├── model/                    # Saved ML models (.pkl files)
│
├── fake_input.py             # Generates sample test inputs
├── generate_dataset.py       # Creates or augments datasets
├── model_creator.py          # Defines and compiles ML model
├── predict.py                # Loads model and performs prediction
├── train_model.py            # Trains model and saves it
├── streamlit_app.py          # Streamlit dashboard for user interaction
│
├── requirements.txt          # Required Python libraries
├── README.md                 # Project documentation (this file)
└── .gitignore                # Files/folders to exclude from Git tracking

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yashgawande0905/NIT-T-INTERNSHIP.git
cd NIT-T-INTERNSHIP

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate       # For Windows
# OR
source venv/bin/activate    # For Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run streamlit_app.py

🧩 Technologies Used

Python 3.x

NumPy, Pandas, Scikit-learn – for data handling and ML

Streamlit – for creating an interactive dashboard

Matplotlib / Plotly – for visualization

Joblib / Pickle – for model saving and loading

📈 Workflow Summary

Dataset Preparation: Generate or collect experimental data.

Model Training: Train regression models using train_model.py.

Model Evaluation: Analyze metrics like RMSE, MAE, and Efficiency.

Prediction: Use predict.py for test cases.

Visualization: Launch streamlit_app.py to interact with data in real-time.

✨ Future Enhancements

Integrate deep learning (ANN/CNN) for complex heat transfer models.

Add automatic feature selection and hyperparameter tuning.

Include 3D visualization for temperature gradients.

🧑‍💻 Contributors

Yash Gawande
NIT Trichy Internship Project — AI & Thermal System Modeling

📬 Feel free to fork, open issues, or contribute!
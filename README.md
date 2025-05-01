# IRIS-flower-species-prediction.

🔍 𝐖𝐡𝐚𝐭 𝐈 𝐃𝐢𝐝:
𝐃𝐚𝐭𝐚 𝐏𝐫𝐞𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠: Cleaned and prepared data using libraries like Pandas and Scikit-learn.
𝐌𝐨𝐝𝐞𝐥 𝐁𝐮𝐢𝐥𝐝𝐢𝐧𝐠: Trained a RandomForestClassifier model to make predictions on the dataset.
𝐄𝐯𝐚𝐥𝐮𝐚𝐭𝐢𝐨𝐧: Evaluated model performance using accuracy, precision, and recall metrics.
𝐒𝐭𝐫𝐞𝐚𝐦𝐥𝐢𝐭 𝐀𝐩𝐩: Developed a Streamlit web app to make the model interactive and user-friendly.
𝐃𝐞𝐩𝐥𝐨𝐲𝐦𝐞𝐧𝐭 𝐨𝐧 𝐆𝐢𝐭𝐇𝐮𝐛: I’ve made the entire process available in a public GitHub repository, so you can clone it and try it for yourself!
💻 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬 𝐔𝐬𝐞𝐝:
Python (Pandas, Scikit-learn, NumPy)
Streamlit (for the web app)
GitHub (for version control and sharing the project)
👉 𝐖𝐡𝐲 𝐒𝐭𝐫𝐞𝐚𝐦𝐥𝐢𝐭? Streamlit allows me to create a fast, simple, and interactive front-end for any machine learning model without having to worry about complex web development frameworks. It's perfect for showcasing models and sharing results interactively.

**🌸 Iris Flower Species Prediction App**
A Streamlit web application that predicts the species of an Iris flower based on sepal and petal measurements using a pre-trained Random Forest model.

**🚀 Features**
Predicts Iris species (Setosa, Versicolor, Virginica) using sepal/petal dimensions.
Color-coded results for intuitive feedback:
✅ Setosa: Green (Success)
⚠️ Versicolor: Yellow (Warning)
🔴 Virginica: Red (Error)
User-friendly interface for inputting flower measurements.

**🧪 Installation**
Prerequisites
Python 3.8+
Git (for cloning)
**Steps**
1. Clone the repository
git clone https://github.com/vmaradhya2020/iris-species-prediction.git
cd iris-species-prediction
2. Install dependencies
pip install -r requirements.txt
3. Ensure model file exists
Place the trained model file iris_random_forest.pkl in the root directory.
4. Run the app
streamlit run app.py

**🧩 Usage**
Open the app in your browser.
Enter the following measurements:
Sepal Length
Sepal Width
Petal Length
Petal Width
Click "Predict Species" to see the result.

**📊 Model Training (Optional for Developers)**
Dataset
Uses the standard Iris dataset with 4 features:
Sepal Length
Sepal Width
Petal Length
Petal Width
Target: Species (Setosa, Versicolor, Virginica)
Training Process
Preprocessed using LabelEncoder for species labels.
Trained a RandomForestClassifier with hyperparameter tuning.
Achieved >95% accuracy on test data.

**📁 Project Structure**
iris-species-prediction/
├── app.py                  # Streamlit app code
├── iris_random_forest.pkl  # Pre-trained model
├── requirements.txt        # Dependencies
└── iris.csv                # Dataset

**🤝 Contributing**
Contributions are welcome!
Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Commit changes (git commit -m 'Add feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.
**📄 License**
This project is licensed under the MIT License – see the LICENSE file for details.

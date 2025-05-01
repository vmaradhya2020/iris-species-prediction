import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('random_forest_classifier_iris.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and description
st.title("🌸 Iris Flower Species Prediction App")
st.write("This app predicts the species of an Iris flower based on its sepal and petal measurements.")

# Input fields
st.header("Enter Flower Measurements")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.5, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

# Mapping for output decoding
class_mapping = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# Predict button
if st.button("Predict Species"):
    # Prepare input data in the correct format
    input_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get species name
    predicted_species = class_mapping.get(prediction, "Unknown")

    # Display result
    if predicted_species == "Setosa":
        st.success(f"✅ Predicted Species: **{predicted_species}**")
    elif predicted_species == "Versicolor":
        st.warning(f"⚠️ Predicted Species: **{predicted_species}**")
    else:
        st.error(f"🔴 Predicted Species: **{predicted_species}**")
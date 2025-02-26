import streamlit as st
import joblib  # For loading trained models
import plotly.express as px  # For visualization

# Load student names from a file (Modify as per your data file)
students = ["Alice", "Bob", "Charlie", "David"]  # Replace with real student names

# Define subjects, their model files, and the required input subjects
subject_models = {
    "Algorithms": {"model": "model_Algorithms.pkl", "inputs": ["Data structure", "Introduction Database", "Database programming"]},
    "Embedded System": {"model": "model_Embedded_System (1).pkl", "inputs": ["Digital engineering", "Operating system", "Internet of things"]},
    "Flutter": {"model": "model_Flutter.pkl", "inputs": ["Web 1", "Web 2", "Python"]},
    "Java Programming": {"model": "model_Java_Programming.pkl", "inputs": ["Java 1", "Programming C++", "Programming C"]},
    "Network Programming": {"model": "model_Network_Programming.pkl", "inputs": ["CCNA", "Linux", "Python"]},
    "Software Engineer": {"model": "model_Software_Engineer.pkl", "inputs": ["Capstone design", "Data structure", "Java 1"]}
}

# Streamlit UI
st.title("🎓 Student Grade Prediction App")

# Student selection
student_name = st.selectbox("🔹 Select Your Name", students)

# Subject selection
subject = st.selectbox("📚 Select Subject to Predict", ["Select a Subject"] + list(subject_models.keys()))

grades = []
if subject != "Select a Subject":
    required_inputs = subject_models[subject]["inputs"]
    st.subheader("Enter your grades for the required subjects:")
    for input_subject in required_inputs:
        grade = st.number_input(f"✏️ Enter your grade in {input_subject}:", min_value=0.0, max_value=150.0, step=0.1)
        grades.append(grade)

    # Predict button
    if st.button("📊 Predict Grade"):
        try:
            # Load the correct model
            model_file = subject_models[subject]["model"]
            model = joblib.load(model_file)

            # Make prediction
            input_data = [grades]  # Model expects a 2D array
            predicted_grade = model.predict(input_data)[0]

            # Display result
            st.success(f"✅ Predicted {subject} Grade: {predicted_grade:.2f}")

            # Visualization with Plotly
            subjects = required_inputs + [subject]
            grades.append(predicted_grade)
            fig = px.line(x=subjects, y=grades, markers=True, title="📈 Student's Performance Over Subjects")
            fig.update_xaxes(title_text="Subjects")
            fig.update_yaxes(title_text="Grades")
            st.plotly_chart(fig)
        
        except Exception as e:
            st.error(f"⚠️ Error loading model: {e}")

import streamlit as st
import joblib  # For loading trained model
import numpy as np

# Load student names from a file (Modify as per your data file)
students = ["Alice", "Bob", "Charlie", "David"]  # Replace with real student names

# List of subjects
subjects = [
    "Linux_Essentials", "Programming_C++", "Web_|", "Introduction_to_DataBase", 
    "Digital_Engineering", "Operating_System", "Web_||", "DataBase_Programming", 
    "Data_Structure", "CCNA_R&S_|", "Java_Programming_|", "Capstone_Design"
]

# Load the classification model
model_file = "model_Clustering.pkl"  # Replace with your model file
model = joblib.load(model_file)

# Streamlit UI
st.title("🎓 Student Predicting Specialization App")

# Student selection
student_name = st.selectbox("🔹 Select Your Name", students)

# Input fields for the required grades
grades = []
for subject in subjects:
    grade = st.number_input(f"✏️ Enter your grade in {subject}:", min_value=0.0, max_value=150.0, step=0.1)
    grades.append(grade)

# Predict button
if st.button("📊 Classify Student"):
    try:
        # Make prediction
        input_data = np.array([grades]).reshape(1, -1)  # Model expects a 2D array
        predicted_class = model.predict(input_data)[0]

        # Map classification to labels
        classification_result = "Software" if predicted_class == 0 else "Network"

        # Display result
        st.success(f"✅ Classification Result: {classification_result}")

        # Show career-related information
        if classification_result == "Software":
            st.subheader("🖥️ Software Development")
            st.write("""
            **1. What is Software?**  
            Software is a set of instructions that tells a computer what to do. It includes programs, apps, and operating systems.  

            **2. Fields of Work in Software:**  
            - **Software Development** – Writing programs and applications.  
            - **Web Development** – Building websites and web apps.  
            - **Mobile App Development** – Creating apps for phones and tablets.  
            - **Artificial Intelligence & Machine Learning** – Making smart programs.  
            - **Cybersecurity** – Protecting software from hackers.  
            - **Data Science** – Analyzing big amounts of information.  
            - **Cloud Computing** – Running software on the internet.  

            **3. Skills Required for Software Development:**  
            ✅ Programming (Python, Java, C++)  
            ✅ Problem-Solving & Debugging  
            ✅ Algorithms & Data Structures  
            ✅ Database Management (SQL, NoSQL)  
            ✅ Creativity & UI/UX Design  
            """)

        else:
            st.subheader("🌐 Networking")
            st.write("""
            **1. What is Networking?**  
            Networking connects computers and devices to share data, enabling communication across local and global networks.  

            **2. Fields of Work in Networking:**  
            - **Network Administration** – Managing and maintaining networks.  
            - **Cybersecurity** – Protecting networks from cyber threats.  
            - **Cloud Networking** – Managing online networks using AWS, Azure, etc.  
            - **Network Engineering** – Designing and setting up networks.  
            - **Telecommunications** – Managing mobile and internet services.  

            **3. Skills Required for Networking:**  
            ✅ Network Protocols (TCP/IP, DNS, HTTP)  
            ✅ Hardware Knowledge (Routers, Switches, Firewalls)  
            ✅ Security & Encryption  
            ✅ Cloud Networking (AWS, Google Cloud, Microsoft Azure)  
            ✅ Troubleshooting & Automation (Python, Bash)  
            """)

    except Exception as e:
        st.error(f"⚠️ Error loading model: {e}")

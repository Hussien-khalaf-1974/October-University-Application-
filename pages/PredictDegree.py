import streamlit as st
import joblib  # For loading trained models
import plotly.express as px  # For visualization

# Load student names from a file (Modify as per your data file)
# students = []  # Replace with real student names


#####################################################################################

names = """
Abram Magdy Fakeh Mansour
Ibrahim Abdullah Ibrahim Hassanein
Ibrahim Fawzy Ibrahim Hossam El Din
Ahmed Abu Al-Ela Hassan Abu Al-Ela
Ahmed Al-Sayed Saber Al-Badri
Ahmed Amin Ahmed Amin Abbas
Ahmed Haggag Kamal Shehata Muhammad
Ahmed Hossam Talaat Mohamed Ali
Ahmed Hassanein Mohammed Al-Saeed Hammad
Ahmed Refaat Sayed Muhammad
Ahmed Saeed Yassin Awis Youssef
Ahmed Shaaban Muhammad Sultan
Ahmed Salah Mohamed Ahmed
Ahmed Tariq Jaber Tolba Karash
Ahmed Abdel Fattah Abdo Abdel Fattah
Ahmed Ali Mohammed Al-Sayed Marzouq
Ahmed Emad for his quality
Ahmed Awad Ali Muhammad
Ahmed Fekry Ismail Sobh
Ahmed Kamal Salah Shalqani
Ahmed Mohamed Ahmed Mahmoud
Ahmed Muhammad Hussein Morsi
Ahmed Muhammad Suleiman Suleiman
Ahmed Mohamed Abdel Latif Al-Kholy
Ahmed Mohamed Fathi Mohamed Al-Sayed
Ahmed Mahmoud Ezz El-Din Mahmoud El-Faqih
Ahmed Hani Ahmed Youssef
Al-Mustafa Muhammad Al-Makawi
Arwa Mohamed Abdel Fattah Shehata Yehia
Ahmed Abdel Zaher's family only
Israa Mahmoud Mohamed Ahmed Abu Bakr
Islam Mahmoud Muhammad Austria
Asmma  Ibrahim Abdel Ghani Darwish
Asmma  Ali Mahmoud Abdel Ghani
Alaa Baha El Din Abbas Gharib Ahmed Al Sheikh
Amira Adel Mohammed Ahmed Al-Barai
Eman Ashraf Ali Ibrahim Ali
Eman Shaaban Awis Qarni
Eman Abdel-Ati Awad Abdel-Ati
Aya Muhammad Hashem Ahmed
Basil Muhammad Sayed Muhammad Ahmed
Bothaina Walid Hassan Mahdi Abdul Rahman
Basmala Ahmed Mohammed Abdel Rahman
Basmala Sayed Shawky Youssef
Tasabeah Muhammad Fathi Othman Abdel Aal
Taqa Jamal Abdul Karim Mustafa
Gana Essam Mohamed Omran
Jana Moamen Mohamed Mohamed Abdel Wahab
Jawaher Abdel Fattah Mahmoud Abdel Hamid Hussein
Hbiba Hassan Mohamed Abdel Fattah
Hbiba Sabry Hussein Abdel Sayed Ahmed
Hbiba Adel Mohammed Al Daker
Hbiba Essam Ahmed Mohamed
Hbiba Amr Ahmed Ahmed Al-Zanati
Habiba Mohamed Afify Slam
Habiba Nader Mustafa Mahmoud Ahmed Issa
Hassan Hosni Abdel Fattah Hassan Mohamed Abu Al-Ghaib
Hassnaa Hossam El-Din Hussein Junaidi Hussein
Hussein Khalaf Hussein Abbas
Hussein Alaa El-Din Muhammad
Kholoud Abdul Rahman Abdul Fadil Ahmed Ibrahim
Doaa Suleiman Sayyed Suleiman
Donia Emad Saeed Mohamed Ismail
Dina Hani Nour El Din Abdullah El Sayed
Dahab Tariq Abdel Nafe Abdel Hamid
Dina Ayman Abdel Hamid Ahmed Hammad
Raul Robert Ador Sarri
Rehab Sayed Mohammed Sayed
Roqaya Ahmed Mahmoud Abdel Qader Abdel Aal
Ramadan Muhammad Ramadan Abdel Jawad
Rana Khaled Mohammed Abdel Hamid
Reem Ramadan Al-Dessouki Mohamed Abu Zaid
Reham Hassan Mohammed Al-Sheikh
Ziad Hassan Muhammad Maarouf
Ziad Abdel Fattah Jamal Al-Din Musleh
Sarah Sayed Ali Hassouna Saleh
Salma Mohsen Mohammed Ahmed Al-Attar
Somia Ramadan Ahmed Nobi Dawi
Sondos Ahmed Hussein Abdel Latif Hussein
Sohair Hani Mohammed Abdullah
Syed Tmam Syed Tmam
Saif Abdel Hamid Musa Diab Mohammed
Saif Mohamed Fathy Abdel Wahab Abdel Hadi
Saif Mustafa Naji Sayed
Saif Mustafa Yahya Muhammad
Sahed Sayed Abdel Aal Sayed Ali
Sahed Mahmoud Abdullah Ziad
Tariq Rajab Khamis Faraj
Tariq Mahmoud Farag Abdel Aziz
Abdul Rahman Ahmed Basem Ali Ghait
Abdul Rahman Ashraf Mohammed Qandeel
Abdul Rahman Gad Yahya Abdel Shafi
Abdul Rahman Hassan Metwally Mohamed Mustafa
Abdel Rahman Hamada Mohamed Ahmed
Abdul Rahman Shaaban Helmy Moawad
Abdul Rahman Tariq Hassanein Hassanein
Abdul Rahman Gharib Hassan Gharib
Abdul Rahman Mohammed Abdul Majeed Sayed
Abdul Rahman Mahmoud Mahmoud Gamal Farag
Abdullah Ahmed Sayed Ahmed
Abdullah Saeed Hassan Siddiq
Abdullah Shaaban Mustafa Abu Jalila
Abdullah Omar Nabawi Omar
Abdullah Mustafa Al-Sayed Abdul Majeed
Abdul Wahab Mohammed Abdul Wahab Abdul Karim
Ezz El-Din Abdel Hamid Fathy Abdel Hamid
Ali Imam Ali almursi
Ali Ibrahim Juma Mahmoud
Ali Al-Din Omar Mustafa Hassan
Ali Hussein Abdel Nabi Sayed
Ali Radhi Hamdan Mohammed Al-Sayed
Ali Abdel Hamid Abdel Aleem Ali
Ali Muhammad Ali Fahmy
Ali Yasser Afify Al-Hanafi
Omar Ahmed Taha Suleiman
Omar Ahmed Ali Abdel-Al
Omar Ayman Tab Abdel Aziz
Omar Tamer Saad Ibrahim Khedr
Omar Adel Abdel Hamid Ahmed Abdullah
Omar Abdel Aati Ahmed Ali
Omar Abdel Azim Mohammed Abdel Jalil Abdel Aleem
Omar Mohammed Tahamy Al-Shafei Hassanein
Omar Mahmoud Ali Taher
Amr Rady Abdel Fadil El Sayed
Ahmed Ali Abdul Qader Ali Muhammad Al-Tajjar
Fatima Al-Zahraa Mohammed Abdul-Jaid Mohammed
Fatima Eid Antar Abdel Nabi
Philopater Michael Nagi Rizkallah Ghali
Catherine Medhat Thumari Ajaybi
Karim Ahmed Gomaa Muhammad
Karim Ahmed Abdel Karim Mustafa
Karim Muhammad Farouk Abboud
Kyrollos Ashraf Amin Semaan
Marcelino Ihab Wagdy Adeeb
Marcelino Shafiq Shaker Smart
Mazen Sami Arafa Mustafa Mousa
Mazen Ali Ismail Mohammed Ismail
Mazen Mustafa Abdel Aziz Mahmoud
Michael Sameh Ibrahim Abdullah
Mohamed Ahmed Shukry Ahmed Ahmed
Muhammad Ahmed Ali Behairy
Mohamed Ahmed Mohamed Abdel Hamid
Muhammad Osama Fayez Muhammad Shuaib
Muhammad Hatem Muhammad Sadiq
Muhammad Khaled Zuhri Mahfouz
Muhammad Rabie Fathi Hassan Hassan
Muhammad Shaaban Sayed Taha
Mohamed Sabry Abbas El Sayed Singer
Mohamed Salah Awad Allah Al-Ruby
Mohamed Diaa Mohamed Reda Mohamed Elsamanoud
Muhammad Adel Hamida Ali
Muhammad Adel Muhammad Hassan
Muhammad Ali Harun Ali Ahmed
Mohammed Imad Mohammed Samer Al-Ash
Mohamed Fawzy Hanfy Bakkar
Mahmoud Zain Al-Abidin Abdullah Mohammed Mohammed
Mahmoud Abdel Aziz Abdel Ghani Farhat
"""

students = [name.strip() for name in names.split("\n") if name.strip()]

#####################################################################
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

import streamlit as st
import joblib  # For loading trained model
import numpy as np

# Load student names from a file (Modify as per your data file)
# students = ["Alice", "Bob", "Charlie", "David"]  # Replace with real student names
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

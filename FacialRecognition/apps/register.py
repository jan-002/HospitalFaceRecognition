

import streamlit as st
import sqlite3
conn = sqlite3.connect("face.db",check_same_thread=False)
cur = conn.cursor()

def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS Records(Name TEXT(150), HomePhone TEXT(10), AltPhone TEXT(15), Email TEXT(200), Address TEXT(200), City TEXT(100), State TEXT(100),
    Pincode TEXT(10), DOB date, age int, Gender TEXT(6), MaritalStatus TEXT(50),PatientEmployerName TEXT(150), EmploymentStatus TEXT(150),EmergencyContactName TEXT(150),
    RelationPatient TEXT(200), EmergencyAddress TEXT(200), EmergencyPhone TEXT(15), PrimaryInsurance TEXT(100), PatientSubPolicyHolderPri TEXT(5),
    SecondaryInsurance TEXT(100), PatientSubPolicyHolderSec TEXT(5), SubPolicyHolder TEXT(5), RelToPatient TEXT(150), PersonAddress TEXT(200), PersonDOB date, 
    PersonEmployer TEXT(150), PersonWorkPhone TEXT(15));""")

def add_data(name, hphone, alphone, email, address, city, state, pincode, dob, age, gender, marital_status,patemp, emp_status, emcontact, relpatient, emaddress, emphone, primary_insurance, sub_pol_pri, secondary_insurance, sub_pol_sec, sub_pol_holder, rel_to_patient,per_address, per_dob, his_her_employer, workphone):
    cur.execute("""INSERT INTO Records (Name, HomePhone, AltPhone, Email, Address, City, State, Pincode, DOB , age , Gender , MaritalStatus,PatientEmployerName, EmploymentStatus ,EmergencyContactName,
    RelationPatient, EmergencyAddress, EmergencyPhone, PrimaryInsurance, PatientSubPolicyHolderPri ,SecondaryInsurance , PatientSubPolicyHolderSec , SubPolicyHolder , RelToPatient , PersonAddress , PersonDOB, 
    PersonEmployer, PersonWorkPhone) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (name, hphone, alphone, email, address, city, state, pincode, dob, age, gender, marital_status,patemp, emp_status, emcontact, relpatient, emaddress, emphone, primary_insurance, sub_pol_pri, secondary_insurance, sub_pol_sec, sub_pol_holder, rel_to_patient,per_address, per_dob, his_her_employer, workphone))
    conn.commit()

def view_data():
    cur.execute("SELECT * FROM Records")
    data = cur.fetchall()
    return data

def delete_data():
    cur.execute("DELETE FROM Records")
    conn.commit()

def app():
    
    st.title("Register New User")
    st.markdown("Please fill out all fields")
    create_table()

    picture = st.camera_input("Register Face Image")
    # run  = True
    # i = 1
    # while run:
    ctr1 = 0
    ctr2 = 0
    ctr3 = 0
    ctr4 = 0
    ctr5 = 0
    vctr1 = 0
    vctr2 = 0
    vctr3 = 0
    vctr4 = 0
    with st.form(key="myForm"):
            name = st.text_input(label="Patient's Full Name")
            if picture:
                str = "images/" + name + ".jpg"
                with open (str,'wb') as file:
                    file.write(picture.getbuffer())
            hphone = st.text_input(label="Patient's Home Phone Number", max_chars=8)
            alphone = st.text_input(label="Alternate Phone Number",max_chars=10)
            email = st.text_input(label="E-Mail Address")

            if not name or not hphone or not alphone or not email:
                ctr1 = 1
            if not hphone.isdigit() and not alphone.isdigit() and not '@' in email and not len(hphone)==8 and not len(alphone)==10:
                vctr1 = 1
            

            cols = st.columns(4)
            for i, col in enumerate(cols):
                if i==0:
                    address = col.text_input(f'Address', key=i)
                elif i==1:
                    city = col.text_input(f'City', key=i)
                elif i==2:
                    state = col.text_input(f'State', key=i)
                elif i==3:
                    pincode = col.text_input(f'Pincode', key=i)

            if not address or not city or not state or not pincode:
                ctr2 = 1
            if not pincode.isdigit() and len(pincode)==6:
                vctr2 = 1

                

            dob = st.date_input(label="Date Of Birth")
            age = st.slider(label="Age", min_value=0, max_value=100, step=1 )
            gender = st.radio("Gender",('Male', 'Female', 'Other'))
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            marital_status = st.radio("Marital Status",('Married', 'Single', 'Divorced', 'Widowed'))
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

            


            patemp = st.text_input(label="Patient's Employer")
            emp_status = st.radio("Employment Status",('Full Time', 'Part Time', 'Unemployed', 'Retired','Student'))

            if not dob or not age or not gender or not marital_status or not patemp or not emp_status:
                ctr3 = 1


            emcontact = st.text_input(label="Emergency Contact Name")
            relpatient = st.text_input(label="Relationship to Patient")
            emaddress = st.text_input(label="Address")
            emphone = st.text_input(label="Phone Number",max_chars=10)


            st.markdown("Insurance Information")

            col1, col2 = st.columns(2)
            
            with col1:
                primary_insurance = st.text_input(label="Primary Insurance")
                sub_pol_pri = st.radio("Patient is a Subscriber/Policy Holder",('Yes', 'No'),key=1)


            with col2:
                secondary_insurance = st.text_input(label="Secondary Insurance")
                sub_pol_sec = st.radio("Patient is a Subscriber/Policy Holder",('Yes', 'No'),key=2)

            if not emcontact or not relpatient or not emaddress or not emphone or not primary_insurance or not sub_pol_pri or not secondary_insurance or not sub_pol_sec:
                ctr4 = 1

            if not emphone.isdigit() and not len(emphone)==10:
                vctr3 = 1


            st.markdown("Insured Information (if other than patient) - Aunthentication with face recognition")

            sub_pol_holder = st.text_input(label="Subscriber/Policy Holder Name", key=3)
            rel_to_patient = st.text_input(label="Relationship to Patient", key=4)
            per_address = st.text_input(label="Address", key=5)
            per_dob = st.date_input(label="Date of Birth")
            his_her_employer = st.text_input(label="His/Her Employer", key=6)
            workphone = st.text_input(label="Work Phone Number", key=7,max_chars=10)

            if not sub_pol_holder or not rel_to_patient or not per_address or not per_dob or not his_her_employer or not workphone:
                ctr5 = 1
            if not workphone.isdigit() and not len(workphone)==10:
                vctr4 = 1

            

            submit = st.form_submit_button("Submit")


            if submit == True:
                if ctr1==1 or ctr2==1 or ctr3==1 or ctr4==1 or ctr5==1:
                    # i = i + 1
                    st.warning("Please refresh and fill out all fields")
                elif vctr1 == 1 or vctr2 == 1 or vctr3 == 1 or vctr4 == 1:
                    st.warning("Please refresh and fill out all fields correctly! \n Phone numbers and Email addresses must be valid")
                else:
                    # run = False
                    add_data(name, hphone, alphone, email, address, city, state, pincode, dob,age, gender, marital_status,patemp, emp_status, emcontact, relpatient, emaddress, emphone, primary_insurance, sub_pol_pri, secondary_insurance, sub_pol_sec, sub_pol_holder, rel_to_patient,per_address, per_dob, his_her_employer, workphone)
                    conn.commit()
                    st.success("Successfully submitted")
                    # delete_data()

    # result = view_data()
    # st.write(result)

   





   
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st
import pandas as pd
import webbrowser as wb

import sqlite3
conn = sqlite3.connect("face.db",check_same_thread=False)
cur = conn.cursor()




def view_data(name):
    column = "Name"
    # select = ("PatientSubPolicyHolderPri", "PatientSubPolicyHolderSec")
    cur.execute(f'SELECT PatientSubPolicyHolderPri, PatientSubPolicyHolderSec FROM Records where '+column+'=?',(name,))
    data = cur.fetchone()
    # cur.execute("SELECT * FROM Records")
    # data = cur.fetchall()
    return data




def app():
    st.title("Online Billing")
    options = st.multiselect('Services',['Consultation - Rs 2500', 'Equipment - Rs 750', 'Medical Administration - Rs 1000', 'Medical Services - Rs 1500', 'Medications - Rs 1250'])
    #cost = {'Consultation - Rs 2500': 2500, 'Equipment - Rs 750':750, 'Medical Administration - Rs 1000':1000, 'Medical Services - Rs 1500':1500, 'Medications - Rs 1250':1250}
    #total_bill = 0
    save = st.button("Done")
    if save:
        # print(options)
        # for i in options:
        #     total_bill = total_bill + cost[i]
        # st.info(f'The total bill is:  {total_bill}')
        st.write("Click the checkbox below to validate for insurance")

    
    run = st.checkbox('Scan Face')
    if run:
        st.markdown("This may take a while, kindly wait")
    FRAME_WINDOW = st.image([])
    path = 'images'
    images = []
    personName = []
    myList = os.listdir(path)
    # print(myList)

    for cu_img in myList:
        current_img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_img)
        personName.append(os.path.splitext(cu_img)[0])
    # print(personName)

    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = faceEncodings(images)
    print("Encoding Complete")

    camera = cv2.VideoCapture(0) #cv2.VideoCapture(1) if using external webcam

    while run:
        ret, frame = camera.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = personName[matchIndex]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(frame, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                result = view_data(name)
                primin = result[0]
                secin = result[1]
                total_bill = 0
                cost = {'Consultation - Rs 2500': 2500, 'Equipment - Rs 750':750, 'Medical Administration - Rs 1000':1000, 'Medical Services - Rs 1500':1500, 'Medications - Rs 1250':1250}
                costList=[]
                opt = []
                for i in options:
                    x = i.rfind("-")
                    opt.append(i[0:x])
                    print(x)
                    costList.append(cost[i])
                    total_bill = total_bill + cost[i]
                df = pd.DataFrame({'Service': opt,'Cost': costList,})
                df.index = df.index+1
                st.write(df)
                st.warning(f'The total bill is:  {total_bill}')

                if (primin.lower() == 'no' and secin.lower() == 'no'):
                    st.success(f"No insurance coverage, total bill: {total_bill}")
                elif (primin.lower() == 'yes' and secin.lower() == 'no'):
                    total_bill = total_bill*0.5
                    st.success(f"Total bill after Primary insurance coverage: {total_bill}")
                elif (primin.lower() == 'yes' and secin.lower() == 'yes'):
                    total_bill = 0
                    st.success(f"Total bill after Primary and Secondary insurance coverage: {total_bill}")
                else:
                    st.error("Invalid Insurance Input. Please Register again")
                run = False
                break
        
        FRAME_WINDOW.image(frame)

    button2 = st.button("Proceed to payment")
    if button2:
        str = os.getcwd()
        str = str.replace(os.sep,'/')
        print(str)
        filename = f'{str}/payment.html'
        wb.open(filename)
        
            
# file:///C:/Users/janan/OneDrive/Desktop/WEBDEV/FacialRecognition/apps/payment.html


    



import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
import streamlit as st
import sqlite3
conn = sqlite3.connect("face.db",check_same_thread=False)
cur = conn.cursor()

# def delete_data():
#     cur.execute("DELETE FROM Records")
#     conn.commit()

def view_data(name):
    column = "Name"
    cur.execute(f'SELECT * FROM Records where '+column+'=?',(name,))
    data = cur.fetchone()
    # cur.execute("SELECT * FROM Records")
    # data = cur.fetchall()
    return data

attributeList = ['Name', 'Home Phone', 'Alternate Phone', 'Email', 'Address', 'City', 'State', 'Pincode', 'Date Of Birth', 'Age', 'Gender', 'Marital_status','Patient Employer', 'Employement_Status', 'Emergency Contact', 'Relation To Patient', 
'Emergency Address', 'Emergency Phone', 'Primary insurance', 'Primary Insurace - Subscriber/Policy Holder', 'Secondary Insurance', 'Secondary Insurace - Subscriber/Policy Holder', 'Subsriber/Policy Holder Name', 'Subsriber Relation_to_patient',
'Subsriber_address', 'Subscriber Date Of Birth', 'Subscriber Employer', 'Subscriber Workphone']

def app():
    st.title("Hospital Records")
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

    camera = cv2.VideoCapture(0)



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
                # if name.casefold() != '.jpg':
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.rectangle(frame, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                    print(name)
                    result = view_data(name)

                    recordList=[]
                    for i in range (1,29):
                        recordList.append(f'{result[i]}')

                    df = pd.DataFrame({
                        'first column': attributeList,
                        'second column': recordList,
                    })
                    df.index = df.index+1
                    st.write(df)
                    # st.write(result)
                    # delete_data()
                    # result = view_data(name)
                    # st.write(result)
                    run=False
                    break

        
        FRAME_WINDOW.image(frame)

            



    



# HospitalFaceRecognition
Hospital and Medical Insurance Management Web - App based on Face Recognition

FIRST PLEASE INSTALL THE FACE RECOGNITION MODULE: (Was not able to upload an already cloned github file onto my repository, Sorry for the inconvinience)

STEP 1:
Clone the following github repository: github.com/ageitgey/face_recognition and store it in a folder (say facerecog).

STEP 2:
In the command line, open the folder (facerecog) and create a virtual environment by using the command 'virtualenv myvenvpy'.Here, myvenvpy is the virtual environment name, you can give any name. If the virtual environment is not installed, install it uing pip install virtualenv.

STEP 3:
To activate the virtual environment, go to  the Scripts folder in the virtual environment (myvenvpy/Scripts). Then go to activate (.\activate). If you do this for the first time, you may get an error, paste the following code 'Set-ExecutionPolicy RemoteSigned' when you are in the Scripts folder and hit enter, it will work. Now we have created the virtual environment.

STEP 4:
Go back to the cloned facial_recognition folder and enter 'python setup.py install' (64 bit of python is must). Once this is done , enter pip install cmake. Once done enter 'python setup.py install' again. This will take a lot of time, but once done, do a pip freeze and check if dlib, face-recognition , etc are installed.

STEP 5:
If any module is to be imported, go to the virtual environment in the facerecog folder and perform a pip install
Eg: Pip install streamlit


Steps to follow for execution of the web app:
Step 1
Go to the FacialRecognition folder in the github repository and open its files in a code editor( I used Visual Studio Code )

Step 2
Change the interpreter. Hit Ctrl + Shift + P in VS Code. Choose select interpreter:python >> Enter interpreter path. Open the Scripts folder (HospitalFaceRecognition >> facerecog >> myvenvpy >> Scripts >> python

Step 3
Run FacialRecognition >> app.py using the selected interpreter.
Type 'streamlit run app.py' on the terminal. This will open the streamlit app in the browser.

Notes:
After every registration, go back to the code editor and delete the '.jpg' file in images and refresh the app on the browser to proceed smoothly.
After every payment success, run the demo.py file. This will give the order id as output. Copy it, and paste it as order id in the payment.html file.

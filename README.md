# OCR-Flask
Setup python environment: 
1)sudo apt install -y python3-pip
2)sudo apt install tesseract-ocr 
3)sudo apt install libtesseract-dev
                        
Create a virtualenv and workon it: 
1)sudo apt install python3-venv
2)python3 -m venv envname-env
3)source envname-env/bin/activate
                       
Install the required library: 
1)sudo apt-get install python-pip  
2)pip install numpy Pillow pytesseract datetime datefinder Image
                            
Install Flask: sudo pip install flask                            

Run the application by running the app.py: python app.py

To test we can use an app like Postman. Open Postman, select POST method and enter URL: localhost:5000/upload. Under Body enter KEY as file and VALUE as any image and click on send.

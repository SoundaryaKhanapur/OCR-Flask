# OCR-Flask
Setup python environment: sudo apt install -y python3-pip
                        : sudo apt install tesseract-ocr 
                        : sudo apt install libtesseract-dev
                        
Create a virtualenv and workon it: sudo apt install python3-venv
                                 : python3 -m venv envname-env
                                 : source envname-env/bin/activate
                       
Install the required library: sudo apt-get install python-pip  
				                    : pip install numpy Pillow pytesseract datetime datefinder Image
                            
Install Flask: sudo pip install flask                            

Run the application by running the app.py in ocr_server folder: python app.py

To test we can use an app like Postman. Open Postman, select POST method and enter URL: localhost:5000/upload. Under Body enter KEY as file and VALUE as any image and click on send.

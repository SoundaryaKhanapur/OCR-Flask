try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re
import datefinder

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))

    text = re.sub('[-\+]', '', text)
    striplines=text.splitlines()
    store = ''
    store = store + striplines[0] + striplines[1] + striplines[2]
    sub = ["Amt:","Total Am[a-z]","Payable Am[a-z]*","Grand Total","Gross Total","Sale","[A-Z][a-z]* Total","Total"]
    array_length = len(sub)
    for  i in range(array_length) :
        sub1=(sub[i])
        res = [i for i in striplines if sub1 in i]
        if(res):
            res1= re.findall('\d*\.?\d\d',str(res))
            x = 0
            amt = 0
            for result in res1:
                y=float(result)
                if(y>x):
                    amt=y
                    x=y
            if str(amt) not in store:
                store = store + ("\nAmount: "+str(amt))
            store = store + '\n'
    sub1 = ["Date","DATE","Transaction Time","Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sep","Oct","Nov","Dec",]
    array_length = len(sub1)
    for  i in range(array_length) :
        sub2=(sub1[i])
        res11 = [i for i in striplines if sub2 in i]
        if(len(res11)!=0):
            datestr=str(res11)
            matches = datefinder.find_dates(str(datestr))
            for match in matches:
                store = store + str(match) + "\n"


    
    x = re.findall("Restaurant|Hotel|BAKERY|Bakery|Table|Cafe|Tip|Waiter|Cafe|Eat|Mandi|Pizza|Burger|Veg|Non-Veg|House|Food Court|A.C|Non-A.C|Coffee Shop|Caterers|Vegeterian|Resto|Frankie|Cuisine|Ice-Cream Outlet|Take Away|Fast Food|Navtara", text)
    y = re.findall("Supermarket|Market|Stores|General|Goods|Sold|No Return|NO EXCHANGE|Grocieries|Grocery", text)
    z= re.findall("Petrol|Diesel|Gas",text)
    if (x):
        store = store + "FOOD BILL"
    elif(y):
        store = store + "GROCERIES BILL"
    elif(z):
        store = store + "FUEL BILL"
    else:
        store = store + "\nSorry couldn't detect, please click the image again"
        
    return store



import base64

with open("123.png",'rb') as fs:
    open("456.txt","wb").write(base64.b64encode(fs.read()) )
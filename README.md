# PDFGenerator
A Tool to create a protected pdf with watermark

## code example:

> python ./pdfGenerator.py -f "firstname" -u "username" -p "password" -o "outputfile" e "ebcryptionpassword" -t "templatefile" 

## Parameters:
```
-f, --firstname: The user first name is used as part of the greeting message
-u, --username: The actual username used for authintication
-p, --password: The user's password used for authintication
-o, --outputFileName: The result output pdf encrypted file
-e, --encryptionPassword: The encryption password used to protect the PDF file
-t, --templateFile: The template PDF file which has the organization logo and watermark
```

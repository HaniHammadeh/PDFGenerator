from PyPDF2 import PdfFileReader, PdfFileWriter
import fpdf
import argparse

def greeing(pdf: fpdf.FPDF, text: str)-> None:
    pdf.set_font('Arial', 'B', 16)
    pdf.set_x(20)
    pdf.cell(100, 120, text)

def setBodyText(pdf: fpdf.FPDF, message: list[str]) -> None:
    pdf.set_font('Arial', 'B', 10)
    i=1
    for msg in message:
        pdf.set_x(20)
        pdf.cell(100,210+10*i,msg)
        i+=1

def setUserNamePassword(pdf: fpdf.FPDF, usernamepass: list[str]) -> None:
    pdf.set_font('Arial', 'B', 10)
    i=1
    for msg in usernamepass:
        pdf.set_x(20)
        pdf.cell(100,240+10*i,msg)
        i+=1

def addPage(overlayPdfFileName: str, greetingMessage: str, message, usernamepass: list[str]) -> str:
    # define the ovelay pdf file to be as a base pdf we add a water mark
    # create a blank pdf file
    pdf = fpdf.FPDF()
    pdf.add_page()
    greeing(pdf, greetingMessage)
    setBodyText(pdf,message=message)
    setUserNamePassword(pdf,usernamepass=usernamepass)
    pdf.output(overlayPdfFileName, 'F')
    pdf.close()
    return overlayPdfFileName
def wtareMarkFile(srcTemplateFile: str, overlayFileName: str, encryptionPassword) -> None:
    # read the template watermark
    pdf_reader=PdfFileReader(srcTemplateFile)
    pdf_template_page=pdf_reader.getPage(0)
    # read the  source file (without watermark)
    pdf_reader_2=PdfFileReader(overlayFileName)
    pdf_overlay_page=pdf_reader_2.getPage(0)
    # merge the two pdf files
    pdf_template_page.mergePage(pdf_overlay_page)
    pdf_writer=PdfFileWriter()
    pdf_writer.add_page(pdf_template_page)
    
    pdf_writer.encrypt(encryptionPassword)
    with open(overlayFileName,'wb') as pf:
        pdf_writer.write(pf)

def main():
    
    
    parser = argparse.ArgumentParser(
                    prog = 'pdfGenerator',
                    description = 'This tool will create an encrypted pdf file for password sharing',
                    epilog = 'Enjoy! using the tool.')
    parser.add_argument('-f','--firstname',action='store', type=str,required=True,help="The user first name is used as part of the greeting message")
    parser.add_argument('-u','--username',action='store', type=str,required=True,help='The actual username used for authintication')
    parser.add_argument('-p','--password', action='store', type=str, required=True,help='The user password used for autintication')
    parser.add_argument('-o','--outputFileName', action='store', type=str, required=True,help='The result output pdf encrypted file')
    parser.add_argument('-e','--encryptionPassword', action='store', type=str, required=True, help='The encryption password used to protect the PDF file' )
    parser.add_argument('-t','--templateFile', action='store', type=str, required=True,help='The template PDF file which has the organization logo and watermark' )

   
    args = parser.parse_args()
    message=['Nobody else should know your password, not even people you trust.',
        'That is the only way you can be sure only you have access to your account']
    usernamepass=[f'Your Username is : {args.username}', f'Your Password is :  {args.password}']
    greeting=f'Dear {args.firstname}'
    srcFile=addPage(args.outputFileName,greetingMessage=greeting, message=message,usernamepass=usernamepass)
    templateFile=args.templateFile
    encpass=args.encryptionPassword

    wtareMarkFile(templateFile,srcFile,encpass)
    

if __name__== '__main__':
    main()


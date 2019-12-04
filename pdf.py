from PyPDF2 import PdfFileWriter, PdfFileReader


def pdf_split(pdf_path):
    """Open source tool form github
    https://gist.github.com/simonneutert/26350512af1ab2cd6acacf03d881c80d"""
    pdfdoc = pdf_path  # Examples: "C:/Users/Top/Desktop/__shmython__/name.pdf"

    inputpdf = PdfFileReader(open(pdfdoc, "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("C:/Users/Top/Desktop/shmython/[%s].pdf" % i, "wb") as outputStream:
            output.write(outputStream)

import img2pdf
pdf = img2pdf.convert(['heart.png', 'instagram.png'])
f1 = open("myreport.pdf", "wb")
f1.write(pdf)
f1.close()

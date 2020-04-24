import numpy as np
import pytesseract
from PIL import Image

print('step 0 initialize tesseract')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
print('step 1')
img = Image.open('ms-2.JPG').convert('LA')
print('step 2')
text = pytesseract.image_to_string(img)
print('step 3')
print(text)
print('step 4')
#dlist = text.split()
#print(dlist)

dlister = text.split()
print(type(dlister))

for i in range(len(dlister)):
    dlister[i] = dlister[i].lower()
print(type(dlister))
dlist = list(dlister)
print(dlist)
print(type(dlist))

print('step 5')
#t = np.array(dlist)
#print(t)
print('step 6 -marks')
#x = np.where(t == 'NINETY')
#y = np.where(t == 'EIGHTY')
#z = np.where(t == 'SEVENTY')
#print(x)
#print(y)
#print(z)
#def filmrkss(string, substrmkss):
#    return [dlist.index(str) for str in string if
 #            any(sub in str for sub in substrmkss)]
substrmkss = ['seventy', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79']

#def filmrkse(string, substrmkse):
 #   return [dlist.index(str) for str in string if
  #           any(sub in str for sub in substrmkse)]
substrmkse = ['eighty', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89']

#def filmrksn(string, substrmksn):
 #   return [dlist.index(str) for str in string if
  #           any(sub in str for sub in substrmksn)]
substrmksn = ['ninety', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

submarks = ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79','80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
#svnty = filmrkss(dlist,substrmkss)
#eigty = filmrkse(dlist,substrmkse)
#ninty = filmrksn(dlist,substrmksn)
#print(svnty)
#print(eigty)
#print(ninty)

#if len(svnty) == 0 and len(eigty) == 0 and len(ninty) == 0:
 #   print("sorry you are not eligible or try uploading good quality image again")

print('step 7 -subjects')

substrp = ['phys', 'sics', 'physics', 'hysi']
substrc = ['chemistry', 'chem', 'mistry']
substrm = ['mathe', 'math', 'mathematics']

def filterp(string, substrp):
    return [dlist.index(str) for str in string if
             any(sub in str for sub in substrp)]

def filterc(string, substrc):
    return [dlist.index(str) for str in string if
             any(sub in str for sub in substrc)]

def filterm(string, substrm):
    return [dlist.index(str) for str in string if
             any(sub in str for sub in substrm)]

p = np.array(filterp(dlist, substrp))
print(p)
c = np.array(filterc(dlist, substrc))
print(c)
m = np.array(filterm(dlist, substrm))
print(m)

#check if mpc is null or not

if len(m) == 0 and len(p) == 0 and len(c) == 0:
    print("unable to read image: please upload a clearer/good quality image -ml-cnn")


print(type(m))
print('step 8')
pval = list(range(3))
cval = list(range(3))
mval = list(range(3))
gplist = list(range(0))
gclist = list(range(0))
gmlist = list(range(0))
#print(gplist)
#print(gclist)
#print(gmlist)
#print('gc gp gm list values upside')
if len(p) == 0:
    print("PHYSICS NOT FOUND")
elif len(p) > 0:
    for i in range(3):
        pval[i] = 1+int(p)+i
        gplist.append(dlist[1+int(p)+i])

if len(c) == 0:
    print("CHEMISTRY NOT FOUND")
elif len(c) > 0:
    for i in range(3):
        cval[i] = 1+int(c)+i
        gclist.append(dlist[1+int(c)+i])

if len(m) == 0:
    print("MATHEMATICS NOT FOUND")
elif len(m) > 0:
    for i in range(3):
        mval[i] = 1+int(m)+i
        gmlist.append(dlist[1+int(m)+i])

#location post pcm
print(pval)
print(cval)
print(mval)

print('step 9 - ')
print(gplist)
print(gclist)
print(gmlist)

print('---physics--')
def filmrkss(string, substrmkss):
    return [str for str in string if
            any(sub in str for sub in substrmkss)]

physvnty = filmrkss(gplist,substrmkss)

def filmrkse(string, substrmkse):
    return [str for str in string if
             any(sub in str for sub in substrmkse)]

phyeigty = filmrkse(gplist,substrmkse)

def filmrksn(string, substrmksn):
    return [str for str in string if
             any(sub in str for sub in substrmksn)]

phyninty = filmrksn(gplist,substrmksn)

print(physvnty)
print(phyeigty)
print(phyninty)

print('---chemistry--')

chsvnty = filmrkss(gclist,substrmkss)

cheigty = filmrkse(gclist,substrmkse)

chninty = filmrksn(gclist,substrmksn)

print(chsvnty)
print(cheigty)
print(chninty)

print('---maths--')

mtsvnty = filmrkss(gmlist,substrmkss)

mteigty = filmrkse(gmlist,substrmkse)

mtninty = filmrksn(gmlist,substrmksn)

print(mtsvnty)
print(mteigty)
print(mtninty)

print('step 10 - final step')
physics = 0
if len(physvnty) > 0:
    physics = 70
elif len(phyeigty) > 0:
    physics = 80
elif len(phyninty) > 0:
    physics = 90

print("PHYSICS:")
print(physics)
chemistry = 0
if len(chsvnty) > 0:
    chemistry = 70
elif len(cheigty) > 0:
    chemistry = 80
elif len(chninty) > 0:
    chemistry = 90

print("CHEMISTRY:")
print(chemistry)
mathematics = 0
if len(mtsvnty) > 0:
    mathematics = 70
elif len(mteigty) > 0:
    mathematics = 80
elif len(mtninty) > 0:
    mathematics = 90

print("MATHEMATICS:")
print(mathematics)
percentage = (physics+chemistry+mathematics)/3
print("PERCENTAGE:")
print(percentage)
print('RESULT')
print('------')
if percentage > 90:
 print('Campus-Alpha')
elif percentage >= 80:
 print('Campus-Beta')
elif percentage >= 70:
 print('Campus-Gama')
else :
 print('SORRY YOU ARE NOT SELECTED')

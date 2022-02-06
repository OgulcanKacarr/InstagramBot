

#STRİNG

#Yazıyı tersten yazdırma
rev_string= input("enter text: ")
print(rev_string[::-1])
#==================================
a="Hello world"
a[0:]	#sıfırdan başla sona kadar al,
a[0:2]	#sıfırdan başla, ikiye kadar olanları al.
#==================================
message = "hello there. My name ise Ogulcan"
message.upper() #karakterlerin hepsini büyük harf yap.
message.lower() #karakterlerin hepsini küçük harf yap.
message.title() #her kelimenin baş harfini büyük harf yap.
message.capitalize() #kelimenin sadece ilk harfini büyük harf yap.
message.strip()	 #baş ve sonundaki boşluk karakterleri silinir.
message.lstrip()	#sadece soldan sil.
message.rstrip()	#sadece sağdan sil.
message.strip("w.ce")	#yazı içeriismde w . c e harflerini siler.
message.split()	#her kelimeyi parçalayara ayırır. String'i diziye çevirir.
message.split(".") #yazıyı noktalardan sonra ayırır.
message= "-".join(message)	#ayrılmış yazıyı aralarına - koyarak birleştir.
index = message.find("Hello") #yazı içerisinde hello kelimesi varsa onun index'ini döndürür. -1 dönerse kelime yoktur.
isFound = message.startswith("H") #H ile başlıyorsa
print(isFound)					#True değeri dönecektir.
isFound = message.endswith("n")	#n ile bitiyorsa
print(isFound)					#true değeri dönecektir.
message.replace("Hello","hello") #Hello değerini, hello olarak değiştirir.
message.center(100,'*')		#yazıyı 100 karakterlerik alan oluşturur ve onun içinde ortalar ve boşluklara * ekler.
message.ljust(20,"*")	#ifadeyi sadece sola yasla ve yıldız koy.
message.rjust(20,"*")	#ifadeyi sadece sağa yasla ve yıldız koy.
message.count("e")		#yazı içerisinde e harfinden kaçtane var?.
message.isalpha()	 #yazı içerisindeki değerler alfabetik mi?
message.isdigit()	#yazı içerisindeki değerler sayısal mı?

#==================================
#LIST
myList = ["BMW","Mercedes","Mazda"]

len(myList)			 #liste kaç elemanlı.
myList[0]			 #listenin ilk elemanı.
myList[-1]			 #listenin son elemanı.
myList[0] = "Opel"	 #listenin ilk elemanını değiştir.
"Mercedes" in myList #Mercedes liste içinde bulunuyorsa true döndürür.
myList[0:3]			 #ilk üç elemanı al.
del myList[-1]		 #son elemanı sil.
min(myList)			 #liste içerisindeki minimum değeri alır.
max(myList)			 #liste içerisindeki maximum değeri alır.
myList.append("TOGG") #TOGG kelimesini listeye ekle.
myList.insert(3,"TOGG") #üçüncü indeksten sonra TOGG kelimesini ekle.
myList.pop(0)			#ilk elemanı sil.
myList.remove("BMW")	#BMW içeriğini sil.
myList.sort()			#sayısal ya da alfabetik olarak sıralanır.
myList.reverse()		#listeyi tam tersine çevirir.
myList.clear()			#tüm listeyi temizler.

#==================================
#DICTIONARY

citys = {

"İstanbul":34,
"Sakarya":54,
"Bolu":14
	
}

citys["İstanbul"]	#34 plakası gelecektir.

users = {

"Admin":{
	"age":22,
	"role":"admin"
},
"ogulcan":{
	"role":"manager"
},
"guest":{
	"role":"customer"
},
}
	
users["admin"]["age"]	#admin kullanıcısının yaşına ulaşılır.

#==============================
#LOOP

for item in range(2,10):	#2 ile 10 arasında sayı oluşturur.
	print(item)

greeting = "hello"

for index, item in enumerate(greeting):	#listeyi elemanları indexler.
	print(f" {item} ve {index}")
#================================
#FUNC

def sayHello(name = 'default'):
	print(f"hello {name}")		#girilin değere işlem yapılır, eğer bir değer girilmezse default olarak verilen yazı kullanılır.

def age(date):
	return 2022 - date			#dışarıya kişinin yaşını döndürür.

def add(*params):
	return sum((params))		#gelen her parametreleri topla.

def displayUser(**args):		#dictionary gelecek ise iki yıldız ile belirtilir.
	for key, value in args.items():
		print(f" {key} is {value}")

displayUser(name="ogulcan", age=2, city="istanbul")


#====================
#OOP

#Class
class Person:
	#attributes

	#constructor method (yapıcı metod)
	def __init__(self, name, year):
		#object attributers
		self.name = name
		self.year = year

	#methods
	def intro(self):
		print("hello")

	def calculateAge(self):
		print(2022 - self.year)


p1 = Person("ogulcan",1999)
p2 = Person("serap",1999)

print(f"ogulcan: {p1.calculateAge()}, serap: {p2.calculateAge()}")

#===================================
#ERROR HANDLİNG

while True:
	try:
		x = int(input("x: "))
		y = int(input("y: "))
		print(x/y)
	except Exception as e:		#her hatayı kendi gösterir.
		print(f"Yanlış bilgi girdiniz, Hata kodu:[ {e} ]")
	else:			#bilgi gelene kadar döngüde kalır.
		break

ya da

def checkPassword(password):
	if len(password) < 8:
		raise Exception("parola en az 7 karakter olmalıdır")
	elif not re.search("[a-z]",password):
		raise Exception("parola küçük harf içermelidir.")
	elif not re.search("[A-Z]",password):
		raise.Exception("parola büyük harf içermelidir.")
	elif re.search("\s",password):
		raise.Exception("parola boşluk içermemelidir.")

password="12345"

try:
	checkPassword(password)
except Exception as ex:
	print(ex)

#=========================================
#FILE

#w: yazma, dosyayı oluşturur.
#a: ekleme, dosya konumda yoksa oluşturur.
#x: oluşturma, dosya zaten varsa hata verir.
#r: okuma, dosya yoksa hata verir.
######################

#dosya oluşturma/açma
try:	
	file = open("C:/Users/Desktop/newFile.txt","a", encoding='utf-8')
	file.write("\nbla bla bla") #yazı yazma
except FileNotFoundError:
	print("dosya yok")
finally:
	file.close() #dosya kapatma. Kapanmazsa yavaşlamalara sebep verir.
######################
#dosya okuma
try:	
	file = open("C:/Users/Desktop/newFile.txt","r", encoding='utf-8')
	for i in file:
		print(i, end="")
except FileNotFoundError:
	print("dosya yok")
finally:
	file.close() #dosya kapatma. Kapanmazsa yavaşlamalara sebep verir.
######################
#dosya okuma
try:	
	file = open("C:/Users/Desktop/newFile.txt","r", encoding='utf-8')
	content = file.read()	#cursor dosyanın en sonuna gider.
	content2 = file.read(5) #içeriğin ilk 5 karakterini alır.
	print(content,end="")
	print(content2,end="")
except FileNotFoundError:
	print("dosya yok")
finally:
	file.close() #dosya kapatma. Kapanmazsa yavaşlamalara sebep verir.
######################
#dosya okuma
try:	
	file = open("C:/Users/Desktop/newFile.txt","r", encoding='utf-8')
	content = file.readline() #her satırı okur.
	print(content, end="")
except FileNotFoundError:
	print("dosya yok")
finally:
	file.close() #dosya kapatma. Kapanmazsa yavaşlamalara sebep verir.

######################
#dosya okuma
try:	
	file = open("C:/Users/Desktop/newFile.txt","r", encoding='utf-8')
	content = file.readlines() #tüm satırları okuma.
	print(content[0], end="")
	content.insert(1,"test")	#0'dan sonraya değer ekleme.
except FileNotFoundError:
	print("dosya yok")
finally:
	file.close() #dosya kapatma. Kapanmazsa yavaşlamalara sebep verir

#======================================
#MODULES

#RANDOM LIB
result = random.randint(1,10)		#rastgele sayı üretme
print(result)

names = ["serap","yağmur","ogulcan"]
result = names[random.randint(0,len(names)-1)]	#liste kadar sayı üret.
print(result)

names = ["serap","yağmur","ogulcan"]
result = random.choice(names)			#liste içerisinde rastgele birini seç.
print(result)

names = ["serap","yağmur","ogulcan"]
print(names)
result = random.shuffle(names)			#listeyi karıştırır.
print(names)

names = ["serap","yağmur","ogulcan"]
result = random.sample(names,2)			#liste içerisinden rastgele 2 değer getir.
print(result)

#DATATIME
from datetime import datetime


day = datetime.today().day				#day
month = datetime.today().month			#month
hour = datetime.today().hour			#hour
minute = datetime.today().minute		#minute
second = datetime.today().second		#second

info = datetime.today()
calender = datetime.ctime(info)			#düzenli şekilde tarihi gösterir.

#OS
os.name								#işletim sistemi türü.
os.getcwd()							#çalışan dosyanın konumu verir.
os.mkdir("newFolder")				#klasör oluşturma.
os.chdir("..")						#klasör değiştirme.
os.chdir("newFolder/newFolder2")	#klasör içerisinde klasör oluşturma.
os.listdir("C:\\")					#dizin gösterme.
os.stat("file.txt")					#dosya hakkında bilgi görme.
os.system("file.exe")				#dosya çalıştırma.
os.rename("newFolder","oldFolder")	#klasör ismi değiştirme.
os.rmdir("oldFolder")				#klasör silme.
a = os.path.abspath("file.py")		#dosya yolu
os.path.dirname(a)					#dizin yolu
os.path.exists("file.py")			#dosya var mı? yok mu?
os.path.isdir("C:\\Users\\Desktop")	#klasör mü? değil mi?
os.path.join("C:\\","Deneme")		#Dizin oluşturma.
os.path.split("C:\\deneme")			#dizini bölme.
os.path.splitext("file.py")			#dosya ile uzantısını ayırır.

#RE (Yazım Denetimi)
string = "hello world"

re.findall("hello",string)	#değer içinde verilen kelimeyi arar.
re.sub(" ","-",string)		#değer içindeki boşlukları "-" ile değiştirir.
re.findall("^a",string)		#kelime a ile başlıyor mu?
re.findall("a$",string)		#kelime a ile bitiyor mu?

#JSON

with open("s.json") as file:			#json içerikli dosyayı ekleyerek işlenebilir hale getirmiş olduk.
	data = json.load(file)
	print(data["name"])

#===
person_dict = {
	
	"name":"Ali",
	"languages":["Python","C#"]

}

result = json.dumps(person_dict)	#json dosyası oluşturma.

#====
person_dict = {
	
	"name":"Ali",
	"languages":["Python","C#"]

}

with open("s.json","w") as file:
	json.dump(person_dict,file)		#json oluşturarak json dosyasına kaydettik.
	
#====
person_string = '{"name":"John", "age":30, "car":null}'

result = json.loads(person_string)
print(result["name"])

#====================
#REQUESTS

import requests
import json

url = "https://api.exchangeratesapi.io/latest"
site = requests.get(url)		#siteye ulaş.
result = json.loads(site.text)	#siteyi json şeklinde çek.

for i in result:			#siteyi komple i'ye aktar.
	print(i["title"])		#sitedeki her title'ı çek.
	if i["userId"] == 1:	#user id'si 1 olanları çek.
	 	print("user ıd: 1")

#======
import requests
import json

url = "https://api.genelpara.com/embed/doviz.json"
site = requests.get(url)		#siteye ulaş.
result = json.loads(site.text)	#siteyi json şeklinde çek.

alis = result["USD"]["alis"]
satis = result["USD"]["satis"]

print(f"Dolar alış fiyatı: {alis} \ndolar satış fiyatı: {satis}")

#=============
#BEATIFUL SOUP

#site kaynak kodlarına ulaşma.

from bs4 import BeautifulSoup
import requests


url = "https://www.fullhdfilmizlesene.pw/"
html = requests.get(url).content	#siteye ulaş ve json olarak al.		
soup = BeautifulSoup(html,"html.parser")	#soup objesi oluştur.


result = soup.title					#sitenin başlığını alır.
result = soup.title.string			#sayfanın direk yazısı gelir.
result = soup.head					#sayfanın head kısmını alır.
result = soup.body					#sayfanın body kısmı gelir.
result = soup.h1.string				#ilk h1 etiketi alır.
result = soup.find_all("h1")		#bütün h1'leri al.
result = soup.find_all("h1")[0]		#h1 içinden ilk elemanı al.
result = soup.div					#div etiketini alır.
result = soup.find_all("div")[2]	#div etiketleri içerisindeki değeri alır.
result = soup.find_all("div").ul 	#div içindeki ul etiketlerini çek.
result = soup.find_all("div").ul.li #div içindeki ul etkiketi içindeki li etiketini alır.
result = soup.find_all("div").ul.find_all("li")	#div içindeki ul etkiketi içindeki li'leri bul.
result = soup.div.findChildren()	#div altındaki bütün etiketleri getir.
result = soup.div.findNextSibling()	#bir sonraki div etiketini çeker.

#SELENIUM

import selenium
import time
from selenium import webdriver

driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)						#url'yi aç.
time.sleep(1)						#1 saniye bekle.
driver.title						#sayfanın başlığı.
driver.maximize_window()			#sayfayı tam ekran yap.
driver.save_screenshot("ss.png")	#sayfadan ss al.
newUrl = "http://github.com/OgulcanKacarr"
driver.get(url)						#başka sayfaya yönlendirme yap.
driver.back()						#önceki sayfaya geri gel.
driver.forwad()						#sonraki sayfaya git.

if "ogulcankacar" in driver.title:	#sayfanın başlığında ogulcankacarr yazıyor mu.
	print("yes")

driver.close()						#sayfayı kapat.

#================
#sayfa etkileşimleri


s = "/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]"
searchInput = driver.find_element_by_xpath(s)	#arama kutusuna ulaş.
time.sleep(1)

searchInput.send_keys("python")			#kutu içine python yaz.
searchInput.send_keys(Keys.ENTER)		#enter'a bas.
time.sleep(1)

repoElements = ".repo-list-item a"	#repo elemanlarının a etiketlerini yani başlıklarını al.
repo = driver.find_elements_by_css_selector(repoElements)

for element in repo:
	print(element.text)


#=======================
#NUMPY - NUMBERİC DATA ANALİZ

import numpy as np


arrayList = np.array([1,2,3,4,5,6,7,8,9])	#liste oluşturma.
multiArrayList =  arrayList.reshape(3,3)	#3 listeyi satır ve 3 sutundan oluşan matriks oluştur.
multiArrayList.sum(axis=1)	#satırların toplamı.
multiArrayList.sum(axis=0)	#sutünların toplamı.

result = np.array([[1,3,4],[5,7,9]])
result = result[:,2]		#her listenin ikinci sütünlarını al. 4 ve 9
result = np.arange(1,10,4)	#1 dahil ama 10 dahil olmamak üzere 1'den 10'a kadar eleman üretir ve bu elemanlar 4'er 4'er oluşur.
result = np.zeros(10)	#10 adet sıfırlardan oluşan liste oluşur.
result = np.ones(10)	#10 adet birlerden oluşan liste oluşturur.
result = np.linspace(0,100,5)	#0 ile 100 arasındaki sayıları eşit şekilde 5 parçaya böler.
result = np.random.randint(0,10) # 0 ile 9 arasında rasgele sayı üretir.
result = np.random.randint(1,10,3)	#1 ile 9 arasında sayı üret ve bu sayılardan 3 tane gönder.
result = np.random.rand(5)	#0 ile 1 arasında 5 tane sayı üret.
resultMax = result.max()	#en büyük sayı.
resultMin = result.min()	#en küçük sayı.
resultOrt = result.mean()	#sayıların ortalaması.
indexMax = result.argmax()	#en büyük sayının index numarası.
indexMin = result.argmin()	#en düşük sayının index numarası.


result = np.sin(result)		#sinüs alma.
result = np.cos(result)		#kosinüs alma.
result = np.sqrt(result)	#karekök alma.
result = np.vstack((result,result))	#matriksleri dikey olarak dizer.
result = np.hstack((result,result))	#matriksleri yatay olarak dizer.

#====================0
#PANDAS - DATA ANALİZ

import pandas as pd

df = pd.read_csv("data.nba.csv")	#excell dosyasını bağladık.
result = df.head(10)	#ilk 10 satırı çektik.
result = len(df.index)	#toplam kaç kayıt var.
result = df["Salary"].mean()	#tüm oyuncuların toplam maaş ortalaması.
result = df.columns		#column isimleri.
result = len(df.columns)	#ne kadar column var

#==========
#QTDesigner











































































































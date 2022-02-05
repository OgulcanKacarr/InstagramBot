from selenium.webdriver.common.keys import Keys 
from InstagramBotUser import username, password
from colorama import Fore, Back
from selenium import webdriver
import colorama
import selenium
import wget
import time
import os

class Instagram():
	def __init__(self,username,password):
		self.browserProfile = webdriver.FirefoxOptions()
		self.browser = webdriver.Firefox()
		self.username = username
		self.password = password
		#self.browser.set_window_position(700, -300)
		#self.browser.set_window_size(500,600)
	def signIn(self):
		self.browser.get("https://www.instagram.com/accounts/login/?next=%2Faccount%2Flogin&source=desktop_nav")
		time.sleep(3)
		usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
		passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")

		usernameInput.send_keys(self.username)
		passwordInput.send_keys(self.password)
		passwordInput.send_keys(Keys.ENTER)
		time.sleep(3)

	def getFollowers(self):
		self.browser.get(f"https://www.instagram.com/{self.username}")
		time.sleep(3)
		followersButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]")
		followersButton.click()
		time.sleep(3)
		dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
		followersCount = len(dialog.find_elements_by_css_selector("li"))
		print(f"first count: {followersCount}")
		action = webdriver.ActionChains(self.browser)
		while True:
			dialog.click()
			action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
			time.sleep(3)
			newCount = len(dialog.find_elements_by_css_selector("li"))
			if followersCount != newCount:
				followersCount = newCount
				print(Fore.GREEN)
				print(f"updated count: {newCount}")
				time.sleep(2)
			else:
				break
		followers = dialog.find_elements_by_css_selector("li")

		followersList = []
		for user in followers:
			link = user.find_element_by_css_selector("a").get_attribute("href")
			print(Fore.RED)
			print(f"User profile: {link}")
			followersList.append(link)
		try:  
			with open("Wordlist/followers.txt","a",encoding="utf-8") as file:
				for item in followersList:
					file.write(item + "\n")
					file.close()
				
		except:
			file.close()
		print(Fore.BLUE)
		print(f"\nall users profile save >> /Wordlist/followers.txt")

	def followUser(self,username):
		self.browser.get("https://www.instagram.com/"+username)
		time.sleep(3)
		followButton = self.browser.find_element_by_tag_name("button")
		#followButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
		#print(followButton.text)
		if followButton.text != "Takiptesin" or followButton.text != "Message" or followButton.text != "Following" or followButton.text != "Mesaj" or followButton.text == "Follow Back":
			followButton.click()
			print(Fore.GREEN)
			print("following is succesfull")
			time.sleep(2)
		else:
			print(Fore.RED)
			print("Already following")

	def unFollowUser(self,username):
		self.browser.get("https://www.instagram.com/"+username)
		time.sleep(3)
		#followButton = self.browser.find_element_by_tag_name("button")
		followButton = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button")
		if followButton.text != "Follow Back" or followButton.text == "Takiptesin" or followButton.text == "Message" or followButton.text == "Following" or followButton.text == "Mesaj":
			followButton.click()
			confirmButton = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
			confirmButton.click()
			print(Fore.GREEN)
			print("unfollowing is succesfull")
			time.sleep(2)
		else:
			print(Fore.RED)
			print("Already unfollowing")

	

def InstallBrowser():
	try:
		print(Fore.GREEN)
		url = 'https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz'
		filename = wget.download(url)
		print("\n\n")
		os.system("tar -xvf geckodriver-v0.28.0-linux64.tar.gz")
		os.remove("geckodriver-v0.28.0-linux64.tar.gz")
		os.system("mv geckodriver /usr/bin")
		os.system("chmod 777 /usr/bin/geckodriver")
		os.remove("geckodriver")
	except KeyboardInterrupt:
		print(Fore.RED)
		print("\nBye bye")

def fileConts():
	haveOrnotFile = os.path.exists("/usr/bin/geckodriver")
	if haveOrnotFile != True:
		print(Fore.BLUE)
		print("""
                                                                                                                                                       
                                                                                                      .                                                   
                                                   ...'',,.                                         .''''.....                                            
                                              .'''''''''....                     .'''.              .......''.....                                        
                                         ..''.','...''....     '.     ...  .''. .:ddl.               .................                                    
                                       ..','',,''...''''...''',,.    ,od:..:dd:..;dd;  .:cccc:,.      ..'......'''......                                  
                                    ...'','..''.....'...  ..',,''::. ;ddc. ;dd:..'od;.,odc''::c;..,:;'...........,'..'.....                               
                                 ...'''..''..''.........';'':;::';o, .coo:;cdl.  'od,.'lo:.......,:lcclc'........,'..'.........                           
                              ...'...............,cooolc,..lc.:d;.cl...;c;,'',....;l,...,c:::;..lxo::lod;..,;....'...............                         
                              ....''...........;lol,.;odo' 'c:,,,,;c,........ ..................,::::loc'.cddl:,'.....'...........                        
                             .......'.........:dl'.   ;dd;  .',''.,c,....   .;:;'.,:.  .....'....  ..;;..cddl;,col,....''......'....                      
                          ...........'.'.... 'ddo:....ldo;     ''',..       ;olcooc;.     ....          'dd:. .,ldo....','.....'...'..                    
                        .................'.   ,ooollol:'..                 .co:;ll;,.      .            .''. .cddl.  ..........'..'''....                 
                     .............''.   ...    ....';.                      ,llolcc:'                       .cdc'.   ..   .........'.......               
                     .. ..   ......                                           ...'::.                        ..             ................              
                     ......  .                                              .;:cldc,.                                                ......               
                 .........                                                 .lxoccl,                                                   .''......           
                .......                                                     .,;:coo:.                                                   .',...'.          
              .......                                                            .;;.                                                     ........        
            ..'...                                                          ..     .'.                                                       ....'.       
           .....                                                           .;.      ;;'.                                                       ...''.     
          .....                                                            .;,     .;...                                                        ....'.    
         ....                                                               .,;;;;,,.                                                             .....   
        ...                                                                   ...,;'                                                                ....  
                                                                            ..,;cll:.                                                                     
                                                                           .cdocll,                                                                       
                                                                           .,clcloc,.                                                                     
                                                                              ...;cc.                                                                     
                                                                           .,'.  .,:'                                                                     
                                                                           .;ol;;cl;.                       Oğulcan KAÇAR                                             
                                                                            .;oddl;'.                       github.com/OgulcanKacarr                                              
                                                                           .:lloolc:'.                                                                    
                         .....'...'.......''..'.. .''.                       ......                      ..'....'...'.......'.........                    
                                                                           .........                                                                      
                                                                           ..........                                                                     
                                                                           ..........                                                                     
                                                                           .''....'..                                                                     
        """)
        	
		print(Fore.GREEN)
		print("\n\n[!] please wait, files are uploading..\n")
		print("============================================")
		time.sleep(3)
		try:
			InstallBrowser()
			print(Fore.BLUE)
			print("Download complete")
			print(Fore.RED)
			
		except KeyboardInterrupt:
			print(Fore.RED)
			print("\nCancel")
			exit()
	else:
		pass

colorama.init()
os.system("clear")
fileConts()
print(Fore.GREEN)
print("WELCOME".center(110,"*"))
print(Fore.BLUE)
print("""
                                                                                                      .                                                   
                                                   ...'',,.                                         .''''.....                                            
                                              .'''''''''....                     .'''.              .......''.....                                        
                                         ..''.','...''....     '.     ...  .''. .:ddl.               .................                                    
                                       ..','',,''...''''...''',,.    ,od:..:dd:..;dd;  .:cccc:,.      ..'......'''......                                  
                                    ...'','..''.....'...  ..',,''::. ;ddc. ;dd:..'od;.,odc''::c;..,:;'...........,'..'.....                               
                                 ...'''..''..''.........';'':;::';o, .coo:;cdl.  'od,.'lo:.......,:lcclc'........,'..'.........                           
                              ...'...............,cooolc,..lc.:d;.cl...;c;,'',....;l,...,c:::;..lxo::lod;..,;....'...............                         
                              ....''...........;lol,.;odo' 'c:,,,,;c,........ ..................,::::loc'.cddl:,'.....'...........                        
                             .......'.........:dl'.   ;dd;  .',''.,c,....   .;:;'.,:.  .....'....  ..;;..cddl;,col,....''......'....                      
                          ...........'.'.... 'ddo:....ldo;     ''',..       ;olcooc;.     ....          'dd:. .,ldo....','.....'...'..                    
                        .................'.   ,ooollol:'..                 .co:;ll;,.      .            .''. .cddl.  ..........'..'''....                 
                     .............''.   ...    ....';.                      ,llolcc:'                       .cdc'.   ..   .........'.......               
                     .. ..   ......                                           ...'::.                        ..             ................              
                     ......  .                                              .;:cldc,.                                                ......               
                 .........                                                 .lxoccl,                                                   .''......           
                .......                                                     .,;:coo:.                                                   .',...'.          
              .......                                                            .;;.                                                     ........        
            ..'...                                                          ..     .'.                                                       ....'.       
           .....                                                           .;.      ;;'.                                                       ...''.     
          .....                                                            .;,     .;...                                                        ....'.    
         ....                                                               .,;;;;,,.                                                             .....   
        ...                                                                   ...,;'                                                                ....  
                                                                            ..,;cll:.                                                                     
                                                                           .cdocll,                                                                       
                                                                           .,clcloc,.                                                                     
                                                                              ...;cc.                                                                     
                                                                           .,'.  .,:'                                                                     
                                                                           .;ol;;cl;.                       Oğulcan KAÇAR                                             
                                                                            .;oddl;'.                       github.com/OgulcanKacarr                                              
                                                                           .:lloolc:'.                                                                    
                         .....'...'.......''..'.. .''.                       ......                      ..'....'...'.......'.........                    
                                                                           .........                                                                      
                                                                           ..........                                                                     
                                                                           ..........                                                                     
                                                                           .''....'..                                                                     
        """)
print(Fore.RED)
print(f"\n1- Attract Followers\n2- Auto Follower\n3- Automatic Unfollow\n4- Help\n5- Exit")

while True: 
	try:
		print(Fore.GREEN)
		choose = int(input("Please enter a option: "))
		print(Fore.RED)
		if choose == 1:
			#getYourFollowers
			instagram = Instagram(username,password)
			instagram.signIn()
			instagram.getFollowers()
		elif choose == 2:
			print(Fore.BLUE)
			a = int(input("Use single=1 / Use list=2:"))
			if a == 1:
			#   auto following / unfollowing
				print(Fore.GREEN)
				user = input("Person to follow: ")
				instagram = Instagram(username,password)
				instagram.signIn()
				instagram.followUser(user)
			else:
				userList = []
				users = open("Wordlist/userList.txt","r",encoding="utf-8")
				for line in users:
					print(f"following users: {line}")
					userList.append(line)
					for user in userList:
						instagram = Instagram(username,password)
						instagram.signIn()
						instagram.followUser(user)
						time.sleep(2)
		elif choose == 3:
			a = int(input("Use single=1 / Use list=2:"))
			if a == 1:
			#   auto following / unfollowing
				print(Fore.GREEN)
				user = input("Person to unfollow: ")
				instagram = Instagram(username,password)
				instagram.signIn()
				instagram.unFollowUser(user)
			else:
				userList = []
				users = open("Wordlist/UnUserList.txt","r",encoding="utf-8")
				for line in users:
					print(f"Unfollowing users: {line}")
					userList.append(line)
					for user in userList:
						instagram = Instagram(username,password)
						instagram.signIn()
						instagram.unFollowUser(user)
						time.sleep(2)
		elif choose == 4:
			print(Fore.BLUE)
			print("HELPING".center(100,"*"))
			print(Fore.YELLOW)
			print("""


				[Attract Followers] : here you can save all the followers in a text file.
				[Auto Follower]     : Here you can automatically follow one or more users that you pull from a text file.
				[Automatic Unfollow]: Here you can automatically unfollow one or more users that you pull from a text file.



				""")

		elif choose == 5:
			print(Fore.GREEN)
			print("bye bye")
			break
	except Exception as e:
		print(Fore.RED)
		print(f"Error code: {e}")
		print(Fore.BLUE)
		print("There may be a problem with Instagram. Please try again later. :(")
	except KeyboardInterrupt:
		print(Fore.GREEN)
		print("bye bye")
		exit()



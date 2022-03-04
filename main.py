from colorama import init, Fore, Back
from requests.exceptions import ConnectionError
try:
	import os,sys,time,requests

class Main:

	def __init__(self):
		self.detekos()
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK

IP = requests.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))

	def menu(self):
		os.system("clear")
	print("\033[1;0m\033[1;41mFollow Akun IG Gua Om...\033[1;0m")
	time.sleep(10)
	os.system("xdg-open https://bit.ly/KenzoxploitIG")
	os.system("clear")
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		;    \033[1;0m\033[1;41mAuthor : KenzoXploit\033[1;0m   ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	
NOTE: This tool's only work for Indonesia number phone.

1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Sociolla.com
""")
	print(""+Fore.RED+"   [+] Time Local:\033[1;92m"+localtime)
	print(""+Fore.RED+"   [+] Instagram:\033[1;92mbit.ly/KenzoxploitIG")
	print(""+Fore.RED+"   [+] IP Kamu:\033[1;92m"+IP)
	print(""+Fore.RED+"   [+] Pengguna:\033[1;92m1032 Orang")
	print("")
		
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))

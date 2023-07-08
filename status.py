import urllib.request, urllib.error
import threading
import dns.resolver


def baner():
    print("""
               ~~~~ SUBDOMAIN ENUMERATION TOOL ~~~~
    
Created By :
                 ______                      ________                         
___________  ____  /______________        ______(_)_____ ___      _______ _
_  ___/_  / / /_  __ \  _ \_  ___/        _____  /_  __ `/_ | /| / /  __ `/
/ /__ _  /_/ /_  /_/ /  __/  /            ____  / / /_/ /__ |/ |/ // /_/ / 
\___/ _\__, / /_.___/\___//_/________________  /  \__,_/ ____/|__/ \__,_/  
      /____/                _/_____//_____/___/                            
    """)


def uslResposeCodeReturn(url):
    try:
        conn = urllib.request.urlopen(url)
    
    except urllib.error.HTTPError as e:    
        print("{} --> [{}]".format(url,e.code))


    except urllib.error.URLError as e:
        print('URLError: {}'.format(e.reason))

    else:  
      print("{} --> [{}]".format(url,"200"))
    

def mainprocess(fileName):
    file = open(fileName, 'r')
    try:
        for each in file:
           url=each.rstrip('\n')
           uslResposeCodeReturn(url)
           
    except:
        print("finshed {}".format(threading.current_thread().getName()))


def clickJackFinder():
    url=input("enter the url > ")
    jackbinary=0

    response = urllib.request.urlopen(url)
    headers = response.headers

    for header, value in headers.items():
       if "X-Frame-Options" in header or "Content-Security-Policy" in header:
           print("\n\n -------------- NO BUG -> {} this domain NOT vuln for CLICKJACKING".format(url))
           jackbinary=1
           break
    if(jackbinary==0):
        print("\n\n -------------- NO BUG -> {} this domain vuln for CLICKJACKING".format(url))
       
    

def has_valid_spf():
    domain=input("Enter the domain without protocol[http/https] > ")
    try:
        answers = dns.resolver.query(domain, 'TXT')
      
        for data in answers:
            for txt_string in data.strings:
                if txt_string.decode().startswith('v=spf1'):
                    print("\n\n -------------- NO BUG -> {} this domain has valid spf record".format(domain))
        
    except dns.resolver.NoAnswer:
         print("\n\n ------------ YES BUG -> {} this domain has NOT valid spf record".format(domain))

def starting():
   
    a="""
       1 --> status Code checker
       2 --> clickjacking finder
       3 --> spf validation checker

    """
    print(a)
    num=int(input("Enter the num >"))
    if(num==1):
        mainprocess("statuscode.txt")
    elif(num==2):
        clickJackFinder()
    elif(num==3):
       has_valid_spf()
    else:
       print("check your input")

baner()
while(True):
    starting()

import sys
from tkinter.messagebox import NO
import requests
import re
import optparse
from selenium import webdriver
from time import sleep
class WebScraping:
    def __init__(self):
        self.argu = sys.argv
        print("""

__        __   _    ____                       _             
\ \      / /__| |__/ ___|  ___ _ __ __ _ _ __ (_)_ __   __ _ 
 \ \ /\ / / _ \ '_ \___ \ / __| '__/ _` | '_ \| | '_ \ / _` |
  \ V  V /  __/ |_) |__) | (__| | | (_| | |_) | | | | | (_| |
   \_/\_/ \___|_.__/____/ \___|_|  \__,_| .__/|_|_| |_|\__, |
                                        |_|            |___/ 
                                        by HaxorPoint

                #################  HAXORPOINT  #################
                
                >>>> Name: Professor
                
                #################  HAXORPOINT  #################""")
    def Enter_Website(self):
        try:
            reader = optparse.OptionParser()
            reader.add_option('-u','--url',dest='Enter_url',type='str')
            reader.add_option('-f','--file',dest='Enter_file',type='str')
            reader.add_option('-l','--link',dest='For_link',type='str')
            reader.add_option('-e','--email',dest='For_email',type='str')
            reader.add_option('-p','--phone',dest='For_number',type='str')
            reader.add_option('-s','--screenshot',dest='For_screenshot',type='str')
            options,args = reader.parse_args()
            self.url_input = options.Enter_url
            self.file_input = options.Enter_file
            self.link_input = options.For_link
            self.email_input = options.For_email
            self.phone_input = options.For_number
            self.Screenshot_input = options.For_screenshot
            self.pattern = r'http://([a-zA-Z0-9]+.[a-zA-Z0-9]+)'
            self.pattern1 = r'https://([a-zA-Z0-9]+.[a-zA-Z0-9]+)'
            if options.Enter_url != None:
                if re.match(self.pattern, self.url_input) or re.match(self.pattern1, self.url_input):
                    self.data()
                    self.Result()
                else:
                    print("< please correct you url Enter your url form of http and htttps>")
                    sys.exit()
            elif options.Enter_file != None:
                with open(self.file_input,'r') as file:
                    data = file.read()
                    pattern1 = r'([a-zA-Z]+://[a-zA-Z0-9]+.[a-zA-Z0-9]+)'
                    self.text = re.findall(pattern1,data)
                    for i in self.text:
                        self.url_input = i
                        self.data()
                        self.Result()
        except:
                print()
                print("type -h or --help for help")
    def data(self):
                    try:
                        html = requests.get(self.url_input)
                        self.html_data = html.text
                        return self.html_data
                    except:
                        print("Unknown Host")
                        sys.exit()
    def Email(self):
        pattern = r'([a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+)'
        out_emails = re.findall(pattern,self.html_data)
        for i in out_emails:
            print(i)
    def links(self):
        ptt = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        out_links = re.findall(ptt,self.html_data)
        for i in out_links:
            print(i[0])
    def Phone(self):
        pattern = r'((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}'
        phone = re.findall(pattern,self.html_data)
        for i in set(phone):
            print(i[0])
    def screenshot(self):
        a = 0
        for i in set(self.text):
            print(i)
            
            # driver = webdriver.Chrome()
            # driver.get(i)
            # sleep(1)
            # driver.get_screenshot_as_file(f"screenshot{a}.png")
            # driver.quit()
            # a +=1
    def Result(self):
        if self.link_input != None:
            self.links()
        elif self.email_input != None:
            self.Email()
        elif self.phone_input != None:
            self.Phone()
        elif self.Screenshot_input != None:
            self.screenshot()

obj = WebScraping()
obj.Enter_Website()
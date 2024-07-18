import requests
import abc
from selenium import webdriver
from bs4 import BeautifulSoup


  
class Get591ServiceBase:
    @abc.abstractmethod
    def getInfo()->any:
        pass
       

 
class Get591byAPiService(Get591ServiceBase): 
    
    def __init__(self,
                 api_url='https://rent.591.com.tw/home/search/rsList?is_format_data=1&is_new_list=1&type=1&firstRow=30&totalRows=18910&region=8&recom_community=1',
                 headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
                'Referer': 'https://www.google.com/'
                },
                 cookies={}):
        self.api_url=api_url
        self.headers=headers
        self.cookies = cookies
    
    def getInfo(self)->any:
        try:   
            driver=webdriver.Chrome()
            driver.get('https://rent.591.com.tw/')
            cookies=driver.get_cookies()
            
            page_source=driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            
            csrf_token = soup.select_one('meta[name="csrf-token"]')['content']
            text=''

            for cookie in cookies:
                text+=f'{cookie['name']}={cookie['value']};'
                
            text=text[:-1]
            
            
            self.cookies  ={
                'cookie_name': text
            }
            self.headers['X-Csrf-Token']=csrf_token

            driver.quit()
            
            response= requests.get(self.api_url, headers=self.headers, cookies=self.cookies)
            
            data = response.json()
            
            return data
        except Exception as err:
            print(err)
        
          
  
class Get591byHtmlService(Get591ServiceBase):
    def getInfo(self)->any:
        # todo
        return {"dummy":"hello"} 
         
         


def getDummyCookie():
    return 'urlJumpIp=8; T591_TOKEN=7f1h4s4n78vrd1rulkam9rt6qr; is_new_index=1; is_new_index_redirect=1; _gcl_au=1.1.1435490278.1720684478; __utmz=82835026.1720749234.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.4.177724605.1720684478; __lt__cid=262f6ef4-85f9-47ee-9e76-9537c3405315; last_search_type=8; tw591__privacy_agree=1; _ga_8E3GTG4K5C=GS1.3.1720760895.1.0.1720760895.60.0.0; new_rent_list_kind_test=0; __utma=82835026.177724605.1720684478.1721007734.1721140168.3; _gid=GA1.3.143664614.1721140174; _gid=GA1.4.143664614.1721140174; webp=1; PHPSESSID=rp6a70faef2q8obkvv3tuh68l0; newUI=1; _gat=1; _dc_gtm_UA-97423186-1=1; __lt__sid=fe72f2fe-b940ccd7; _clck=14udy6q%7C2%7Cfnj%7C0%7C1653; timeDifference=0; XSRF-TOKEN=eyJpdiI6IjAxQ0pzck0yUG42TG81K05sZ2ZtYkE9PSIsInZhbHVlIjoiTDlsQktGOGtRQjVwUXpNdU9rSndEeWVRbXlYeEpOVjdxOE9GL2NINEpYcWF4YkpUeVBSU0JzR0hoY0lHU3g4bzhYcXRLZG5DTnpIQnd6aGx2NnEzc0F3U05Fa2l1THhCdlpQNHlrTzhtOGhhRFltT1hNT2VEQnFIK2NENDRCajUiLCJtYWMiOiI4ZmE2OTgzNzZjZmU2MzJkYmEzMTMyZTNjYWNhMWI1ZDZkYjVjNTYxZDEyYmI5NWNiNGQ2YjI2MzE5MTcyZWE4IiwidGFnIjoiIn0%3D; _clsk=8y6i6f%7C1721195215958%7C1%7C1%7Cz.clarity.ms%2Fcollect; _gat_UA-97423186-1=1; 591_new_session=eyJpdiI6ImtMeDdYMFhyUlhSd2RuZ3RWMVBaL3c9PSIsInZhbHVlIjoiZnBDeWxEbmJDZ1FvNlh0K3RmOFREbm14ZnByVWNzeExWQ2xMUGJkcUtTSENHbmdkK0s3Y1ErRHFQbHBobkE4UERsRitMRzlicXk3cC9XMTE0OWtDbWV1enJOc0VCcjVuVUZqWWxzTHdGaXR4NitzZDBWdjJmemo1Y0ZYcjQyRXMiLCJtYWMiOiIwMWQ3N2YzZTA0ZGI0M2ZmODIzZDFjY2ExY2FiY2ZkNDEwNGMzNzBlYzE0NGY0OTIzYTMxODRlZTRiYzUxZDRhIiwidGFnIjoiIn0%3D; _ga_HDSPSZ773Q=GS1.1.1721195214.10.1.1721195224.50.0.0; _ga=GA1.1.177724605.1720684478; _ga_H07366Z19P=GS1.3.1721195214.7.1.1721195224.50.0.0'


def getDummyCsrfToken():
    return 'dgow9WGC0HXsxpR4kvL1CnQq4LfNVP1qobGJF1vV'
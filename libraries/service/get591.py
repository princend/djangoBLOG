import requests
import abc
  
  
class Get591ServiceBase:
    @abc.abstractmethod
    def getInfo()->any:
        pass
       

 
class Get591byAPiService(Get591ServiceBase): 
    
    def __init__(self,
                 api_url='https://www.591.com.tw/home/index/guessLove',
                 headers={
                 'User-Agent': 'PostmanRuntime/7.26.8',
                'Referer': 'https://www.google.com/'
                },
                 cookies={
                'cookie_name': 'urlJumpIp=8; T591_TOKEN=jqqu8ukio0mkma5ffudrsdpo14; PHPSESSID=0ie64e7rk7e8en38akgmijd6oj; 591_new_session=eyJpdiI6Im5IUVoyNHVia0VlOG1EUjl6WTVxVVE9PSIsInZhbHVlIjoia3VKNjRHZGZMZEFCK3A4VFdQb2ZDVUIvZnBNYTV6VXM2UGpnMDNvYWxFZFhyU0ZPb1VoREhnMFZqZ3lPVEcvMWVnVERyTDRzLzhnREVsekVuakxJcGlXSmhjSDJlaU9DVTR6dXUzZVVPZkpjMEhWMVp6RFZXRFRrTnZlQW5qd2MiLCJtYWMiOiI3OGQ3OGJlZTYxNjkzYjQwZmEyYjQ5NjBiNWZlMzg5YTlkM2Q2ZDVjYjg2MTk4OTE4NzA3YjdjY2IwMjU2YTJmIiwidGFnIjoiIn0%3D'
                }):
        self.api_url=api_url
        self.headers=headers
        self.cookies = cookies
    
    def getInfo(self)->any:
        try:   
            response= requests.post(self.api_url, headers=self.headers, cookies=self.cookies)
            data = response.json()
            return data
        except Exception as err:
            print(err)
        
          
  
class Get591byHtmlService(Get591ServiceBase):
    def getInfo(self)->any:
        # todo
        return {"dummy":"hello"} 
         
'''
Created on 2017年8月8日

@author: Administrator
'''

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #https://baike.baidu.com/item/Python/407313?fr=aladdin
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            print('链接名称:',link.get_text(),'已加入要爬取队列')
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        res_data['url'] = page_url
        
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
    
        return res_data
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser')#############html_parser
        
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        
        return new_urls, new_data
    




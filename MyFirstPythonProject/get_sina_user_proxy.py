# encoding: utf-8

import os,sys,urllib2  
  
PROXY_INFO = {  
  'host' : '10.56.192.29' , #proxy server ip address  
  'port' : 8080  
}  
  
def load_url(url):   
  proxy_support = urllib2.ProxyHandler ( { 'http' :   
   'http://%(host)s:%(port)d' % PROXY_INFO } )   
  
  opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)  
  
  urllib2.install_opener(opener)   
  
  src = urllib2.urlopen(url)  
  
  return src.read()  
      
if __name__=='__main__':  
  print load_url("http://www.baidu.com")

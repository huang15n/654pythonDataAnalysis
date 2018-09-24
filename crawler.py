from urllib.request import urlopen # this is python3 
from bs4 import BeautifulSoup
import csv 
import re


""" this to define the crawler for the links that specified the category of ebay"""	

class Crawler:
	
	fieldnames_for_csv = ['item_description', 'item_price', 'item_shipping','total_price']
	
	def crawl_to_pages(self,max_page_number,file_name,weblink):
			words = ""
			current_page = 1
			self.text_file = open(file_name+".txt","w+")
			self.raw_data_csv = open(file_name+".csv","w+")
			self.csv_writer_raw_data = csv.DictWriter(self.raw_data_csv,fieldnames= self.fieldnames_for_csv)
			self.csv_writer_raw_data.writeheader()
			while current_page < max_page_number:
				url = weblink+"_pgn="+str(current_page)
		
				soup = BeautifulSoup(urlopen(url),"lxml")

				description = soup.find_all("li",{"class":"s-item"})
				for x in range(0,len(description)):
					item_description = description[x].div.div.img['alt']
					print(item_description)
					price =  soup.find_all("span",{"class":"s-item__price"})
					item_price = price[x].text.strip('C ')
					item_price = item_price[0:5]
					item_price_double = float(item_price.replace('$',''))
					
					print(item_price_double)
					shipping =  soup.find_all("span",{"class":"s-item__shipping"})

					item_shipping = shipping[x].text.strip('C shipping')
					if(item_shipping == 'Free shipping' or item_shipping == 'Free'):
						item_shipping = '$0.0'
					
					item_shipping_double = float(item_shipping.replace('$',''))
					print(item_shipping_double)
					total_price = item_shipping_double + item_price_double
					self.text_file.write("product name:"+str(item_description)+" price:"+str(item_price)+" shipping:"+str(item_shipping)+" total price:"+str(total_price)+"\n")
					self.csv_writer_raw_data.writerow({'item_description':item_description,'item_price':item_price_double,'item_shipping':item_shipping_double,"total_price":total_price})
					words += str(item_description).lower() + " " +str(item_price).lower() + " " + str(item_shipping).lower() + " "+ str(total_price).lower() + " "
				current_page += 1
		    
		
			#print(sorted(self.product_info,key = lambda s: s[3]))
			self.text_file.close()
			self.raw_data_csv.close()
			return words
      	
		 
		 

 

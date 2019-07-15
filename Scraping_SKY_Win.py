#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver #Control remoto de navegador Web.
from selenium.webdriver.common.keys import Keys #Para simular el uso del teclado

import time
from datetime import datetime, date, timedelta #herramientas para manejos de tiempo y fechas.

import calendar
import csv



tiempo=time.localtime()


ori=[1,2,1,3]
des=[2,1,3,1]
i=0

Active=False
day=tiempo.tm_mday-1
while True:
	if (tiempo.tm_hour<18 and tiempo.tm_hour>7 and not (i==0 and tiempo.tm_mday==day)) or i>0:
		day=tiempo.tm_mday
		Active=True
		time_start=datetime.now()

		hoy = date.today()

		str_hoy=str(hoy.day)+"/"+str(hoy.month)+"/"+str(hoy.year)

		n=30*20

		with open('Vuelos '+str_hoy.replace('/','-')+'.csv', mode='a') as vuelos_file:
		    vuelos_writer = csv.writer(vuelos_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		    vuelos_writer.writerow(['Código','Hora salida','Origen','Ciudad Origen','Hora llegada','Info1','Destino','Tarifa','Fecha Vuelo','Update'])
		'''
		ruta="C:/Users/User/AppData/Local/Programs/Python/Python37/Lib/site-packages/selenium/webdriver/chrome/chromedriver"
		browser = webdriver.Chrome(ruta)
		'''
		option=webdriver.ChromeOptions()
		option.add_argument('headless')
		ruta="C:/Users/Oscar Munoz/AppData/Local/Programs/Python/Python37-32/chromedriver"
		browser = webdriver.Chrome(ruta)
		#browser=webdriver.Chrome()
		j=0

		mess_count=0

		len_elem=0

		Iatas=['SCL','CJC','CCP','CPO']

		
		origin=ori[i]
		print("Origen: "+Iatas[ori[i]-1]+".\n"+"Destino: "+Iatas[des[i]-1])
		"""
		while not (origin<=4 and origin>=1):
			origin=int(input('Ingresar una ciudad de ORIGEN (ingresar valores entre 1 y 3):\n\n 1 := Santiago (Arturo Merino Benitez "SCL").\n'
				+' 2 := Calama (El Loa "CJC").\n 3 := Concepción (Carriel Sur "CCP").\n\t' ))
		"""
		
		destiny=des[i]
		"""
		while not (destiny<=4 and destiny>=1):
			destiny=int(input('Ingresar una ciudad de DESTINO (ingresar valores entre 1 y 3):\n\n 1 := Santiago (Arturo Merino Benitez "SCL").\n'
					+' 2 := Calama (El Loa "CJC").\n 3 := Concepción (Carriel Sur "CCP").\n\t' ))
			if destiny == origin:
				print('La ciudad de destino no puede coincidir con la ciudad de origen.\n\n')
				destiny=0
		"""


		while j<=n and mess_count<=4:
			
			fech=hoy+timedelta(days=j)			#arreglar
			j=j+1
			#fech_arr=fech.split("-")

			fech_dia=str(fech.day)
			if len(fech_dia)<2:
				fech_dia="0"+fech_dia

			fech_mes=str(fech.month)
			if len(fech_mes)<2:
				fech_mes="0"+fech_mes

			fech_year=str(fech.year)

			#Calama: CJC, Santiago: SCL, Concepción: CCP

			#fecha1_dia=fech_dia
			#fecha1_anomes=fech_year+"-"+fech_mes
			#auAvailability="1"
			#ida_vuelta="ida"
			#vuelos_origen=Ciudades[Iatas[origin-1]]
			#from_city1=Iatas[origin-1]
			#vuelos_destino=Ciudades[Iatas[destiny-1]]
			#to_city1=Iatas[destiny-1]
			#flex="1"
			#vuelos_fecha_salida_ddmmaaaa=fecha1_dia+"/"+fech_mes+"/"+fech_year
			#cabina="Y"
			#nadults="1"
			#nchildren="0"
			#ninfants="0"
			#url='https://www.latam.com/es_cl/apps/personas/booking?fecha1_dia=05&fecha1_anomes=2018-11&auAvailability=1&ida_vuelta=ida&vuelos_origen=Santiago%20de%20Chile&from_city1=SCL&vuelos_destino=Concepci%C3%B3n&to_city1=CCP&flex=1&vuelos_fecha_salida_ddmmaaaa=05/11/2018&cabina=Y&nadults=1&nchildren=0&ninfants=0'
			#url='https://www.latam.com/es_cl/apps/personas/booking?fecha1_dia='+fecha1_dia+'&fecha1_anomes='+fecha1_anomes+'&auAvailability='+auAvailability+'&ida_vuelta='+ida_vuelta+	'&vuelos_origen='+vuelos_origen+'&from_city1='+from_city1+'&vuelos_destino='+vuelos_destino+'&to_city1='+to_city1+'&flex='+flex+'&vuelos_fecha_salida_ddmmaaaa='+vuelos_fecha_salida_ddmmaaaa+'&cabina='+cabina+'&nadults='+nadults+'&nchildren='+nchildren+'&ninfants='+ninfants
			
			fromCityCode=Iatas[origin-1]
			toCityCode=Iatas[destiny-1]
			departureDateString=fech_year+"-"+fech_mes+"-"+fech_dia
			fareTypeCategory="1"
			adults="1"
			children="0"
			infants="0"
			pets="0"

			url='https://www.skyairline.com/chile/flujo-compra/busqueda-vuelos?fromCityCode='+fromCityCode+'&toCityCode='+toCityCode+'&departureDateString='+departureDateString+'&fareTypeCategory='+fareTypeCategory+'&adults='+adults+'&children='+children+'&infants='+infants+'&pets='+pets+'&currency=CLP&isMobileSearch=false&isNewSearch=true'


			browser.get(url)
			if len_elem==0:
				time.sleep(20)

			search_route_box_flight_class="flight-search-route-box"	#Clase de los contenedores que poseen la información de cada vuelo.
			null_pading_flight_search_container="day-result-noFlights"  		#En HTML aparece contenedor con esta clase para mostrar que no hay pasajes en fecha indicada
			
			len_elem=0
			count=0	

			message_container=browser.find_elements_by_class_name(null_pading_flight_search_container)
			x=browser.find_elements_by_xpath("//div[@data-bind='slideIn: noFlightsFound']")
			try:
				atributo_estilo=x[0].get_attribute("style")
				print(atributo_estilo)
			except:
				atributo_estilo=" "

			#x=browser.find_elements_by_class_name(search_route_box_flight_class)
			#print("hay",len(x), "vuelos")

			if atributo_estilo=="display: block;": #and len(x)==0:  #arreglar
				mess_count=mess_count+1
				print("Mensaje de falta de vuelos ",mess_count," veces.")
				
			#elif mess_count>0:
			#	mess_count=0
			while (len_elem==0 and count<1000) and atributo_estilo=="display: none;":			#arreglar
				count=count+1
				
				elem = browser.find_elements_by_class_name(search_route_box_flight_class)

				len_elem=len(elem)
				print(len_elem)
				
				for el in elem:
					
					el_arr=el.text.split("\n")
					
								
					with open('Vuelos '+str_hoy.replace('/','-')+'.csv', mode='a') as vuelos_file:
						vuelos_writer = csv.writer(vuelos_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

						hora_salida=el_arr[3][0:5]
						iata_origen=el_arr[3][6:9]
						hora_llegada=el_arr[5][0:5]
						if len(el_arr)==8:
							iata_destino=el_arr[5][6:9]
							tarifa_vuelo=el_arr[6]
							vuelos_writer.writerow([el_arr[4],hora_salida,iata_origen,el_arr[0][0:8],hora_llegada,el_arr[7],iata_destino,tarifa_vuelo,departureDateString,datetime.now()])
							pass	

						elif len(el_arr)==7:
							iata_destino=el_arr[5][6:9].encode('utf-8')
							tarifa_vuelo=el_arr[6].encode('utf-8')
							vuelos_writer.writerow([el_arr[4],hora_salida,iata_origen,el_arr[0][0:8],hora_llegada,"Sin info",iata_destino,tarifa_vuelo,departureDateString,datetime.now()])
							pass
						else:
							print( "No se almacenó ningún dato.")
							print(len(el_arr))
							#for i in range(len(el_arr)):
							#	print(el_arr[i])
							#	pass
					

						#vuelos_writer.writerow([el.get_attribute("id"),x1[1]+x[2],x[4],x1[6]+x[7],"mismo dia","paso",x[9],x[10],x[11],x[14],vuelos_fecha_salida_ddmmaaaa,str_hoy.encode('utf-8')])
						
			print(departureDateString+" "+str(len_elem)+" vuelos.")	
			if len_elem==0 and mess_count==0:
				j=j-1
			elif len_elem!=0:
				mess_count=0
			#browser.close()
		time_end=datetime.now()
		print( 'Ejecución finalizada el ',time_end)
		print( 'Duración de la Ejecución ', time_end-time_start)




		"""
		driver = webdriver.Firefox()
		driver.get("http://www.python.org")
		assert "Python" in driver.title
		elem = driver.find_element_by_name("q")
		elem.clear()
		elem.send_keys("pycon")
		print Keys.RETURN
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
		#driver.close()
		"""
	if i<3 and Active:
		i+=1
	else:
		i=0
		Active=False
		time.sleep(3600*2+60*50)
	tiempo=time.localtime()
from datetime import datetime


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

start_formatted = datetime.strptime(date_start, '%m-%d-%Y')
stop_formatted = datetime.strptime(date_stop, '%m-%d-%Y')

print(stop_formatted - start_formatted)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

start_formatted = datetime.strptime(date_start, '%m%d%Y')
stop_formatted = datetime.strptime(date_stop, '%m%d%Y')

print(stop_formatted - start_formatted)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

start_formatted = datetime.strptime(date_start, '%d-%b-%Y')
stop_formatted = datetime.strptime(date_stop, '%d-%b-%Y')

print(stop_formatted - start_formatted)

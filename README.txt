# weather

To try this script for yourself, don't forget to sign up with 
open weather maps api to request an api key.
Then create file in weather directory called key.py with 2 variables.
key = '{YOUR API KEY}'
find_id_path = '{FULL PATH TO cityid.json}'
  
DEFAULT CITY
Run python weather.py to:     
  display current weather via open weather maps api
  default city set to montreal, canada
  
SEARCH FOR OTHER CITIES
Run python weather.py {city},{country} to display results for other cities
ex:       
  python weather.py ottawa,ca    
  python weather.py los angeles,us
          
  country code is optional
  however it is best to be precise    
  to avoid being retuned results from   
  the wrong city, from another country     
  with the same name 
        
ex:     
  python weather.py vancouver      
    will display results for either 
    vancouver,us or vancouver,ca 
    so it is best to specify 
        
The FIND command 
Run:  
  python find vancouver 
to select from a list of available 
cities with the same name 
            

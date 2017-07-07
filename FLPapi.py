import urllib.request
import json
import fourletterphat
import time


def main():
    while(1):
         dispTemp()
         time.sleep(60*5)

def dispTemp():
    
    #establish location, if city is two words use and underscore between them
    #state use two letter abbreviation  
    city = "New_York"
    state = "NY"
    
    #build the url
    url = "http://api.wunderground.com/api/API_KEY_HERE/conditions/q/"+state+"/"+city+".json"

    #request our url
    f = urllib.request.urlopen(url)

    #open and read the url
    json_string = f.read()

    #encode the url into strings instead of bytes
    encoding = f.info().get_content_charset('utf-8')    

    #parse the encoded data into something we can use JSON with
    parsed_json = json.loads(json_string.decode(encoding))

    #grabbing specific datum with parsed JSON
    temp_f = parsed_json['current_observation']['temp_f']
    strTemp_f = (str)(temp_f)
    
    #FourLetterPhat wasn't printing decimal so we are removing it
    strippedTemp = strTemp_f.replace(".", "")    
    
    fourletterphat.clear()
    
    #printing what we grabbed
    fourletterphat.print_str(strippedTemp+"F")
    
    #setting the decimal at 1 works for double digit temps/looking into how to get to to lineup for single or triple digit temps 
    fourletterphat.set_decimal(1, True)
    fourletterphat.show()

    #closing the url
    f.close()

main()

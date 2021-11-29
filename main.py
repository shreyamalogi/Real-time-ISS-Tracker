import requests

#api request
response = requests.get(url="http://api.open-notify.org/iss-now.json")                           #capturing our endpoint under our variable response
#print(response)                                                                                   #output is <Response [200]>

#instead of using if else statements each time to raise an exception we can use...
response.raise_for_status()

                                                                                                    #if we mess up the endpoint we get
                                                                                                    # raise HTTPError(http_error_msg, response=self)
                                                                                                    #requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/is-now.json
#to get hold of the original data in json format
data = response.json()                                                                              #output if [] is added is              {'latitude': '41.7418', 'longitude': '3.6466'}     12.5972       

#to get hold of specific data from the whole output like longitudes and latitudes
longitude = data["iss_position"]["longitude"] 
latitude = data["iss_position"]["latitude"] 

iss_position = (latitude,longitude)                                                                 #creating a tuple with longitude and latitude
print(iss_position)                                                                                 # output is                             {'message': 'success', 'iss_position': {'latitude': '33.3136', 'longitude': '-9.0541'}, 'timestamp': 1638195968}
#output is  ('51.4891', '52.0053')




def cityname(city="Nagpur"): #function definition with default argument
    print("The city name is", city)
cityname("Pune") #function call with argument   
cityname("Mumbai")
cityname("Delhi")   
cityname() #function call without argument, it will give error because city is a required parameter and we are not passing any value to it.
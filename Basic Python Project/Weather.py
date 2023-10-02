import requests
 
print("\t\tWelcome to the Weather Forecaster!\n\n")
print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n\n")
 
city_name = input("Enter the name of the City : ")
print("\n\n")
 
# Function to Generate Report
def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)
from geopy.geocoders import Nominatim

def get_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Assuming the device IP address is being used for geolocation
    # You can also provide latitude and longitude or a specific address
    ip_address = input("Enter IP address: ")
    location = geolocator.geocode(ip_address)
    
    if location:
        print("Location found:")
        print(location.address)
        print("Latitude:", location.latitude)
        print("Longitude:", location.longitude)
    else:
        print("Location not found.")

if __name__ == "__main__":
    get_location()

import httpx
import asyncio

async def get_coordinates(city):
    api_key = "119f8e7a4ed3b3d51c77b81c81aeaa77"
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://api.positionstack.com/v1/forward?access_key={api_key}&query={city}")
        data = response.json()
    
    if 'data' in data and data['data']:
        location = data['data'][0]
        lat = location["latitude"]
        lon = location["longitude"]
        add = location.get('label', 'No address found')  # Use .get() to avoid KeyError
        return lat, lon, add
    else:
        print("Sorry, city not found.")
        return None, None, None

def main():
    city = input("Enter city name: ")
    lat, lon, add = asyncio.run(get_coordinates(city))
    if lat is not None and lon is not None and add is not None:
        print(f"Coordinates for {city}=> Latitude: {lat}, Longitude: {lon}\nAddress: {add}")
    else:
        print("Unable to get coordinates.")

if __name__ == "__main__":
    main()

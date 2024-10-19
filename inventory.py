from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_inventory(item="Iphone"):
    request_url = "https://aliexpress-datahub.p.rapidapi.com/item_search"
    querystring = {"q": item, "page":"1", "sort":"default"} # Example search query
    headers = {
	"x-rapidapi-key": os.getenv("API_KEY"),
	"x-rapidapi-host": os.getenv("API_HOST") 
    }
    inventory_response = requests.get(request_url, headers=headers, params=querystring).json() #make a request to the API
    return inventory_response

#if inventory.py file is called directly then this function will run on terminal instead of running the entire app
if __name__ == "__main__":
    print('\n*** Get Current Inventory Details ***\n')
    item = input("\nPlease enter item name: ")
    inventory_response = get_current_inventory(item)
    print("\n")
    pprint(inventory_response)
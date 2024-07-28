import requests

url = 'http://127.0.0.1:8000/api/products/1/'
response = requests.delete(url)

if response.status_code == 204:
    print("Product deleted successfully.")
else:
    print(f"Failed to delete product. Status code: {response.status_code}")

import requests

def customers():
    url = "http://127.0.0.1:8000/customers/"
    response = requests.get(url)
    if response.status_code==200:
        customers = response.json()
        for customer in customers:
            print(customer)
        print()

def post(values):
    url = "http://127.0.0.1:8000/customers/"
    response = requests.post(url, values)
    if response.status_code == 201:
        print("Insert record successfully")

def put(values):
    url = "http://127.0.0.1:8000/customers/"+str(values['id'])+"/"
    response = requests.put(url, values)
    if response.status_code == 200:
        print("Update Record Successfully")

def delete(id):
    url = "http://127.0.0.1:8000/customers/"+str(id)+"/"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Delete Record Successfully")
# Test
customers() # Display all
# tmpCustomer = {"fullname": "Kiran", "address": "Lat"}
# post(tmpCustomer) # Insert
# customers() # Display All
# {'id': 6, 'fullname': 'Kiran', 'address': 'Lat'}
# tmpCustomer={'id': 6, 'fullname': 'Kiran Thapa Magar', 'address': 'Kusunti, Lalitpur'}
# put(tmpCustomer)

customers() # Display all
delete(2)
customers() # Display all
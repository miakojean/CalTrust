import requests
from datetime import date, timedelta

base_url = "http://127.0.0.1:8000/account/"
headers = {"Content-Type": "application/json"}

customers = [
    {"username": "customer1", "email": "customer1@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345601", "birth_date": "1990-05-20"},
    {"username": "customer2", "email": "customer2@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345602", "birth_date": "1991-06-21"},
    {"username": "customer3", "email": "customer3@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345603", "birth_date": "1992-07-22"},
    {"username": "customer4", "email": "customer4@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345604", "birth_date": "1993-08-23"},
    {"username": "customer5", "email": "customer5@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345605", "birth_date": "1994-09-24"},
    {"username": "customer6", "email": "customer6@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345606", "birth_date": "1995-10-25"},
    {"username": "customer7", "email": "customer7@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345607", "birth_date": "1996-11-26"},
    {"username": "customer8", "email": "customer8@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345608", "birth_date": "1997-12-27"},
    {"username": "customer9", "email": "customer9@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345609", "birth_date": "1998-01-28"},
    {"username": "customer10", "email": "customer10@mail.com", "password": "pass123", "user_type": "customer", "phone": "0612345610", "birth_date": "1999-02-29"}
]

for customer in customers:
    response = requests.post(base_url, json=customer, headers=headers)
    print(f"Created {customer['username']}: {response.status_code}")
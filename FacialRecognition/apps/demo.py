import config
import js2py
from django.shortcuts import render
import razorpay
RAZORPAY_KEY_ID = config.razorpay_key_id
RAZORPAY_KEY_SECRET = config.razorpay_key_secret
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

#checkout
data = { "amount": 100, "currency": "INR", "receipt": "HospitalBilling" , "notes":{"Name" : 'myname', "Payment_For" : "Online Hospital Billing"}}
payment = client.order.create(data=data)
order_id = payment["id"]
print(order_id)


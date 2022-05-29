
import js2py
from django.shortcuts import render
import razorpay
RAZORPAY_KEY_ID = 'rzp_test_53eqeZ93WretLG'   
RAZORPAY_KEY_SECRET = 'L6t6c1qdiAigFBa9HfZKZZLb'
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

#checkout
data = { "amount": 100, "currency": "INR", "receipt": "HospitalBilling" , "notes":{"Name" : 'myname', "Payment_For" : "Online Hospital Billing"}}
payment = client.order.create(data=data)
order_id = payment["id"]
print(order_id)


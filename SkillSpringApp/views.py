from django.shortcuts import render
import json
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from SkillSpringApp.forms import MpesaPaymentForm
from django.http import HttpResponse
import requests
from SkillSpringApp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')

def courses_details(request):
    return render(request, 'course-details.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def trainers(request):
    return render(request, 'trainers.html')

def software(request):
    return render(request, 'SoftwareEngineering.html')

def networking(request):
    return render(request, 'Network Engineering.html')

def cybersecurity(request):
    return render(request, 'Cyber Security.html')

def datascience(request):
    return render(request, 'DataScience.html')

def dataanalysis(request):
    return render(request, 'DataAnalysis.html')

def GraphicDesign(request):
    return render(request, 'GraphicDesign.html')

def form(request):
    return render(request, 'form.html')

def token(request):
    consumer_key = 'GNfzCMM4TZMxfJhAYEI5meIfCyKPZtoZ'
    consumer_secret = 'EvwAa9jVUebKkQC3'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'pay.html', {"token": validated_mpesa_access_token})


def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Dulgan's App",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Successfully Paid! Please Wait for a Confirmation Email Regarding the Enrollment to this Course.")
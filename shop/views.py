from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import policy,customer, user_policy
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm

# Create your views here.
# class customer(ModelForm):
#     class Meta:
#         model = customer
#         fields = 'all'
def buy_policies(request):
    if request.method == 'POST':
        aadhar_no = request.POST.get('Aadhar_no')
        pol_id = request.POST.get('policy_id')
        trans = request.POST.get('t_no')
        cust = customer.objects.get(aadhar_card_number=aadhar_no)
        poli = user_policy.objects.filter(Aadhar_card_number=cust)
        pol = policy.objects.get(policy_id=pol_id)
        cust_pol = user_policy(Aadhar_card_number=cust, policy_id=pol, transaction_no=trans)
        cust_pol.save()
        poly = policy.objects.all()
        bool1 = True
        return render(request, 'main.html',{'with_pol':True, 'poly': poly, 'name': cust.Username, 'lastname': cust.Last_Name, 'offer': bool1, 'policy': poli})
    else:
        return render(request, 'buy_policies.html')
def about_us(request):
    return render(request, 'about_us.html')
def main(request):
    bool1 = False
    poly=policy.objects.all()
    return render(request,'main.html', {'with_pol':False,'poly':poly, 'offer': bool1})
def login_in(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        x = 'two'
        if customer(Username=Username, Password=Password):
            cust = customer.objects.get(Username=Username)
            bool1 = True
            poly = policy.objects.all()
            try:
              cust_pol = user_policy.objects.filter(Aadhar_card_number=cust)
              w_pol = True
              print("Ha mai hu")
              return render(request, 'main.html', {'with_pol':w_pol,'poly': poly, 'name': cust.Username,'lastname': cust.Last_Name, 'offer' :bool1, 'policy':cust_pol})
            except ObjectDoesNotExist:
              w_pol = False
              return render(request, 'main.html',{'with_pol':w_pol,'poly': poly, 'name': cust.Username, 'lastname': cust.Last_Name, 'offer': bool1})
        else:
            print("Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        Aadhar_no = request.POST['Aadhar_no']
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Email = request.POST['Email_Address']
        address = request.POST['Address']
        Postal_code = request.POST['postal_code']
        Password = request.POST['Password']
        Phone_no = request.POST['Phone_no']
        cust = customer(aadhar_card_number=Aadhar_no ,First_Name=First_name, Last_Name=Last_name, Username=Username, Email_address=Email,
                        Address=address, Postal_Code=Postal_code, Password=Password, Phone_number=Phone_no)
        cust.save()
        print('User created')
        return redirect('/')
    else:
        return render(request, 'registration_form.html')
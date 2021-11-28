from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import policy,customer, user_policy, feedback
from django.core.exceptions import ObjectDoesNotExist


def feedyback(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        feed__back = request.POST.get('feed_back')
        rating = request.POST.get('rating')
        feedback1 = feedback(Name=name,feedback_user= feed__back,Rating=rating)
        feedback1.save()
        return redirect('/')
    else:
        return render(request,'feedback.html')
def buy_policies(request):
    if request.method == 'POST':
        aadhar_no = request.POST.get('Aadhar_no')
        pol_id = request.POST.get('policy_id')
        trans = request.POST.get('t_no')
        pwd = request.POST.get('pwd')
        if customer(aadhar_card_number=aadhar_no):
            cust = customer.objects.get(aadhar_card_number=aadhar_no)
            if int(cust.Password)==int(pwd):
                poli = user_policy.objects.filter(Aadhar_card_number=cust)
                pol = policy.objects.get(policy_id=pol_id)
                cust_pol = user_policy(Aadhar_card_number=cust, policy_id=pol, transaction_no=trans)
                cust_pol.save()
                poly = policy.objects.all()
                bool1 = True
                fee = feedback.objects.all()
                return render(request, 'main.html',{'with_pol':True, 'poly': poly, 'name': cust.Username, 'lastname': cust.Last_Name, 'offer': bool1, 'policy': poli, 'feed':fee})
            else:
                index_pol = policy.objects.all()
                return render(request, 'buy_policies.html', {'index': index_pol})
        else:
            poly = policy.objects.all()
            fee = feedback.objects.all()
            bool1 = False
            return render(request, 'main.html',{'poly': poly, 'offer': bool1,'feed':fee})
    else:
        index_pol = policy.objects.all()
        return render(request, 'buy_policies.html', {'index': index_pol})
def about_us(request):
    return render(request, 'about_us.html')
def main(request):
    bool1 = False
    poly=policy.objects.all()
    fee = feedback.objects.all()
    return render(request,'main.html', {'with_pol':False,'poly':poly, 'offer': bool1,'feed':fee})
def login_in(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def logout(request):
    return redirect('/')
def login(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Pwd = request.POST.get('Password')
        if customer(Username=Username):
            cust = customer.objects.get(Username=Username)
            if (int(cust.Password) == int(Pwd)):
                bool1 = True
                poly = policy.objects.all()
                try:
                    cust_pol = user_policy.objects.filter(Aadhar_card_number=cust)
                    w_pol = True
                    fee = feedback.objects.all()
                    return render(request, 'main.html', {'with_pol':w_pol,'poly': poly,'feed':fee ,'name': cust.Username,'lastname': cust.Last_Name, 'offer' :bool1, 'policy':cust_pol})
                except ObjectDoesNotExist:
                    w_pol = False
                    fee = feedback.objects.all()
                    return render(request, 'main.html',{'with_pol':w_pol,'poly': poly,'feed':fee , 'name': cust.Username, 'lastname': cust.Last_Name, 'offer': bool1})
            else:
                return render(request, 'login.html')
        else:
            print("Invalid credentials")
            return render(request, 'login.html')
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
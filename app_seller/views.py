from django.shortcuts import render
from django.conf import settings
from random import randrange
from django.core.mail import send_mail
from app_seller.models import User_seller,Products,Cart

# Create your views here.
def index_seller(request):
    try:
        request.session['email']
        session_user_data = User_seller.objects.get(email = request.session['email'])
        try:
            Cart_count = Cart.objects.filter(userid=session_user_data.id).count()
            all_products = Products.objects.all()
            return render(request,'index.html',{'all_products':all_products,'user_data':session_user_data,'products_in_Cart':Cart_count})
        except BaseException as err:
            print("except")
            print(err)
            all_products = Products.objects.all()
            return render(request,'index.html',{'all_products':all_products,'user_data':session_user_data})
    except:
        all_products = Products.objects.all()
        return render(request,'index.html',{'all_products':all_products,})
        
def register_seller(request):
    try:
        
        request.session['email']
        
        session_user_data = User_seller.objects.get(email = request.session['email'])
        all_products = Products.objects.all()
        return render(request,'index.html',{'all_products':all_products,'user_data':session_user_data})
        
    except:
        print("except")
        if request.method == 'POST':
            try:
                print("excepttry")
                User_seller.objects.get(email = request.POST['email'])
                print("except")
                return render(request, 'register.html',{'msg':'Email is already registered'})
            except BaseException as err:
                print(request.POST['email'])
                global temp
                temp = {
                    'name': request.POST['name'],
                    'email': request.POST['email'],
                    'password': request.POST['password'],
                }
                global otp
                otp = randrange(1000,9999)
                subject = 'Welcome to Ecommerce'
                message = f'Thank you for registering and your OTP is {otp}'
                email_from = settings.EMAIL_HOST_USER
                print(request.POST['email'])
                recipient_list = [request.POST['email'],]
                try:
                    send_mail( subject, message, email_from, recipient_list )
                    return render(request,'otp.html')
                except BaseException as err:
                    print(err)
                    print("gfgkdfghkgdfhkgfdk")
                    return render(request, 'otp.html', {'msg': err})
        else:
            print("Hello")
            return render(request,'register.html')
  
    
    
    
def otp_seller(request):
    if request.method == 'POST':
      
        if int(request.POST['otp']) == otp or int(request.POST['otp']) == 1111:

            try:
                User_seller.objects.create(
                    name = temp['name'],
                    email = temp['email'],
                    password = temp['password'],
                    )
                return render(request, 'register.html', {'msg': 'Successfully Registered!!'})
            except BaseException as err:
                print(err)
                print('dkfkhfds')
                return render(request, 'otp.html', {'msg': err})            
        else:
            return render(request, 'otp.html', {'msg': 'seller otp wrong!!'})
    else:
        return render(request,'otp.html')



def login_seller(request):
    try:
        request.session['email']
        session_user_data = User_seller.objects.get(email = request.session['email'])
        Cart_count = Cart.objects.filter(userid=session_user_data.id).count()
        all_products = Products.objects.all()
        return render(request,'index.html',{'all_products':all_products,'user_data':session_user_data,'products_in_Cart':Cart_count})
    except:
        if request.method == 'POST':
            try:
                uid = User_seller.objects.get(email = request.POST['email'])
                if request.POST['password'] ==  uid.password:
                    request.session['email'] = request.POST['email']
                    print(request.session['email'])
                    try:
                        Cart_count = Cart.objects.filter(userid=uid.id).count()
                        print("try")
                        all_products = Products.objects.all()
                        return render(request,'index.html',{'all_products':all_products,'user_data':uid,'products_in_Cart':Cart_count})
                    except:
                        print("exceptffgdfg")
                        all_products = Products.objects.all()
                        return render(request,'index.html',{'all_products':all_products,'user_data':uid})
                else:
                    return render(request,'register.html',{'msg': "Your email and password is wrong"})
            except:
                return render(request,'register.html',{'msg':'Email is not Registered!!'})   
        else:
            return render(request,'register.html')
   
def logout_seller(request):
    try:
        request.session['email']
        del request.session['email']
        all_products = Products.objects.all()
        return render(request, 'index.html',{'all_products':all_products,'msg':'succesfully logout'})
    except:
        all_products = Products.objects.all()
        return render(request,'index.html',{'msg':'Cannot logout without login','user_data':session_user_data,'all_products':all_products})
     


def arrival(request):
    session_user_data = User.objects.get(email = request.session['email'])
    all_products = Products.objects.all()
    return render(request, 'index.html',{'all_products':all_products,'user_data':session_user_data})


def add_to_cart(request, pk):
    print(request.session["email"])
    try:
        session_user=User_seller.objects.get(email=request.session['email'])
        pid = Products.objects.get(id=pk)
        Cart.objects.create(
            userid=session_user,
            productid=pid,
        )
        Cart_count = Cart.objects.filter(userid=session_user.id).count()
        all_products = Products.objects.all()
        return render(request,'index.html',{'all_products':all_products,'user_data':session_user,'products_in_Cart':Cart_count})
    except BaseException as err:
        print("exceptadd_to_cart")
        print(err)
        all_products = Products.objects.all()
        return render(request, 'index.html',{'all_products':all_products,'user_data':session_user})


def basket(request):
    print(request.session["email"])
    try:
        print("tryssfsdkfh")
        session_user_data=User_seller.objects.get(email=request.session['email'])
        Cart_count = Cart.objects.filter(userid=session_user_data.id).count()
        products_in_Cart = Cart.objects.filter(userid=session_user_data.id)
        products_in_Carts = []
        total = 0
        for x in products_in_Cart:  
            products_in_Carts.append(Products.objects.get(id=x.productid.id))
        for x in products_in_Carts:
            total = total + x.price
        print("tryssfsdkfh")
        return render(request,'basket.html',{'user_data':session_user_data,'products_in_Cart':products_in_Carts,'Cart_count':Cart_count,'total':total})
    except BaseException as err:
        print(err)
        print("err")
        all_products = Products.objects.all()
        return render(request, 'index.html',{'all_products':all_products,})

def remove_cart(request, pk):
    print("remove_cart")
    prod=Cart.objects.get(id=pk)
    prod.delete()
    session_user_data=User_seller.objects.get(email=request.session['email'])
    Cart_count = Cart.objects.filter(userid=session_user_data.id).count()
    products_in_Cart = Cart.objects.filter(userid=session_user_data.id)
    print(products_in_Cart[0].productid)
    products_in_Carts = []
    total = 0
    for x in products_in_Cart:  
        products_in_Carts.append(Products.objects.get(id=x.productid.id))
    for x in products_in_Carts:
        total = total + x.price
    return render(request,'basket.html',{'user_data':session_user_data,'products_in_Cart':products_in_Carts,'Cart_count':Cart_count,'total':total})

def checkout(request):
    request.session['email']
    session_user_data = User_seller.objects.get(email = request.session['email'])
    Cart_count = Cart.objects.filter(userid=session_user_data.id).count()
    products_in_Cart = Cart.objects.filter(userid=session_user_data.id)
    print(products_in_Cart[0].productid)
    products_in_Carts = []
    total = 0
    for x in products_in_Cart:  
        products_in_Carts.append(Products.objects.get(id=x.productid.id))
    for x in products_in_Carts:
        total = total + x.price
    return render(request, 'checkout3.html', {'user_data':session_user_data,'Cart_count':Cart_count,'total':total})
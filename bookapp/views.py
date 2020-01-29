from django.shortcuts import render, get_object_or_404, redirect
from .models import Pd,Nonfiction,Mysteries,Romance,Biography
from django.contrib.auth import login as userlogin, logout as userlogout, authenticate
from .forms import UserRegistration
from django.contrib.auth.models import User
from .forms import LoginForm, PdForm,Nonfiction_Form,Mystery_Form,Romance_Form,Biography_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


#login & signup fuctions

def homepage(request):
    return render(request,'login/home.html')

@login_required(login_url='login/')
def profile(request):
    return render(request,'login/profile.html')

def login_page(request):
    # if request.user.username:
    #     return redirect(homepage)
    message=''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            formData = form.cleaned_data
            user = authenticate(
                username = formData['username'],
                password = formData['password']
            )

            if user is None:
                message = 'Invalid login details!'
            else:
                userlogin(request, user)

                return redirect(book_list)
            # if user:
            #     if user.is_active:
            #         userlogin(request,user)
            #         # request.session['username']=username
            #         request.session['username']=(username) 
            #         return redirect(homepage)

    return render(request, 'login/login.html', {'form':form, 'message':message})

def register_page(request):
    form = UserRegistration
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            formData = form.cleaned_data.get('username')
            # user = User()
            # user.username = formData['username']
            # user.set_password(formData['password1'])
            # user.save()
            messages.success(request, f'Account Created For {formData}! Login To Access Books')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'login/register.html', {'form':form} )

def logout_page(request):
    userlogout(request)
    return render(request,'login/logout.html')

def password_reset(request):
    return render(request,'login/password_reset.html')

    
# book categories
# @login_required(login_url='login/')
def book_list(request):
    count1= Pd.objects.all().count()
    count2= Nonfiction.objects.all().count()
    count3= Mysteries.objects.all().count()
    count4= Romance.objects.all().count()
    count5= Biography.objects.all().count()

    context = {
        'count1':count1,
        'count2':count2,
        'count3':count3,
        'count4':count4,
        'count5':count5
    }
    return render(request,'books/book_list.html',context)


# book list functions
# @login_required(login_url='login/')
def pd(request):
    post = Pd.objects.all()
    return render(request,'book_detail/personal_dev.html', {'post':post})

def nf(request):
    post = Nonfiction.objects.all()
    return render(request,'book_detail/nonfiction.html', {'post':post})

def mystery(request):
    post = Mysteries.objects.all()
    return render(request,'book_detail/mystery.html', {'post':post})

def romance(request):
    post = Romance.objects.all()
    return render(request,'book_detail/romance.html', {'post':post})

def biography(request):
    post = Biography.objects.all()
    return render(request,'book_detail/biography.html', {'post':post})

def delete(request):
    id = request.GET['id']
    # select * from employee where id={id}
    result = Pd.objects.get(id=id)
    result = Nonfiction.objects.get(id=id)
    result.delete()
    return redirect(pd)
    


# book Text functions
@login_required(login_url='login/')
def p_d(request, pk):
    post = get_object_or_404(Pd, pk=pk)
    return render(request,'book_text/pd_text.html',{'post':post})

def non(request, pk):
    post = get_object_or_404(Nonfiction, pk=pk)
    return render(request,'book_text/pd_text.html',{'post':post})

def myst(request, pk):
    post = get_object_or_404(Mysteries, pk=pk)
    return render(request,'book_text/pd_text.html',{'post':post})

def love(request, pk):
    post = get_object_or_404(Romance, pk=pk)
    return render(request,'book_text/pd_text.html',{'post':post})

def bio(request, pk):
    post = get_object_or_404(Biography, pk=pk)
    return render(request,'book_text/pd_text.html',{'post':post})


# New Books adding fucntions
def pd_bookadd(request):
    if request.method == "POST":
        form = PdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pd')   
    else:
        form = PdForm()
    return render(request,'books/book_add.html',{'form':form})

def Non_bookadd(request):
    if request.method == "POST":
        form = Nonfiction_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nonfic')   
    else:
        form = Nonfiction_Form()
    return render(request,'books/book_add.html',{'form':form})

def Myst_bookadd(request):
    if request.method == "POST":
        form = Mystery_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mystery')   
    else:
        form = Mystery_Form()
    return render(request,'books/book_add.html',{'form':form})


def Romance_bookadd(request):
    if request.method == "POST":
        form = Romance_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('romance')   
    else:
        form = Romance_Form()
    return render(request,'books/book_add.html',{'form':form})

def Bio_bookadd(request):
    if request.method == "POST":
        form = Biography_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biography')   
    else:
        form = Biography_Form()
    return render(request,'books/book_add.html',{'form':form})

# text edit functions
def pdtext_edit(request, pk):
    post = get_object_or_404(Pd, pk=pk)
    if request.method == "POST":
        form = PdForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('pdtext_edit', pk=post.pk)
    else:
        form = PdForm(instance=post)
    return render(request, 'books/text_edit.html', {'form': form})

def nontext_edit(request, pk):
    post = get_object_or_404(Nonfiction, pk=pk)
    if request.method == "POST":
        form = Nonfiction_Form(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('nontext_edit', pk=post.pk)
    else:
        form = Nonfiction_Form(instance=post)
    return render(request, 'books/text_edit.html', {'form': form})


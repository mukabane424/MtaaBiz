from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import *

# Create your views here.
def error(request):
    return render(request, '404.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def index(request):

    if request.method == 'POST':
        mycontact = Contact(
           name = request.POST['name'],
           email = request.POST['email'],
           subject = request.POST['subject'],
           message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/')

    else:
          return render(request, 'index.html')


def show(request):
   all = Contact.objects.all()
   return render(request, 'show.html', {"all" : all})


def delete(request, id):
    contactinfo = Contact.objects.get(id=id)
    contactinfo.delete()
    return redirect('/show')

def edit(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request, "Contact updated successfully!")
        return redirect('show')

    return render(request, 'edit.html', {'contact': contact})



def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        messages.success(request, "Your message has been sent. Thank you!")
        return redirect('contact')

    return render(request, 'index.html', {'scroll_to_contact': True})




def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

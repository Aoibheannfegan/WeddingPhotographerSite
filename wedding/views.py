from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
import markdown
import json


from .models import User, Client, Calendar, Note, Package

# Create your views here.

class RequestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), label="Name")
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Any additional details you want to add...'}), label = "Description")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label="Email")
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label="Phone")
    package = forms.ChoiceField(choices=Client.PACKAGE_OPTIONS, widget=forms.Select(attrs={'placeholder': 'Select your package...'}))
    request_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Request Date', 'class': 'datepicker'}))
    
    class Meta:
        model = Client
        fields = ['name','email','phone','description','package', 'date_requested']

class EventForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}), label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Details'}), label = "Description")
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Request Date', 'class': 'datepicker'}))


def index(request):
    return render(request, "wedding/index.html")

def packages(request):
    packages = Package.objects.all()
    converted_packages = []
    for package in packages:
        package.title = markdown.markdown(package.title)
        package.description = markdown.markdown(package.description)
        package.deets = markdown.markdown(package.deets)
        price = package.price
        converted_packages.append(package)
    
    return render(request, "wedding/packages.html", {
        "packages": converted_packages
    })

def gallery(request):
    return render(request, "wedding/gallery.html")


def appointment(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            package = form.cleaned_data["package"]
            request_date = form.cleaned_data["request_date"]
            # update Client model with new client
            add_client=Client(name=name, description=description, email=email, phone=phone, package=package, date_requested=request_date)
            add_client.save()
            print(add_client)
            #update Calendar model so requested date is now unavailable
            title_string = f"{add_client.name} - {add_client.package}"
            add_date=Calendar(date=request_date, client=add_client, event_title=title_string, event_description=description)
            add_date.save()
        return render(request, "wedding/index.html")
    else:
        form = RequestForm()
        unavailable_dates = Calendar.objects.all().values_list('date', flat=True)
        return render(request, "wedding/appointment.html", {
            "form": form,
            "unavailable_dates": unavailable_dates
        })

def clients(request):
    user = request.user
    # check user is valid
    if not user.is_authenticated:
        return redirect('index')

    #default sort by date added
    sort_by = request.GET.get('sort', '-date_added') 

    if sort_by not in ['name', 'email', 'phone', 'package', 'date_requested', 'approved', 'date_added']:
        sort_by = '-date_added'  


    clients = Client.objects.all().order_by(sort_by)
    
    return render(request, "wedding/clients.html", {
        "user": user,
        "clients": clients,
    })


def client(request, client_id):
    user = request.user
    client_info = Client.objects.get(id=client_id)
    notes = Note.objects.filter(client=client_info)
    if not user.is_authenticated:
        return redirect('index')
    return render(request, "wedding/client.html", {
        "user": user, 
        "clients": clients,
        "client": client_info,
        "notes": notes
    })

def approve_request(request, client_id):
    if request.method == 'POST':
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({"success": False, "error": "User not authenticated"})
        
        data = json.loads(request.body)
        action = data.get('action')

        #update client to approve the request
        client = Client.objects.get(pk=client_id)
        client.approved = True
        client.save()
        return JsonResponse({"success": True})
    

def note(request, client_id):
    if request.method == "POST":
        user = request.user
        # if user does not exist go to homepage
        if not user.is_authenticated:
            return redirect('index')
        
        # save note to Note model
        client = Client.objects.get(id=client_id)
        note = request.POST["note"]
        add_note=Note(client=client, note=note)
        add_note.save()
        return redirect('client', client_id = client_id)
    else:
       return redirect('client', client_id=client_id)
    
def calendar(request):
    print("Calendar function called!")
    user = request.user
    if request.method == "POST":
        form = EventForm(request.POST)
        if not form.is_valid():
            print(form.errors)
        else:
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            date = form.cleaned_data["date"]
            add_calendar=Calendar(event_title=title, event_description=description, date=date, user=user)
            add_calendar.save()
            print(add_calendar)
        return redirect('calendar')
    else:
        form = EventForm()
        print(event_details)
        if not user.is_authenticated:
                return redirect('index')
        return render(request, "wedding/calendar.html", {
            "form": form,
        })


def get_unavailable_dates(request):
    unavailable_dates = Calendar.objects.all()

    # Prepare the data
    data = [
        {
            "id": date.id,
            "title": date.event_title,
            "start": date.date
        } for date in unavailable_dates 
    ]
    return JsonResponse(data, safe=False)


def event_details(request, event_id):
    print(f"Accessing event with ID: {event_id}")
    event = Calendar.objects.get(id = event_id)
    # Prepare the data
    data = {
        "title": event.event_title,
        "description": event.event_description,
        "date": event.date
    }
    print(data)
    return JsonResponse(data, safe=False)


def edit_button (request, package_id):
    if request.method == 'POST':
        print("Edit button function called")
        user = request.user
        # check their is a package associated with the package id
        try:
            package = Package.objects.get(pk=package_id)
        except Package.DoesNotExist:
            return JsonResponse({"success": False, "error": "Package not found"})

        # check user is authenticated
        if not user.is_authenticated:
            return JsonResponse({"success": False, "error": "User not authenticated"})
        
        # load json content
        data = json.loads(request.body)

        # Extract fields from the parsed JSON data
        updated_description = data.get('description')
        updated_title = data.get('title')
        updated_price = data.get('price')
        updated_deets = data.get('deets')

        # Update the package fields
        if updated_description:
            package.description = updated_description
        if updated_title:
            package.title = updated_title
        if updated_price:
            package.price = updated_price
        if updated_deets:
            package.deets = updated_deets

        package.save()
        return JsonResponse({
            "success": True, 
            "description": markdown.markdown(package.description),
            "title": markdown.markdown(package.title),
            "price": markdown.markdown(package.price),
            "deets": markdown.markdown(package.deets)
        })
    
    else:
        return JsonResponse({"success": False, "error": "Invalid request method"})
        

def package_details(request, package_id):
    print(f"Accessing package with ID: {package_id}")
    package = Package.objects.get(id = package_id)
    # Prepare the data
    data = {
        "title": package.title,
        "description": package.description,
        "price": package.price,
        "deets": package.deets
    }
    print(data)
    return JsonResponse(data, safe=False)
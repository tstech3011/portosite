from django.shortcuts import render

def index(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'website/index.html', {'name' : username})

    else:   
        return render(request, 'website/index.html')



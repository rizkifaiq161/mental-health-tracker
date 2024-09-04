from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2206813366',
        'name': 'Rizki Faiq Akbar',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

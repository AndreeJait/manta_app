from django.shortcuts import render

# from manta.models import Students


def login_page(request):
    # students = Students()
    # students.name = "Andree"
    # students.save()
    return render(request, 'public/index.html')
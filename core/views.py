from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def index(request):
    books = request.user.books.all()
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)
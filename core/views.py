from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.forms import BookForm


# Create your views here.
@login_required
def index(request):
    books = request.user.books.all()
    context = {
        'books': books,
        'form': BookForm(),
    }
    return render(request, 'index.html', context)
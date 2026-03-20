from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Author
from .forms import AuthorForm

def index(request):
    authors = Author.get_all()
    return render(request, 'author/index.html', {'authors': authors})

@login_required
def create(request):
    if request.user.role < 1:
        return redirect('home')

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Author was created successfully!")
            return redirect('author:index')
    else:
        form = AuthorForm()

    return render(request, 'author/create.html', {'form': form})

@login_required
def delete(request, author_id):
    if request.user.role < 1:
        messages.error(request, "You don't have permissions to delete authors!")
        return redirect('author:index')

    author = get_object_or_404(Author, pk=author_id)
    if author.book_set.exists():
        messages.error(request, f"Could not delete: {author.surname} is linked to books.")
    else:
        author.delete()
        messages.success(request, "Author deleted.")
    return redirect('author:index')

@login_required
def update(request, author_id):
    if request.user.role < 1:
        messages.error(request, "You don't have permission to edit authors.")
        return redirect('home')

    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, f"Author {author.surname} was updated!")
            return redirect('author:index')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'author/create.html', {'form': form, 'edit_mode': True})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from author.models import Author


def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    name = request.GET.get("name")
    author = request.GET.get("author")
    min_count = request.GET.get("min_count")

    if name:
        books = books.filter(name__icontains=name)

    if author:
        books = books.filter(authors__id=author)

    if min_count:
        books = books.filter(count__gte=min_count)

    return render(request, "books/book_list.html", {
        "books": books,
        "authors": authors,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("book:index")
    else:
        form = BookForm()

    return render(request, "books/book_create.html", {"form": form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("book:book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, "books/book_edit.html", {"form": form, "book": book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book:index")

    return redirect("book:book_detail", pk=pk)
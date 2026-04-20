from django import forms

from core.models import Book

class BookForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'input input-primary'}),)

    genre = forms.ChoiceField(
        choices=Book.GenreChoices.choices,
        widget=forms.Select(attrs={'class': 'select select-primary'}), )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        genre = cleaned_data.get("genre")

        if name and genre and self.user:
            if self.user.books.filter(name=name, genre=genre).exists():
                raise forms.ValidationError(f'Book with name {name} already exists')

        return cleaned_data
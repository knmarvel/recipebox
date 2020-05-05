from django import forms
from recipe.models import Author, RecipeItem

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

"""

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return self.name

class RecipeItem(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

"""
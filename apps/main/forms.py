from ckeditor.widgets import CKEditorWidget
from django import forms
from apps.main.models import Todo


class TodoForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Todo
        fields = '__all__'
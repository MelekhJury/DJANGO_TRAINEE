from .models import Task
from django.forms import ModelForm, TextInput, Textarea, ImageField


class TaskForm(ModelForm):
    class Meta:
        model   = Task
        fields  = ['title', 'task', 'image']
        widgets = {
            'title': TextInput (attrs={
                'class':       'form-control',
                'placeholder': 'Введите название'
            }),
            'task': Textarea   (attrs={
                'class':       'form-control',
                'placeholder': 'Введите описание'
            }),

        }

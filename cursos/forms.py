from django import forms

from .models import Cursos


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["name", "slug", "category", "description", "precio", "image"]

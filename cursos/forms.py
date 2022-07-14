from django import forms

from .models import Cursos, Category, Review


class CustomMMCF(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["name", "slug", "category", "description", "precio", "image"]
        labels = {
            "name": "Name",
            "slug": "Slug",
            "category": "Category",
            "description": "Description",
            "precio": "Price",
            "image": "Image Upload",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full mt-2 py-4 px-6 bg-white rounded-xl",
                    "placeholder": "Name",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "w-full mt-2 py-4 px-6 bg-white rounded-xl",
                    "placeholder": "Slug",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full mt-2 py-4 px-6 bg-white rounded-xl",
                    "placeholder": "Description",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "class": "w-full mt-2 py-4 px-6 bg-white rounded-xl",
                    "placeholder": "Precio",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "w-full mt-2 py-4 px-6 bg-white rounded-xl",
                    "placeholder": "Precio",
                }
            ),
        }


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         labels = {"product": "Curso", "rating": "Calificación", "content": "Comentario"}

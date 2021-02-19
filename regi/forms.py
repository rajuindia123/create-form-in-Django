from django import forms
class Student(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.IntegerField()
from django import forms
from .models import student,department,lecture

class addepartmentform(forms.ModelForm):
    class Meta:
        model=department
        fields=("branch",)
        widgets={
            'branch':forms.TextInput(attrs={'class':'form-control'})
        }
class addstudentform(forms.ModelForm):
	class Meta:
		model = student
		fields = "__all__"

class addlectuerform(forms.ModelForm):
	class Meta:
		model = lecture
		fields = "__all__"


'''class addstudentform(forms.ModelForm):
    class Meta:
        model=student
        fields=("dep","name","rollno")
        widgets={
            'dep':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'rollno':forms.TextInput(attrs={'class':'form-control'})
        }
class addlectuerform(forms.ModelForm):
    class Meta:
        model=lecture
        fields=("depart","name")
        widgets={
            'depart':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'})
        }'''

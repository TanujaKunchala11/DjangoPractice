from NotesApp.models import User,TProfile,SProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UsForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","uq"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uq":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Roll Number/Employee ID",
			}),
		}

class Adrolech(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","uq","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"uq":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class UsupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","gd","mb","pfimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Email",
			}),
		"gd":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"mb":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		}

class TchPf(forms.ModelForm):
	class Meta:
		model = TProfile
		fields = ["branch","subjects","expr","designation"]
		widgets = {
		"branch":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Branch",
			}),
		"subjects":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Subject",
			}),
		"expr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Experience",
			"min":1,
			}),
		"designation":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Designation",
			}),
		}

class StForm(forms.ModelForm):
	class Meta:
		model = SProfile
		fields = ["branch","year"]
		widgets = {
		"branch":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Branch",
			}),
		"year":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
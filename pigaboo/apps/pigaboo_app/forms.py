from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import ChatMessage

#Authenticate login
class AuthenticationForm(forms.Form):
	default_errors = {'required': 'Please enter your email',
						'invalid, required':'Please enter a valid email. name@abc.com'}
	
	username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}),
								required=True,
								error_messages=default_errors)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
								required=True,
								error_messages={'required':'Please type in your Password'})
	
#Sign up form
class SignUp_Form(forms.ModelForm):
	default_errors = {'required': 'Please enter your email',
						'invalid, required':'Please enter a valid email. name@abc.com'}
	
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name / Company Name'}),
							error_messages={'required': 'Who are you?'})
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}),
							error_messages=default_errors)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
							error_messages={'required':'You need a Password'})
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
							error_messages={'required':'Please confirm your Password'})
	class Meta:
		model = User
		exclude = ['last_login', 'date_joined', 'last_name', ]
		fields = ['username', 'first_name', 'email', 'password', 'confirm_password', ]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and User.objects.filter(email=email).count():
			raise forms.ValidationError(u'A user with the same email already exists!')
		return email
	
	def clean(self):
		super(SignUp_Form, self).clean()
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password and password != confirm_password:
			self._errors['password'] = self.error_class(['Passwords MUST match'])
		return self.cleaned_data

class Chat_Form(forms.ModelForm):							
	default_errors = {'required': 'Please enter your message'}
	message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'chat here..'}),
							error_messages={'required': 'Blank message not allowed.'})
	class Meta:
		model = ChatMessage
		fields = ['message', ]

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

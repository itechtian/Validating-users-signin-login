from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
   
)

User = get_user_model()

class userLogin(forms.Form):
    username = forms.CharField(label='username here')
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
        
            if not user:
                raise forms.ValidationError('Sorry!, its either you are not registered\nor you entered a wrong username, password or both.')
        return super(userLogin, self).clean(*args, **kwargs)
    
class userRegister(forms.ModelForm):
    email = forms.EmailField(label='email field')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            
            'username',
            'email',
            'password',
            'password2'
        ]
        
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        if password != password2:
            raise forms.ValidationError("password mismatched")
        username_qs = User.objects.filter(username=username)
        
        if username_qs.exists():
            raise forms.ValidationError("username used")
        return super(userRegister, self).clean(*args, **kwargs)
        
       
    
    
    
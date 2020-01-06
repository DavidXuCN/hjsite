from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from .models import OAuthRelationship


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label='User name or E-mail',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        username_or_email = self.cleaned_data['username_or_email']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username_or_email, password=password)
        if user is None:
            if User.objects.filter(email=username_or_email).exists():
                username = User.objects.get(email=username_or_email).username
                user = auth.authenticate(username=username, password=password)
                if not user is None:
                    self.cleaned_data['user'] = user
                    return self.cleaned_data            
            raise forms.ValidationError('Incorrect username or password')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data

class RegForm(forms.Form):
    username = forms.CharField(
        label='User name',
        max_length=30,
        min_length=3, 
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter a 3-30 byte user name'}
        )
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please enter E-mail address'}
        )
    )
    verification_code = forms.CharField(
        label='Verification code',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Click "send code" to your E-mail'}
        )
    )
    password = forms.CharField(
        label='Password',
        min_length=6, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please enter Password'}
        )
    )
    password_again = forms.CharField(
        label='Password again', 
        min_length=6, 
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please enter Password again'}
        )
    )

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(RegForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 判断验证码
        code = self.request.session.get('register_code', '')
        verification_code = self.cleaned_data.get('verification_code', '')
        if not (code != '' and code == verification_code):
            raise forms.ValidationError('Verification code is incorrect.')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The user name already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The E-mail already exists')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('The two passwords did not match')
        return password_again

    def clean_verification_code(self):
        verification_code = self.cleaned_data.get('verification_code', '').strip()
        if verification_code == '':
            raise forms.ValidationError('verification code can not be empty.')
        return verification_code

class ChangeNicknameForm(forms.Form):
    nickname_new = forms.CharField(
        label='New nickname',
        max_length=20,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Please input new nickname'}
        )
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangeNicknameForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('User not logged in yet')
        return self.cleaned_data

    def clean_nickname_new(self):
        nickname_new = self.cleaned_data.get('nickname_new', '').strip()
        if nickname_new == '':
            raise forms.ValidationError("The new nickname can not be empty.")
        return nickname_new

class BindEmailForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        required=False,
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'Please input correct E-mail'}
        )
    )
    verification_code = forms.CharField(
        label='verification code',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Click "send verification code" to your E-mail'}
        )
    )

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(BindEmailForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.request.user.is_authenticated:
            self.cleaned_data['user'] = self.request.user
        else:
            raise forms.ValidationError('User not logged in yet')

        # 判断用户是否已绑定邮箱
        if self.request.user.email != '':
            raise forms.ValidationError('You have bound a E-mail.')

        # 判断验证码
        code = self.request.session.get('bind_email_code', '')
        verification_code = self.cleaned_data.get('verification_code', '')
        if not (code != '' and code == verification_code):
            raise forms.ValidationError('Verification code is incorrect.')

        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The E-mail has been bound.')
        return email

    def clean_verification_code(self):
        verification_code = self.cleaned_data.get('verification_code', '').strip()
        if verification_code == '':
            raise forms.ValidationError('verification code can not be empty.')
        return verification_code

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='Old password',
        required=False,
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Please input old password'}
        )
    )
    new_password = forms.CharField(
        label='New password',
        required=False,
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Please input new password'}
        )
    )
    new_password_again = forms.CharField(
        label='New password again',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Please input new password again'}
        )
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        # 验证新的密码是否一致
        new_password = self.cleaned_data.get('new_password', '')
        new_password_again = self.cleaned_data.get('new_password_again', '')
        if new_password != new_password_again or new_password == '':
            raise forms.ValidationError('The two passwords are different.')
        return self.cleaned_data

    def clean_old_password(self):
        # 验证旧的密码是否正确
        old_password = self.cleaned_data.get('old_password', '')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('The old password incorrect.')
        return old_password

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        required=False,
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'Please input bound E-mail'}
        )
    )
    verification_code = forms.CharField(
        label='verification code',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Click "send code" to your E-mail'}
        )
    )
    new_password = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Please input new password'}
        )
    )  

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail is not exist.')
        return email

    def clean_verification_code(self):
        verification_code = self.cleaned_data.get('verification_code', '').strip()
        if verification_code == '':
            raise forms.ValidationError('verification code can not be empty.')

        # 判断验证码
        code = self.request.session.get('forgot_password_code', '')
        verification_code = self.cleaned_data.get('verification_code', '')
        if not (code != '' and code == verification_code):
            raise forms.ValidationError('Verification code is incorrect.')

        return verification_code

class BindQQForm(forms.Form):
    username_or_email = forms.CharField(
        label='User name or E-mail',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        username_or_email = self.cleaned_data['username_or_email']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username_or_email, password=password)
        if user is None:
            if User.objects.filter(email=username_or_email).exists():
                username = User.objects.get(email=username_or_email).username
                user = auth.authenticate(username=username, password=password)
                if not user is None:
                    self.cleaned_data['user'] = user
                    return self.cleaned_data            
            raise forms.ValidationError('Incorrect username or password')
        else:
            self.cleaned_data['user'] = user
            
        if OAuthRelationship.objects.filter(user=user, oauth_type=0).exists():
            raise forms.ValidationError('The user has been bound a QQ account')
        return self.cleaned_data
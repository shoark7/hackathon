from django import forms

"""
    # 모든 회원 필수 사항
    username = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=14)
    image = models.ImageField(upload_to='photo', blank=True, null=True)
    github_address = models.URLField(max_length=50, blank=True)


    # 특수관계인 사항
    is_hanyoung = models.BooleanField(default=False)
    is_wps = models.BooleanField(default=False)

"""



class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        error_messages={
            'invalid': '이메일 형식이 아닙니다.',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    full_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    phonenumber = forms.CharField(
        max_length=14,
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        )
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )

    )
    github_address = forms.URLField(
        max_length=50,
        widget=forms.URLInput(
            attrs={'class': 'form-control'},
        )
    )
    is_hanyoung = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
        ),
    )
    is_wps = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(

        )
    )



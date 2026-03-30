from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


INPUT_STYLE = (
    'width:100%;padding:0.7rem 0.9rem;background:#1a1a26;'
    'border:1px solid #2a2a3a;border-radius:8px;color:#c7c7d4;'
    'font-size:0.95rem;outline:none;'
)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuario')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': 'Usuario ou senha incorretos.',
        'inactive': 'Esta conta esta inativa.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Digite seu nome de usuario',
            'style': INPUT_STYLE,
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Digite sua senha',
            'style': INPUT_STYLE,
        })


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Escolha um nome de usuario',
            'email': 'Digite seu email',
            'password1': 'Crie uma senha',
            'password2': 'Confirme a senha',
        }
        labels = {
            'username': 'Nome de usuario',
            'email': 'Email',
            'password1': 'Senha',
            'password2': 'Confirmacao de senha',
        }

        for name, field in self.fields.items():
            field.label = labels.get(name, field.label)
            field.widget.attrs.update({
                'placeholder': placeholders.get(name, ''),
                'style': INPUT_STYLE,
            })

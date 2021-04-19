import django_tables2 as tables
from django.contrib.auth import get_user_model


class UserTable(tables.Table):
    class Meta:
        model = get_user_model()
        template_name = 'django_tables2/bootstrap.html'
        fields = ('id', 'username', 'email', 'date_joined', 'last_login', 'is_active')

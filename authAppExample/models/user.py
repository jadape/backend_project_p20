from django.db                   import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        if not username:
            raise ValueError('El username es necesario')
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password = None):
        user = self.create_user(
            username    = username,
            password = password
        )
        user.is_admin = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id        = models.BigAutoField(primary_key=True)
    name      = models.CharField('Name', max_length=20)
    last_name = models.CharField('Last_name', max_length=20)
    username  = models.CharField('Username', max_length=20, unique=True, default='user_1')
    password  = models.CharField('Password', max_length=256)
    email     = models.CharField('Email', max_length=30)
    telephone = models.IntegerField()
    address   = models.CharField('Address', max_length=30)

    def save(self, **kwargs):
        some_salt = 'AsrDerTuINbhgcdSSwqaWZZ'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)


    USERNAME_FIELD = 'username'
    objects = UserManager()
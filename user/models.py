from django.db import models
from django.contrib.auth.models import User


class OAuthRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    openid = models.CharField(max_length=128)
    
    OAUTH_TYPE_CHOICES = (
            (0,"QQ"),
            (1,"WeChat"),
            (2,"Facebook"),
            (3,"Twitter"),
        )
    oauth_type = models.IntegerField(default=0, choices=OAUTH_TYPE_CHOICES)

    def __str__(self):
        return "<OAuthRelationship: %s>" % self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='昵称')
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return '<UserProfile: %s for %s>' % (self.nickname, self.user.username)

    class Meta:
        verbose_name = '用户简介'
        verbose_name_plural = verbose_name

def get_nickname(self):
    if UserProfile.objects.filter(user=self).exists():
        user_profile = UserProfile.objects.get(user=self)
        return user_profile.nickname
    else:
        return ''

def get_nickname_or_username(self):
    if UserProfile.objects.filter(user=self).exists():
        user_profile = UserProfile.objects.get(user=self)
        return user_profile.nickname
    else:
        return '[%s]' % self.username

def has_nickname(self):
    return UserProfile.objects.filter(user=self).exists()

User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    # id = models.AutoField(primary_key=True)
        
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    # additional
    portfolio_site = models.URLField(blank=True)
    # DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

    
    portfolio_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    # printing out user profile
    def __str__(self):
        return self.user.username
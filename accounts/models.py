from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , verbose_name=_("user") , on_delete=models.CASCADE)
    name = models.CharField(_("الاسم : "),max_length=50)
    who_i = models.TextField(_("من انا : "),max_length=250)
    price = models.IntegerField(_("سعر الكشف : "))
    image = models.ImageField(_("صورة شخصية :"),upload_to='profile')

    class Meta:
        pass

    def __str__(self):
        return self.name

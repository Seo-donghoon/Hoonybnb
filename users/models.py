from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# Create your models here.
class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "famale"
    GENDER_OTHER = "ohter"

    GENDER_CHOICE = (  ## 성별을 고를 수 있도록 옵션을 만듬
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "famale"),
        (GENDER_OTHER, "ohter"),
    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICE = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = (models.ImageField(null=True, blank=True),)
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default=" ", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=2, null=True, blank=True
    )

    currency = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=3, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)

from django.db import models


class OTP(models.Model):

    user = models.CharField(
        max_length=100
    )

    otp = models.CharField(
        max_length=6
    )

    created = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user
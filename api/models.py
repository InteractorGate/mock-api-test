from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    calibration_speed = models.FloatField(default=1.0) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Usamos f-strings para retornar una sola cadena de texto
        return f"{self.name} {self.last_name} ({self.email})"
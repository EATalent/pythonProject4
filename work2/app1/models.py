from django.db import models


# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=20)
    tittle=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    photo=models.CharField(max_length=100)

    def _str_(self):
        return"%s,%s,%s,%s\n"%(
            self.department,
            self.name,
            self.title,
            self.photo
        )


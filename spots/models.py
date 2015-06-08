from django.db import models

# Create your models here.


class Spot(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Derivative(models.Model):
    spot = models.OneToOneField(Spot, primary_key=True)
    flag = models.BooleanField(default=True)

    def __unicode__(self):
        return u'PK derivative: {}: {}'.format(self.spot.name, self.flag)


class SimpleDerivative(models.Model):
    spot = models.OneToOneField(Spot)
    flag = models.BooleanField(default=True)

    def __unicode__(self):
        return u'Simple derivative: {}: {}'.format(self.spot.name, self.flag)

from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=300)
    def __unicode__(self):
        return u'%s' % (self.name)

class Beer(models.Model):
    name = models.CharField(max_length=300)
    brewery = models.ForeignKey(Brewery)
    ounces = models.IntegerField(max_length=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __unicode__(self):
       return u'%s - %s' % (self.name, self.brewery)
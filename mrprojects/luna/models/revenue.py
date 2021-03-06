# Revenue Model Class
# Author: Mauricio Ribeiro
# Python: 3.4
# Lang: PT-BR

from django.db import models
from django.core.validators import MinValueValidator

from luna.models.revenue_category import RevenueCategory

class Revenue(models.Model):

	value = models.FloatField(validators = [MinValueValidator(0)])
	category = models.ForeignKey(RevenueCategory)
	creation = models.DateTimeField('date published')

	def __str__(self):
		return "%2.f em %s" %(self.value, self.creation.strftime("%d/%m/%Y %H:%M:%S"))
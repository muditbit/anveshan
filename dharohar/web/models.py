from django.db import models

# Create your models here.
class Places(models.Model):
	place_id = models.AutoField
	place_name = models.CharField(max_length=20)
	place_dist = models.CharField(max_length=50, default ="")
	place_state = models.CharField(max_length=50,default="")
	place_comp_addre = models.CharField(max_length=100,default="")
	category = models.CharField(max_length=50, default="")
	place_desc = models.CharField(max_length=300)
	contrib_date = models.DateField()
	image = models.ImageField(upload_to="web/images", default="")



	def __str__(self):
		return self.place_name
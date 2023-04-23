from django.db import models

# Create your models here.
class defect_weight(models.Model):
    weight = models.CharField(max_length=100)
    def __str__(self):
        return self.weight
    
class Defect_cat(models.Model):
    cat = models.CharField(max_length=100)
    def __str__(self):
        return self.cat


class Defect(models.Model):
    Product_name = models.CharField(max_length=100)
    PNC = models.CharField(max_length=100)
    Line = models.CharField(max_length=100)
    location_lvl01 = models.CharField(max_length=100)
    Location_lvl02 = models.CharField(max_length=100)
    Defect = models.CharField(max_length=100)
    Defect_weight = models.ForeignKey(defect_weight, on_delete=models.CASCADE)
    Defect_cat = models.ForeignKey(Defect_cat, on_delete=models.CASCADE)
    Count_units = models.CharField(max_length=100)
    Containment = models.CharField(max_length=200)
    Corrective = models.CharField(max_length=200)
    Operator = models.CharField(max_length=100)
    Notified = models.CharField(max_length=100)
    # to add the now date time 
    created_at = models.DateTimeField(auto_now_add=True)


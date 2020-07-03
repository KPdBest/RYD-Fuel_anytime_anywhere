from django.db import models

# Create your models here.
class SurveyData(models.Model):
    date = models.DateField(db_column="Date",default=None,blank=True, null=True)
    organisation = models.CharField(db_column='Organisation', max_length=50, blank=True, null=True)
    designation = models.CharField(db_column='Designation', max_length=50, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    remark = models.TextField(db_column='Remark',blank=True, null=True)

    class Meta:
        db_table = 'Survey_Data'
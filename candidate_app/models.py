from django.db import models

class Eventdetails(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_location = models.CharField(max_length=255)
    

    def __str__(self):
        return self.event_name

class Candidatedirectory(models.Model):
    event = models.ForeignKey(
        Eventdetails, models.DO_NOTHING, db_column="event", blank=True, null=True
    )
    


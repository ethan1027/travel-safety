from django.db import models

# Create your models here.
class Gunshot(models.Model):
    incident_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=20)
    city_or_county = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    lat = models.FloatField(null=True,blank=True)
    lng = models.FloatField(null=True,blank=True)
    """ incident_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    state = models.CharField(max_length=20)
    city_or_county = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    n_killed = models.IntegerField(null=True,blank=True)
    n_injured = models.IntegerField(null=True,blank=True)
    incident_url = models.URLField(null=True, blank=True)
    source_url = models.URLField(null=True, blank=True)
    incident_url_fields_missing = models.BooleanField(default=False)
    congressional_district = models.FloatField(null=True,blank=True)
    gun_stolen = models.CharField(max_length=100)
    gun_type = models.CharField(max_length=100)
    incident_characteristics = models.CharField(max_length=200)
    lat = models.FloatField(null=True,blank=True)
    location_description = models.CharField(max_length=50)
    lng = models.FloatField(null=True,blank=True)
    n_guns_involved = models.FloatField(null=True,blank=True)
    notes = models.CharField(max_length=200)
    participant_age = models.CharField(max_length=200)
    participant_age_group = models.CharField(max_length=200)
    participant_gender = models.CharField(max_length=200)
    participant_name = models.CharField(max_length=400)
    participant_relationship = models.CharField(max_length=100)
    participant_status = models.CharField(max_length=200)
    participant_type = models.CharField(max_length=200, null=True,blank=True)
    sources = models.URLField(null=True,blank=True)
    state_house_district = models.FloatField(null=True,blank=True)
    state_senate_district = models.FloatField(null=True,blank=True) """

    def __str__(self):
        return self.address + ", " + self.city_or_county + ", " + self.state


class State(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    rank = models.IntegerField(null=True,blank=True)
    total_incidents = models.IntegerField(null=True,blank=True)
    incidents_per_100k = models.FloatField(null=True,blank=True)
    total_killed_n_injured = models.IntegerField(null=True,blank=True)

    def __str__(self):
        summary = self.name + " is "
        if self.rank < 8:
            summary += "very dangerous."
        elif self.rank < 15:
            summary += "dangerous."
        elif self.rank < 23:
            summary += "somewhat dangerous."
        elif self.rank < 40:
            summary += " not so dangerous."
        else:
            summary += " safe."
        return summary

class City(models.Model):
    name = models.CharField(max_length=70, primary_key=True)
    rank = models.IntegerField(null=True,blank=True)
    total_incidents = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name + ' | rank: ' + str(self.rank) + ' | incidents: ' + str(self.total_incidents)



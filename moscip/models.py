from django.db import models

from datetime import datetime


class Scout(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    ssa_id = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def age(self):
        today = datetime.now()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def patrol(self):
        return self.patrols.all().first().patrol.name

    class Config:
        arbitrary_types_allowed = True


class Patrol(models.Model):
    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PatrolMember(models.Model):
    scout = models.ForeignKey(Scout, on_delete=models.CASCADE, related_name="patrols")
    patrol = models.ForeignKey(Patrol, on_delete=models.CASCADE, related_name="members")
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(null=True, blank=True)
    rank = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.scout.first_name + " " + self.scout.last_name + " - " + self.patrol.name


class Troop(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    duration = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

    # TODO: organisers, event type, etc. All the foreign keys

    def __str__(self):
        return self.name


class EventOrganisers(models.Model):
    name = models.CharField(max_length=200)

    # event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EventCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    badge_type = models.ForeignKey("BadgeType", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class BadgeType(models.Model):
    name = models.CharField(max_length=200)
    points = models.ForeignKey("BadgeTypePoints", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class BadgeTypePoints(models.Model):
    num_points = models.IntegerField(default=0)
    date = models.DateField(null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.name


class ScoutBadge(models.Model):
    scout = models.ForeignKey(PatrolMember, on_delete=models.CASCADE, related_name="badges")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name="scouts")
    date_awarded = models.DateField(null=True, blank=True, default=datetime.now)

    def __str__(self):
        return self.scout.scout.first_name + " " + self.scout.scout.last_name + " - " + self.badge.name

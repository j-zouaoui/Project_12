from django.db import models
from django.conf import settings
from contracts.models import Client
from django.db import models
from django.conf import settings
from account.models import SupportContact


class Status(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  TO_DO = 1
  ON_GOING = 2
  DONE = 3

  STATUS_CHOICES = (
      (TO_DO, 'to do'),
      (ON_GOING, 'on going'),
      (DONE, 'done'),
  )
  id = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()

class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(SupportContact, on_delete=models.CASCADE)
    event_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now=True)
    attendees = models.PositiveIntegerField(blank=False, default=0) # to be clarified
    event_date = models.DateField()
    notes = models.TextField()

import datetime
from email.policy import default
from typing import Text
from django.db import models
import datetime
from django.db.models.enums import Choices
from django.utils import timezone
from django.contrib.auth.models import User
from .UserManager import MyAccountManager


InstrumentChoices = (
    ("Blank", "Blank"), 
	("accordian","accordian"),
	("air horn","air horn"),
	("baby grand piano","baby grand piano"),
	("bagpipe","bagpipe"),
	("banjo","banjo"),
	("bass guitar","bass guitar"),
	("bassoon","bassoon"),
	("bugle","bugle"),
	("calliope","calliope"),
	("cello","cello"),
	("clarinet","clarinet"),
	("clavichord","clavichord"),
	("concertina","concertina"),
	("didgeridoo","didgeridoo"),
	("dobro","dobro"),
	("dulcimer","dulcimer"),
	("fiddle","fiddle"),
	("fife","fife"),
	("flugelhorn","flugelhorn"),
	("flute","flute"),
	("French horn","French horn"),
	("glockenspiel","glockenspiel"),
	("grand piano","grand piano"),
	("guitar","guitar"),
	("harmonica","harmonica"),
	("harp","harp"),
	("harpsichord","harpsichord"),
	("hurdy-gurdy","hurdy-gurdy"),
	("kazoo","kazoo"),
	("kick drum","kick drum"),
	("lute","lute"),
	("lyre","lyre"),
	("mandolin","mandolin"),
	("marimba","marimba"),
	("mellotran","mellotran"),
	("melodica","melodica"),
	("oboe","oboe"),
	("pan flute","pan flute"),
	("piano","piano"),
	("piccolo","piccolo"),
	("pipe organ","pipe organ"),
	("saxaphone","saxaphone"),
	("sitar","sitar"),
	("sousaphone","sousaphone"),
	("tambourine", "tambourine"), 
	("theremin","theremin"),
	("trombone","trombone"),
	("tuba","tuba"),
	("ukulele","ukulele"),
	("viola","viola"),
	("violin","violin"),
	("vuvuzela","vuvuzela"),
	("washtub bass","washtub bass"),
	("xylophone","xylophone"),
	("zither","zither"),
)

StatusChoices = (
    ('Not Started', 'Not Started'), 
    ('Starting', 'Starting'),
    ('On Hold', 'On Hold'),
    ('Almost Done', 'Almost Done'),
    ('Done', 'Done'),
)

class Task(models.Model):
	dateOfTask = models.TextField(default=datetime.date.today)
	Status = models.CharField(max_length=25, choices=StatusChoices, default='Not Started')
	title = models.TextField(default='Enter a Title')
	body = models.TextField()
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)
    

	def __str__(self):
		return self.body[0:50]

	class Meta:
		ordering = ['-dateOfTask']

class Journal(models.Model):
	dateOfJournal = models.DateTimeField(default=datetime.datetime.now)
	title = models.TextField()
	body = models.TextField()
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)
    

	def __str__(self):
		return self.body[0:50]

	class Meta:
		ordering = ['-dateOfJournal']	


class Goal(models.Model):
	dateOfGoal = models.DateTimeField(default=datetime.datetime.now)
	title = models.TextField()
	body = models.TextField()
	techniques = models.TextField
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)
    

	def __str__(self):
		return self.body[0:50]

	class Meta:
		ordering = ['-dateOfGoal']







class Profile(models.Model):
	Email = models.EmailField(('email address'), unique=True, blank=True, null=True)
	firstName =  models.CharField(('first name'), max_length=30, blank=True)
	lastName = models.CharField(('last name'), max_length=30, blank=True)
	bio = models.TextField(max_length=124, blank = True)
	instrument = models.CharField(max_length=40, choices=InstrumentChoices, default='Blank')
	date_joined = models.DateTimeField(('date joined'), default=datetime.datetime.now)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
import datetime
from typing import Text
from django.db import models
import datetime
from django.db.models.enums import Choices
from django.utils import timezone

StatusChoices = (
    ('Not Started', 'Not Started'), 
    ('Starting', 'Starting'),
    ('On Hold', 'On Hold'),
    ('Almost Done', 'Almost Done'),
    ('Done', 'Done'),
)

class Task(models.Model):
    dateOfTask = models.DateField(default=datetime.date.today)
    Status = models.CharField(max_length=25, choices=StatusChoices, default='Not Started')
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-dateOfTask']


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

class Profile(models.Model):
    firstName =  models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    bio = models.TextField(max_length=124)
    instrument = models.CharField(max_length=40, choices=InstrumentChoices, default='Blank')




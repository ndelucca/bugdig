from django.db import models
from django.utils.translation import gettext as _

from users.models import Person

class CaseManager( models.Manager ):

    pass

class Case( models.Model ):

    cases = CaseManager()

    title = models.CharField( unique = True,max_length = 60 )

    description = models.TextField( blank = True )

    date_created= models.DateTimeField( auto_now_add = True )

    date_updated= models.DateTimeField( auto_now = True )

    assignee = models.ManyToManyField( Person, blank = True )

    class Types (models.TextChoices):
        TASK = _('task')
        ISSUE = _('issue')
        BUG = _('bug')
        MAINTENANCE = _('maintenance')

    type_of= models.CharField( db_index = True, default = Types.TASK, choices = Types.choices, max_length = 12 )

    class States (models.TextChoices):
        NEW = _('new')
        ASSIGNED = _('assigned')
        FINISHED = _('finished')

    state = models.CharField( default = States.NEW, choices = States.choices, max_length = 12 )

    class Difficulties ( models.IntegerChoices ):
        EASIEST = 0
        EASY = 1
        MEDIUM = 2
        HARD = 3
        HARDEST = 4

    difficulty= models.SmallIntegerField( default = Difficulties.MEDIUM, choices = Difficulties.choices )

    class Priorities (models.IntegerChoices):
        LOWEST = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        HIGHEST = 4

    priority= models.SmallIntegerField( default = Priorities.MEDIUM, choices = Priorities.choices )

    def __str__( self ):

        return (
            f"id:{self.id} "
            f"type_of:{self.type_of} "
            f"title:{self.title} "
            f"assignee:{self.assignee} "
        )

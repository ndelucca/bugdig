from django.db import models
from django.utils.translation import ugettext as _

from users.models import Profile
from django.urls import reverse_lazy

class Case( models.Model ):
    """
    # Case

    Core Bugdig model

    A Case can be assigned to any number of Profile

    A Profile can be assigned to any number of Case
    """
    objects = models.Manager()

    title = models.CharField(
        unique = True,
        max_length = 60,
        verbose_name=_("title"),

    )
    description = models.TextField(
        blank = True,
        verbose_name=_("description")
    )

    date_created= models.DateTimeField( auto_now_add = True, editable=False )
    date_updated= models.DateTimeField( auto_now = True, editable=False )

    assignee = models.ManyToManyField( Profile,
        blank = True,
        verbose_name=_("assignee")
    )

    class Types (models.TextChoices):
        TASK = _('task')
        ISSUE = _('issue')
        BUG = _('bug')
        MAINTENANCE = _('maintenance')

    type_of= models.CharField(
        db_index = True,
        default = Types.TASK,
        choices = Types.choices,
        max_length = 12,
        verbose_name=_("type")
    )

    class States (models.TextChoices):
        NEW = _('new')
        ASSIGNED = _('assigned')
        FINISHED = _('finished')

    state = models.CharField(
        default = States.NEW,
        choices = States.choices,
        max_length = 12,
        verbose_name=_("state")
    )

    class Difficulties ( models.IntegerChoices ):
        EASIEST = 0
        EASY = 1
        MEDIUM = 2
        HARD = 3
        HARDEST = 4

    difficulty= models.SmallIntegerField(
        default = Difficulties.MEDIUM,
        choices = Difficulties.choices,
        verbose_name=_("difficulty")
    )

    class Priorities (models.IntegerChoices):
        LOWEST = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        HIGHEST = 4

    priority= models.SmallIntegerField(
        default = Priorities.MEDIUM,
        choices = Priorities.choices,
        verbose_name=_("priority")
    )

    def get_absolute_url(self):
        return reverse_lazy('cases:read', args=[self.id])

    def __str__( self ):

        assignees = tuple(self.assignee.all())

        return f"{self.id} - {self.type_of} - {self.title} - {str(assignees)}"

    def __repr__(self):
        assignees = tuple(self.assignee.all())

        return f"{self.id} - {self.type_of} - {self.title} - {str(assignees)}"

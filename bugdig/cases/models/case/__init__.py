from django.db import models

class Case(models.Model):

    title = models.CharField(
        unique = True,
        max_length = 60,
    )

    description = models.TextField(
        blank = True,
    )

    date_created= models.DateTimeField(
        auto_now_add = True
    )

    date_updated= models.DateTimeField(
        auto_now = True
    )

    assignee = models.CharField(
        blank = True,
        max_length = 30
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
        max_length = 12
    )
    class States (models.TextChoices):
        NEW = _('new')
        ASSIGNED = _('assigned')
        FINISHED = _('finished')

    state = models.CharField(
        default = States.NEW,
        choices = States.choices
    )

    class Difficulties ( models.IntegerChoices ):
        EASIEST = 0
        EASY = 1
        MEDIUM = 2
        HARD = 3
        HARDEST = 4

    difficulty= models.SmallIntegerField(
        default = Difficulties.MEDIUM,
        choices = Difficulties.choices
    )

    class Priorities (models.IntegerChoices):
        LOWEST = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        HIGHEST = 4

    priority= models.SmallIntegerField(
        default = Priorities.MEDIUM,
        choices = Priorities.choices
    )

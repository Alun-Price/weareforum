from django.contrib import admin
from .models import Subject, Thread, Posts, Poll, PollSubject, Vote

# Register your models here.

admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Posts)
admin.site.register(Poll)
admin.site.register(PollSubject)
admin.site.register(Vote)

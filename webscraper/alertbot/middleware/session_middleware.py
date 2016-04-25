from django.contrib.auth import logout
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from alertbot.models import User
from django.conf import settings

class SessionFilter:
    def process_request(self, request):
        if(request.path[0:8] != '/profile'):
            return
        try:
            if(request.session.get('_login',0) != 1):
                request.session.flush()
                return HttpResponseRedirect('/login')
            id = request.session['_id']
            user = User.objects.get(id = id)
            return
        except:
            return HttpResponseRedirect('/login')

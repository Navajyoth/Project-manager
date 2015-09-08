import httplib2
import re

# Create your views here.
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.http import HttpResponseRedirect

from apps.account.models import User
from apps.utils.auth import login_model_user


flow = OAuth2WebServerFlow(
    client_id=settings.GMAIL_CLIENT_ID,
    client_secret=settings.GMAIL_CLIENT_SECRET,
    scope=settings.GMAIL_SCOPE,
    redirect_uri=settings.GMAIL_REDIRECT_URI)


def _get_user_details(code):
    credentials = flow.step2_exchange(code)
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('plus', 'v1', http=http)
    response = service.people().get(userId='me').execute()
    domain = re.findall(r'@rawdatatech.com', response['emails'][0]['value'])
    if domain:
        user = User()
        user.first_name = response['displayName'] if response[
            'displayName'] else response['emails'][0]['value'].split('@')[0] + " " + " 1"
        user.email = response['emails'][0]['value']
        return user
    raise PermissionDenied


def login(request):
    auth_uri = flow.step1_get_authorize_url()
    return HttpResponseRedirect(auth_uri)  # + "&approval_prompt=force")


def callback(request):
    code = request.GET.get('code')
    if code:
        user = _get_user_details(code)
    else:
        raise Http404(
            "the get url didn't return the code istead it retured a error")
    try:
        user = User.objects.get(email=user.email)
        user.save()
    except ObjectDoesNotExist:
        user = User.objects.create_user(email=user.email,
                                        first_name=user.name.split(' ')[0],
                                        last_name=user.name.split(' ')[1],
                                        password="")
    login_model_user(request, user)
    return HttpResponseRedirect('/')

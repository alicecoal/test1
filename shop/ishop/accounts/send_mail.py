import logging

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.form_to_model import get_user_from_form
from accounts.tokens import account_activation_token

logger = logging.getLogger(__name__)


def send_mail_to(request, user):
    current_site = get_current_site(request)
    subject = 'Please Activate Your Account'
    message = render_to_string('activation_request.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    logger.info("Successful sent message to {} with {}".format(user, subject))
    user.email_user(subject, message)


def send_mail_to_user_from_form(request, form):
    user = get_user_from_form(form)
    send_mail_to(request, user)

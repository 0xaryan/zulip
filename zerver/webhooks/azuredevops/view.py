from typing import Any, Dict, Iterable, Optional

from django.http import HttpRequest, HttpResponse
from django.utils.translation import ugettext as _

from zerver.decorator import api_key_only_webhook_view
from zerver.lib.webhooks.common import check_send_webhook_message
from zerver.lib.request import REQ, has_request_variables
from zerver.lib.response import json_error, json_success
from zerver.lib.validator import check_dict, check_string
from zerver.models import UserProfile

@api_key_only_webhook_view('AzureDevops')
@has_request_variables
def api_azuredevops_webhook(
        request: HttpRequest, user_profile: UserProfile,
        payload: Dict[str, Iterable[Dict[str, Any]]]=REQ(argument_type='body'),
        topic: str=REQ(default='coverage')
) -> HttpResponse:

    # construct the body of the message
    body = 'A new build from Azure DevOps! :smile:'

    # try to add the Wikipedia article of the day
    body_template = '\n' + payload['detailedMessage']["markdown"]
    body += body_template


    # send the message
    check_send_webhook_message(request, user_profile, topic, body)

    return json_success()

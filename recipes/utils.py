from django.contrib.auth.models import AnonymousUser

def profile_from_request(request):
    """
    Get the profile of the user in the request, or None if not logged in
    :param request: Http request
    :return: request.user's Profile or None
    """
    if isinstance(request.user, AnonymousUser):
        return None
    else:
        return request.user.get_profile()
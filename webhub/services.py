from django.core.exceptions import ObjectDoesNotExist
from webhub.models import Post, RevPost


def get_post_by_id(post_id):

    post = None
    try:
        post = Post.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        pass

    return post


def get_revpost_of_owner(post_id):

    revpost = None
    try:
        revpost = RevPost.objects.filter(owner_rev_post_id=post_id)
    except ObjectDoesNotExist:
        pass

    return revpost

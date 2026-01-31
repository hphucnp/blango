from django import template

register = template.Library()


@register.filter
def author_details(author, current_user=None):
    """
    Display author details. If the author is the current user, show "me".
    Otherwise, show the author's name or email.
    """
    if current_user and author == current_user:
        return "me"

    if author.first_name and author.last_name:
        return f"{author.first_name} {author.last_name}"
    elif author.first_name:
        return author.first_name
    elif author.email:
        return author.email
    else:
        return author.username

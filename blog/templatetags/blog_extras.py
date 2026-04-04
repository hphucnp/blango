from django import template
from django.contrib.auth.management.commands.changepassword import UserModel
from django.utils.html import escape, format_html, mark_safe

register = template.Library()


@register.filter
def full_name(user):
    first_name = user.first_name
    last_name = user.last_name

    if not last_name:
        return escape(first_name)

    return format_html("<em>{}</em>, {}", first_name, last_name)


@register.filter
def author_details(author, current_user):
    """
    Display author details. If the author is the current user, show "me".
    Otherwise, show the author's name or email.
    """
    if not isinstance(author, UserModel):
        return ""
    if author == current_user:
        return mark_safe("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = mark_safe('<a href="mailto:{}">'.format(author.email))
        suffix = mark_safe("</a>")
    else:
        prefix = ""
        suffix = ""

    return mark_safe("{}{}{}".format(prefix, name, suffix))


@register.simple_tag
def row(extra_classes=""):
    return mark_safe('<div class="row {}">'.format(extra_classes))

@register.simple_tag
def endrow():
    return mark_safe('</div>')

@register.simple_tag
def col(extra_classes=""):
    return mark_safe('<div class="col {}">'.format(extra_classes))


@register.simple_tag
def endcol():
    return mark_safe("</div>")

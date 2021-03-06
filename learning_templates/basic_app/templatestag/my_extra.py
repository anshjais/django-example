from djanog import template

register=template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)

@register.filter(name='cap')
def cap(value):
    return value.count()

from functools import wraps


def extendfunc(func):
    @wraps(func)
    def wrapped_view(self, request, *args, **kwargs):
        
        ### Add your code here ###

        return func(self, request, *args, **kwargs)
    return wrapped_view

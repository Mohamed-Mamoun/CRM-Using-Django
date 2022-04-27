from django.shortcuts import redirect


def authenticated_user(view_func):
    def inner_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return inner_func

#--------------------- Permission decrators --------------------

def permission(allowed_roles=[]):
    def decrators(view_func):
        def wrapper_func(request, *args, **Kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                                  
            if group in allowed_roles:
                return view_func(request, *args, **Kwargs)
            else:
                return redirect('User')
        return wrapper_func
    return decrators

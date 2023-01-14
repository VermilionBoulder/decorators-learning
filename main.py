import datetime


T = f"[{datetime.datetime.now().strftime('%d.%m.%y %H:%M'):14}]"


def printt(*args, **kwargs):
    print(T, *args, **kwargs)


def make_bold(f):
    def wrapped(*args):
        return f"<b>{f(*args)}</b>"
    return wrapped


def surround_with_text(text):
    def decorated(f):
        def wrapped(*args, **kwargs):
            return f"{text} {f(*args, **kwargs)} {text}"
        return wrapped
    return decorated


def log(fun):
    def wrapped(*args, **kwargs):
        printt(f"{fun.__name__} called")
        output = fun(*args, **kwargs)
        printt(f"Return value: {output}")
        return output
    return wrapped


@log
def say(*text):
    return ", ".join(text)


say("oompa")
say("loompa")
say("sample", "text")

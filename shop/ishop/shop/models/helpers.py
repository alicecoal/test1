from django.contrib.auth.models import User


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


def decorator(fun):
    def wrapper(*args, **kwargs):
        value = fun(*args, **kwargs)
        if value > 1:
            print('Too many orders')
            subject = 'Too many orders'
            message = 'Hi Ann, on ikea2.0 is too many orders, we need your help!'
            User.objects.filter(is_superuser=True)[0].email_user(subject, message)

    return wrapper


class Observer:
    subscribers = []

    def __init__(self):
        self.subscribers.append(self)
        self.subscribers = {}

    def observe(self, event_name, callback):
        self.subscribers[event_name] = callback


class Event:
    def __init__(self, name, data, autofire=True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()

    def fire(self):
        for observer in Observer.subscribers:
            if self.name in observer.subscribers:
                observer.subscribers[self.name](self.data)

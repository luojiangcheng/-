from django.shortcuts import render


def index(requests):
    return render(requests, "index.html")


def todo1(requests):
    return render(requests, "todo1.html")


def todo2(requests):
    return render(requests, "todo2.html")


def todo3(requests):
    return render(requests, "todo3.html")


def todo5(requests):
    return render(requests, "todo5.html")


def todo6(requests):
    return render(requests, "todo6.html")


def todo4(requests):
    return render(requests, "技术排名top20.html")

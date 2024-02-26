from django.shortcuts import render

def main(requests):
    return render(requests, 'index.html')

def about_me(requests):
    return render(requests, 'about_me.html')
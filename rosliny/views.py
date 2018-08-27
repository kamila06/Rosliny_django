from __future__ import unicode_literals

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from hitcount.models import HitCount
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, TemplateView
from hitcount.views import HitCountDetailView

from models import Index,Catalog, Contact

# class PostMixinDetailView(object):
#     """
#     Mixin to same us some typing.  Adds context for us!
#     """
#     model = Index
#
#     def get_context_data(self, **kwargs):
#         context = super(PostMixinDetailView, self).get_context_data(**kwargs)
#         context['post_list'] = Post.objects.all()[:5]
#         context['post_views'] = ["ajax", "detail", "detail-with-count"]
#         return context
#
#
# class IndexView(PostMixinDetailView, TemplateView):
#     template_name = 'roslinysite/index.html'
#
#
# # class PostDetailJSONView(PostMixinDetailView, DetailView):
# #     template_name = 'blog/post_ajax.html'
# #
# #     @classmethod
# #     def as_view(cls, **initkwargs):
# #         view = super(PostDetailJSONView, cls).as_view(**initkwargs)
# #         return ensure_csrf_cookie(view)
#
#
# class PostDetailView(PostMixinDetailView, HitCountDetailView):
#     """
#     Generic hitcount class based view.
#     """
#     pass
#
#
# class PostCountHitDetailView(PostMixinDetailView, HitCountDetailView):
#     """
#     Generic hitcount class based view that will also perform the hitcount logic.
#     """
#     count_hit = True


def index(request):
    return render(request, 'roslinysite/index.html', {})

def catalog(request):
    return render(request, 'roslinysite/katalog.html', {})


# def contact(request):
#     return render(request, 'roslinysite/kontakt.html', {})
#

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Subject: ']
            from_email = form.cleaned_data['From email: ']
            message = form.cleaned_data['Message: ']
            try:
                send_mail(subject, message, from_email, ['kamilarud1995@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "roslinysite/kontakt.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

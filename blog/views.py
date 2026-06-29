from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import BlogPost


class ContentManagerMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("blog.can_manage_blog"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_published:
            raise Http404("Статья не опубликована")
        obj.views_count += 1
        obj.save()
        if obj.views_count == 100 and not obj.congratulation_sent:
            send_mail(
                subject="🎉 Поздравляем! 100 просмотров",
                message=f'🎉 Поздравление! Статья "{obj.title}" набрала 100 просмотров! Ты крут!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["tvoja_pochta@example.com"],  # твоя почта
                fail_silently=False,
            )
            obj.congratulation_sent = True
            obj.save(update_fields=["congratulation_sent"])
        return obj


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:list")


class BlogPostUpdateView(LoginRequiredMixin, ContentManagerMixin, UpdateView):
    model = BlogPost
    fields = ["title", "content", "preview", "is_published"]
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})


class BlogPostDeleteView(LoginRequiredMixin, ContentManagerMixin, DeleteView):
    model = BlogPost
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:list")

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import F
from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from main.forms import TaomForm
from main.models import Kategoriya, Taom
from django.core.paginator import Paginator


def main_index(request):
    return render(request,'main/index.html',{
        'kategoriyalar' : Kategoriya.objects.all().order_by('name')
    })

def main_kategoriya(request, rid):
    taomlar = Taom.objects.filter(kategoriya_id=rid).order_by('name')
    paginator = Paginator(taomlar, 10)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'main/taom.html',{
        'taomlar' : taomlar,
        'page_obj': page_obj,
        'how_many_pages' : list(range(1,page_obj.paginator.num_pages+1))
    })


def main_taom(request, pid):
    taom = Taom.objects.filter(id=pid)
    if request.method == 'GET':
        taom.update(viewed=F('viewed')+1)
    return render(request, 'main/read.html', {
        'taom': Taom.objects.get(id=pid),
        'name' : 'name'
    })

class TaomView(CreateView ,LoginRequiredMixin):
    template_name = "account/registration.html"
    model = Taom
    form_class = TaomForm

    def form_valid(self, form):
        k = form.save(commit=False)
        k.creator = self.request.user
        messages.success(self.request,_("Taomingiz muvaffaqiyalo qo'shildi"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main_index')


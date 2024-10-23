from django.db.models import Max, Count
from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        self.answer2 = Author.objects.annotate(number_of_entries=Count('entries')).order_by('-number_of_entries')[0]
        self.answer3 = Entry.objects.filter(tags__name__in=['Кино', 'Музыка']).distinct()
        self.answer4 = Author.objects.filter(gender='ж').count()
        self.answer5 = round(Author.objects.filter(status_rule=True).count() * 100 / Author.objects.count(), 2)
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1, 5))
        self.answer7 = Author.objects.filter().order_by('-age')[0]
        self.answer8 = Author.objects.filter().count() - Author.objects.filter(phone_number=None).count()
        self.answer9 = Author.objects.filter(age__lt=25)
        self.answer10 = Author.objects.annotate(count=Count('entries')).values('username',
                                                                                           'count')
        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}  # Создайте здесь запросы к БД
        return render(request, 'train_db/training_db.html', context=context)


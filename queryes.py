import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    # """<QuerySet [<Entry: Знакомство с Парижем>,
    # <Entry: Инновации в области виртуальной реальности>]>"""

    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))

    print(Entry.objects.filter(headline__contains='мод'))
    # <QuerySet [
    # <Entry: Тенденции моды на текущий сезон>,
    # <Entry: История моды: от ретро до современности>,
    # <Entry: Интервью с известными модельерами и дизайнерами>
    # ]>














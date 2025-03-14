import os
import csv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pageflip_project.settings')
import django

django.setup()


from pageflip.models import BookPage,SubGenreCategory



def populate():
    with open('database.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            title = row["Book Name"]
            author = row["Author"]
            year = row["Year of Publication"]
            series_info = row["Standalone/Series"]
            description = row["Brief Description"]
            subgenre_text = row["Subgenre"]


            book, created = BookPage.objects.get_or_create(
                title=title,
                defaults={
                    "author": author,
                    "year_of_publication": year,
                    "series_info": series_info,
                    "description": description
                }
            )
            if created:
                print(f"Created book: {title}")
            else:
                print(f"Found existing book: {title}")


            if hasattr(book, "subgenres"):
                subgenre_list = [s.strip() for s in subgenre_text.split(',')]
                for sname in subgenre_list:
                    sub_obj, _ = SubGenreCategory.objects.get_or_create(name=sname)
                    book.subgenres.add(sub_obj)


def run():
    print("Starting population script...")
    populate()
    print("Population script complete.")


if __name__ == '__main__':
    run()

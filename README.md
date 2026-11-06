# Django Store

Sklep internetowy w Django z PostgreSQL: katalog produktów, koszyk zalogowanego klienta i strona zamówienia. Projekt szkolny (TPM), rozwijany krok po kroku: modele, widoki, szablony, a potem koszyk obsługiwany przez `fetch`.

## Funkcje
- Katalog produktów ze zdjęciami (pole `ImageField`, upload przez panel administracyjny)
- Koszyk przypisany do klienta: dodawanie i usuwanie pozycji przez endpoint JSON `POST /update_item/` z tokenem CSRF
- Podsumowanie zamówienia: liczba sztuk i wartość koszyka liczone we właściwościach modelu `Order`
- Panel administracyjny Django do zarządzania produktami, zamówieniami i adresami wysyłki

## Model danych
`Customer` (1:1 z `User`) → `Order` → `OrderItem` → `Product`, a do zamówienia `ShippingAddress`.

## Stack
Python, Django 4.2, PostgreSQL (psycopg2), Bootstrap 5, JavaScript (Fetch API)

## Uruchomienie
```bash
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env          # uzupełnij dane bazy, ustaw zmienne środowiskowe
cd ecommerce
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Konfiguracja jest czytana ze zmiennych środowiskowych (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `POSTGRES_*`), wzór w `.env.example`.

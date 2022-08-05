1. Open Project and Create Virtual Environment
2. pip install -r requirements.txt
3. Create User
    python manage.py createsuperuser --username krishna --email krishna@gmail.com
4. Generate tokens
    python manage.py drf_create_token krishna
    Generated token 749ddd5b6b256a39a1370ac68c360cf5c69b73e5 for user krishna
5. Run test.py file of api_test
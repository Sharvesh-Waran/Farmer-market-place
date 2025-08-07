# Farmer-market-place

```Python Version: 3.12.3```

While installing locally, make sure to install django and its related dependencies in a Virtual Environment, as it is standard practice for Django Projects

This project connects to a remote postgres database. To use a local sqlite3 database, uncomment the following lines in ```market/settings.py```

```py
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

'''
```

Comment out the postgres database configuration

```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "marketplace",
        "USER": "neondb_owner",
        "PASSWORD": "npg_isk8zrFjX5mJ",
        "HOST": "ep-patient-salad-a1sgoxav-pooler.ap-southeast-1.aws.neon.tech",
        "PORT": "5432",
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}
```



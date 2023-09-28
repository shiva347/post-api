# post-api

## Project Setup 
Clone the repository
```
git clone https://github.com/shiva347/post-api.git
```

Create and activate a virtual environment
```
python -m venv myenv
```
For Windows 
```
myenv\Scripts\activate
```
For Linux or Mac
```
source myenv/bin/activate
```
Navigate backend project directory
```
cd BackendAssignment
```
Install the required packages
```
pip install -r requirements.txt
```


**Now, set up the PostgreSQL database on your system if it's not already configured, and replace 'NAME', 'USER', and 'PASSWORD' with your own valuess.
If you haven't set it up yet, you can add the following database configuration.**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```
Runserver 
```
python mange.py run server
```

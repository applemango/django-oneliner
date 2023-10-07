[
    [
        i:=__import__,
        os:=i("os"),
        sys:=i("sys"),
        pymysql:=i("pymysql"),
        django:=i("django"),
        get_wsgi_application:=i("django.core.wsgi")
    ],
    urlpatterns := [
        django.urls.path("", lambda request: django.http.JsonResponse({"msg": "Hello, world!"}))
    ],
    pymysql.install_as_MySQLdb(),
    django.conf.settings.configure(
        DEBUG=(
            os.environ.get("DEBUG","")=="1"
        ),
        ALLOWED_HOSTS=["*"],
        ROOT_URLCONF=__name__,
        SECRET_KEY=django.utils.crypto.get_random_string(50),
        MIDDLEWARE=["django.middleware.common.CommonMiddleware"]
    ),
    app:=django.core.wsgi.get_wsgi_application(),
    django.core.management.execute_from_command_line(sys.argv)
]
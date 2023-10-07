[
    us := lambda u, j: [u("", lambda r: j({"msg": "Hello, world!"}))],
    i:=__import__,
    o:=i("os"),
    s:=i("sys"),
    p:=i("pymysql"),
    d:=i("django"),
    i("django.core.wsgi"),
    u:= d.urls.path,
    j:=d.http.JsonResponse,
    urlpatterns := us(u, j),
    p.install_as_MySQLdb(),
    d.conf.settings.configure(
        DEBUG=True,ALLOWED_HOSTS=["*"],
        ROOT_URLCONF=__name__,
        SECRET_KEY=d.utils.crypto.get_random_string(50),
        MIDDLEWARE=[
            "django.middleware.common.CommonMiddleware"
        ]
    ),
    app:=d.core.wsgi.get_wsgi_application(),
    d.core.management.execute_from_command_line(s.argv)
]
bottle-app-engine
=================

This app demonstrates how to restrict access to specific authenticated users on [Google App Engine][app-engine]. The app uses Python 2.7 and [Bottle][bottle], and the [Users API][users-api].


Setup
-----

- Put your static website in the "static" folder. The default page is "index.html".
- Add the email addresses to ALLOWED_USERS in wsgi.py.
- Install bottle with `pip install --target . --requirement requirements.txt`
- Deploy!


[bottle]: http://bottlepy.org/
[app-engine]: https://cloud.google.com/appengine/
[users-api]: https://cloud.google.com/appengine/docs/python/users/

# User Management Webservice


**This api is used to create, edit and delete user information.**

# Requirements



# URL 

http://usermanagement.somee.com/WEBSERVICE/RestServiceImpl.svc/

		
			# http://usermanagement.somee.com/WEBSERVICE/RestServiceImpl.svc/AllUsers
		


# Arguments


The user management webservice accepts five (5) parameters, with two one them being optional

<dl>
<dt>firstname  (string) </dt>
  <dd>The user first name</dd>

<dt>lastname  (string)</dt>
  <dd>The users last name  </dd>

<dt>email  (string) </dt>
  <dd>The users email address, this is also the primary key // eg. youremail@gmail.com</dd>

<dt>passCode (string)</dt>
  <dd>The user password</dd>

<dt>userType (string)</dt>
  <dd>This indicates the type of user, the userType accepts of of two choices "admin" or "generalUser"</dd>


**Below**: *Below is an example of a JSON object*

# Example

Let's take a look at an example of the arguments that would be passed


```python
	{
		"email": "chris@uwi.com",
		"firstName": "Christopher",
		"lastName": "Walton",
		"passCode": "password",
		"userType": "admin"
	}

```
# Endpoints

```
    POST
```

<p>/CreateUser/</p>

```
    GET
```
<p>/user/       -- API endpoint returns all users</p>
<p>/users/{pk}/    -- API endpoint only return user information whose username {pk} has been specified </p>
<p>/users/{pk}/get_email -- API endpoint returns email of a user

```
    PUT
```
<p>/users/{pk}/   -- API endpoint which allows the user information to be edited </p>

```
    DELETE
```
<p>/users/{pk}/   -- API endpoint deletes the user whose username has been specfied</p>

# Additional Information






[build-status-image]: https://secure.travis-ci.org/tomchristie/django-rest-framework.png?branch=master
[travis]: http://travis-ci.org/tomchristie/django-rest-framework?branch=master
[twitter]: https://twitter.com/_tomchristie
[group]: https://groups.google.com/forum/?fromgroups#!forum/django-rest-framework
[0.4]: https://github.com/tomchristie/django-rest-framework/tree/0.4.X
[sandbox]: http://restframework.herokuapp.com/

[index]: http://www.django-rest-framework.org/
[oauth1-section]: http://www.django-rest-framework.org/api-guide/authentication.html#oauthauthentication
[oauth2-section]: http://www.django-rest-framework.org/api-guide/authentication.html#oauth2authentication
[serializer-section]: http://www.django-rest-framework.org/api-guide/serializers.html#serializers
[modelserializer-section]: http://www.django-rest-framework.org/api-guide/serializers.html#modelserializer
[functionview-section]: http://www.django-rest-framework.org/api-guide/views.html#function-based-views
[generic-views]: http://www.django-rest-framework.org/api-guide/generic-views.html
[viewsets]: http://www.django-rest-framework.org/api-guide/viewsets.html
[routers]: http://www.django-rest-framework.org/api-guide/routers.html
[serializers]: http://www.django-rest-framework.org/api-guide/serializers.html
[authentication]: http://www.django-rest-framework.org/api-guide/authentication.html

[rest-framework-2-announcement]: http://www.django-rest-framework.org/topics/rest-framework-2-announcement.html
[2.1.0-notes]: https://groups.google.com/d/topic/django-rest-framework/Vv2M0CMY9bg/discussion
[image]: http://www.django-rest-framework.org/img/quickstart.png

[tox]: http://testrun.org/tox/latest/

[tehjones]: https://twitter.com/tehjones/status/294986071979196416
[wlonk]: https://twitter.com/wlonk/status/261689665952833536
[laserllama]: https://twitter.com/laserllama/status/328688333750407168

[docs]: http://www.django-rest-framework.org/
[urlobject]: https://github.com/zacharyvoase/urlobject
[markdown]: http://pypi.python.org/pypi/Markdown/
[pyyaml]: http://pypi.python.org/pypi/PyYAML
[defusedxml]: https://pypi.python.org/pypi/defusedxml
[django-filter]: http://pypi.python.org/pypi/django-filter
[security-mail]: mailto:rest-framework-security@googlegroups.com
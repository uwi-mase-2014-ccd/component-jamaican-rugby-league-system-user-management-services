# User Management Webservice


**This api is used to create, edit and delete user information.**

# URL 

http://usermanagement.somee.com/UserManagementComponent/RestServiceImpl.svc



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
<ul>
<li><strong>/CreateUser</strong></li>
</ul>
```
    GET
```
<ul>
<li><strong>/AllUser</strong>      -- API endpoint returns all users</li>
<li><strong>/AuthenticateUser/{email}/{passCode}</strong></li>
</ul>
		{ 
		"email": "email",
		"passCode": "password"
		}
<ul>		
<li><strong>/User/{email}</strong>	-- API endpoint returns the user whose email has been passed </li>
<li><strong>/AllUserTypes</strong>	-- API endpoint returns all user types </li>
</ul>
```
    PUT
```
<ul>
<li><strong>/EditUser/{email}</strong>   -- API endpoint which allows the user information to be edited but you are not allowed to change the user's</ul>
</ul>
<p>
	The Edit User request requires all parameters as shown in the ```JSON``` string below, i.e the email has to remain the same 
</p>
	{
		"email": "chris@uwi.com",
		"firstName": "Christopher",
		"lastName": "Walton",
		"passCode": "password",
		"userType": "admin"
	}



```
    DELETE
```
<p><strong>/DeleteUser/{email}</strong>  -- API endpoint deletes the user whose email address has been specfied  ```return True``` if deleted else ```return False```</p>

<p>
	 EXAMPLE: For a GET you would use the 	
</p>
```
	http://usermanagement.somee.com/WEBSERVICE/RestServiceImpl.svc/AllUsers

```

# Additional Information

A user must be created before you are able to login, or run
```GET /AllUser ```and use one of the users' username and password.
Note that as stated above the email is the primary key, therefore two users cant exist with the same primary key



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
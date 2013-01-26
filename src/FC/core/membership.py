from FC.models.User import User

def getUser(request):
	userId = int(request.session.get("user_id", "0"))
	if userId == 0:
		return None
	user = User.objects.get(id = userId)
	return user

def login(request, user):
	request.session["user_id"] = user.id

def logout(request):
	request.session.pop("user_id")

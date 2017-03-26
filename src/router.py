from webapp2 import WSGIApplication, Route

app = WSGIApplication([
    # Home
    Route(r"/",
          handler="app.home.HomePage", name="home"),
    Route(r"/register",
          handler="app.registration.RegistrationPage", name="signup"),
    Route(r"/login",
          handler="app.login.LoginPage", name="login"),
    Route(r"/logout",
          handler="app.logout.LogoutPage", name="logout"),

    # /posts
    Route(r"/posts",
          handler="app.posts.list.ListPosts", name="userposts"),
    Route(r"/posts/view/<post_key:[a-zA-Z0-9-_]+>",
          handler="app.posts.view.ViewPost", name="viewpost"),
    Route(r"/posts/add",
          handler="app.posts.add.AddPost", name="addpost"),
    Route(r"/posts/edit/<post_key:[a-zA-Z0-9-_]+>",
          handler="app.posts.edit.EditPost", name="editpost"),
    Route(r"/posts/delete/<post_key:[a-zA-Z0-9-_]+>",
          handler="app.posts.delete.DeletePost", name="deletepost"),
    Route(r"/posts/like/<post_key:[a-zA-Z0-9-_]+>",
          handler="app.posts.like.LikePost", name="likepost"),

    # /comments
    Route(r"/posts/<post_key:[a-zA-Z0-9-_]+>/comments/"
          + r"edit/<comment_key:[a-zA-Z0-9-_]+>",
          handler="app.posts.comments.edit.EditComment", name="editcomment"),
    Route(r"/posts/<post_key:[a-zA-Z0-9-_]+>/comments/"
          + r"delete/<comment_key:[a-zA-Z0-9-_]+>", name="deletecomment",
          handler="app.posts.comments.delete.DeleteComment"),

    # /user
    Route(r"/posts/user/<user_key:[a-zA-Z0-9-_]+>", name="user",
          handler="app.posts.user.UserPosts")
], debug=True)

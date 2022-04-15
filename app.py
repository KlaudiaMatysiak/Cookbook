import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# @login_required decorator
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
def login_required(f):
    """Login required decorator used for page where user has to be logged in to access the page"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You are not authorized to access this page.")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/home")
def home():
    """Render template for Home Page"""
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    """show all the recipes"""
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Searching for specific recipe"""
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """register user"""
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        register_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_user)

        session["user"] = request.form.get("username").lower()
        flash("Registration Succesfull!")
        return redirect(url_for("get_recipes"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """login into the user account"""
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("get_recipes"))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out user from website"""
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """Adding recipe to db"""
    if request.method == "POST":
        recipe = {
            "title": request.form.get("title"),
            "ingredients": request.form.get("ingredients").splitlines(),
            "method": request.form.get("method").splitlines(),
            "image": request.form.get("image"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added!")
        return redirect(url_for("get_recipes"))
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """Edit the recipe"""
    if request.method == "POST":
        recipe = {
            "title": request.form.get("title"),
            "ingredients": request.form.get("ingredients").splitlines(),
            "method": request.form.get("method").splitlines(),
            "image": request.form.get("image"),
            "added_by": session["user"]
        }
        mongo.db.recipes.replace_one(
            {"_id": ObjectId(recipe_id)}, recipe)
        flash("Recipe successfully updated!")
        return redirect(url_for("get_recipes"))

    find_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=find_recipe)


@app.route("/delete_recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    """Delete a recipe"""
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("get_recipes"))


@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def show_recipe(recipe_id):
    """Check full recipe page"""
    title = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("show_recipe.html", recipe=title)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

from flask import Blueprint, render_template, request

authors_blueprint = Blueprint(
    "authors_blueprint", __name__, template_folder="templates"
)


@authors_blueprint.route("/", methods=["GET"])
@authors_blueprint.route("/<story_id>", methods=["GET"])
def index(story_id=None):
    story_text = f"story { story_id }" if story_id else "nothing"
    return render_template("authors/authors.html", story_text=story_text)


@authors_blueprint.route("/get_email/", methods=["GET", "POST"])
def get_email():
    if "email" in request.form:
        email = request.form["email"]
        return render_template("authors/authors.html", story_text=email)
    else:
        return render_template("authors/form.html")

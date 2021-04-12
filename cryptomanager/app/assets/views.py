from flask import Blueprint, render_template, flash, redirect, url_for

assets = Blueprint('assets', __name__, template_folder="templates")


@assets.route('/assets', methods=["GET", "POST"])
def get_asset():
    return render_template('assets.html',)

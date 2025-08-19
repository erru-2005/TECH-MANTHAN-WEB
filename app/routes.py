from flask import Blueprint, render_template, request, jsonify
from . import mongo
from bson import ObjectId

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/all_event')
def All_Event():
    return render_template('all_event.html')

@main.route('/admin/home')
def admin_home():
    return render_template('home.html')

@main.route('/user/event')
def event():
    return render_template('event1.html')

@main.route('/event/codex')
def codex_event():
    # Renders the 3D, mobile-friendly TECH-MANTHAN 3.0 CODEX template
    return render_template('TECH recreate.html')

# Lightweight registration landing so the CTA works


@main.route('/showcase/new')
def showcase_new():
    # Background is the second image; foreground is the poster with 3D tilt + CTA
    return render_template('new.html')


@main.route('/event1')
def showcase_new1():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event1.html')

@main.route('/event2')
def showcase_new2():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event2.html')

@main.route('/event3')
def showcase_new3():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event3.html')

@main.route('/event4')
def showcase_new4():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event4.html')

@main.route('/event5')
def showcase_new5():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event5.html')

@main.route('/event6')
def showcase_new6():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event6.html')

@main.route('/event7')
def showcase_new7():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event7.html')

@main.route('/event8')
def showcase_new8():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event8.html')

@main.route('/event9')
def showcase_new9():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event9.html')

@main.route('/event10')
def showcase_new10():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event10.html')

@main.route('/event11')
def showcase_new11():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event11.html')

@main.route('/event12')
def showcase_new12():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event12.html')

@main.route('/event13')
def showcase_new13():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event13.html')

@main.route('/event14')
def showcase_new14():
    # Single-card version that replaces the first image with the second image and adds 3D + CTA
    return render_template('event14.html')

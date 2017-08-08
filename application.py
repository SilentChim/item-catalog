from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Application, Feature

# Imports to create anti forgery state tokens
from flask import session as login_session
import random
import string

app = Flask(__name__)

engine = create_engine('sqlite:///application.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a state token to prevent request forgery
# Store in session for validation later
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html')

# JSON APIs to view Application Info
@app.route('/application/<int:application_id>/feature/JSON')
def applicationFeatureJSON(application_id):
    application = session.query(Application).filter_by(id=application_id).one()
    features = session.query(Feature).filter_by(
        application_id=application_id).all()
    return jsonify(Features=[f.serialize for f in features])


@app.route('/application/<int:application_id>/feature/<int:feature_id>/JSON')
def featureJSON(application_id, feature_id):
    App_Feature = session.query(Feature).filter_by(id=feature_id).one()
    return jsonify(App_Feature=App_Feature.serialize)


@app.route('/restaurant/JSON')
def applicationsJSON():
    applications = session.query(Application).all()
    return jsonify(applications=[a.serialize for a in applications])

# Main Handlers
# Shows all applications
@app.route('/')
@app.route('/application')
def showApplications():
    applications = session.query(Application).all()
    return render_template('applications.html', applications =
        applications)

# Creates new application
@app.route('/application/new', methods=['GET','POST'])
def newApplication():
    if request.method == 'POST':
        newApplication = Application(name=request.form['name'])
        session.add(newApplication)
        session.commit()
        return redirect(url_for('showApplications'))
    else:
        return render_template('newApplication.html')

# Edit exhisting application
@app.route('/application/<int:application_id>/edit', methods=['GET','POST'])
def editApplication(application_id):
    editedApplication = session.query(
        Application).filter_by(id=application_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedApplication.name = request.form['name']
            return redirect(url_for('showApplications'))
    else:
        return render_template(
            'editApplication.html', application=editedApplication)

# Deletes exhisting application
@app.route('/application/<int:application_id>/delete', methods=['GET','POST'])
def deleteApplication(application_id):
  applicationToDelete = session.query(Application).filter_by(id = application_id).one()
  if request.method == 'POST':
    session.delete(applicationToDelete)
    flash('%s Successfully Deleted' % applicationToDelete.name)
    session.commit()
    return redirect(url_for('showApplications', application_id = application_id))
  else:
    return render_template('deleteApplication.html',application = applicationToDelete)

# Shows all features
@app.route('/application/<int:application_id>/', methods=['GET','POST'])
def showFeatures(application_id):
    application = session.query(Application).filter_by(id=application_id).one()
    features = session.query(Feature).filter_by(application_id=application.id).all()
    return render_template('feature.html', application=application, features=features)


@app.route('/application/<int:application_id>/feature/new', methods=['GET','POST'])
def createFeature(application_id):
    if request.method == 'POST':
        newFeature = Feature(title = request.form['title'],description=request.form[
                           'description'], client=request.form['client'],
                           client_priority=request.form['client_priority'],
                           target_date=request.form['target_date'],
                           product_area=request.form['product_area'],
                           application_id=application_id)
        session.add(newFeature)
        session.commit()
        flash("New feature created")
        return redirect(url_for('showFeature', application_id =
            application_id))
    else:
        return render_template('newFeature.html', application_id =
            application_id)


@app.route('/application/<int:application_id>/feature/<int:feature_id>/edit', methods=['GET','POST'])
def editFeature(application_id, feature_id):
    editedFeature = session.query(Feature).filter_by(id=feature_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editedFeature.title = request.form['title']
        if request.form['description']:
            editedFeature.description = request.form['description']
        if request.form['client']:
            editedFeature.client = request.form['client']
        # if request.form['client_priority']:
        #     editedFeature.client_priority = request.form['client_priority']
        # if request.form['target_date']:
        #     editedFeature.target_date = request.form['target_date']
        if request.form['product_area']:
            editedFeature.product_area = request.form['product_area']
        session.add(editedFeature)
        session.commit()
        return redirect(url_for('showFeature', application_id=application_id))
    else:

        return render_template(
            'editFeature.html', application_id=restaurant_id, feature_id=feature_id, feature=editedFeature)


@app.route('/application/<int:application_id>/feature/<int:feature_id>/delete', methods=['GET','POST'])
def deleteFeature(application_id, feature_id):
    featureToDelete = session.query(Feature).filter_by(id=feature_id).one()
    if request.method == 'POST':
        session.delete(featureToDelete)
        session.commit()
        return redirect(url_for('showFeature', application_id=application_id))
    else:
        return render_template('deleteFeature.html', feature=featureToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

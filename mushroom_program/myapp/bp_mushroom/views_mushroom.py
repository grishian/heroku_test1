import logging
from myapp import db
from myapp.bp_mushroom import bp_mushroom
from myapp.bp_mushroom.model_mushroom import Mushroom, Note
from flask import render_template, url_for, request, redirect, flash, abort

logging.basicConfig(filename='example.log', level=logging.ERROR)


@bp_mushroom.route('/mushrooms')
def do_your_mushrooms():
    mushrooms = Mushroom.query.all()

    return render_template('mushroom/mushrooms.html', title='Mushrooms', mushrooms=mushrooms)


@bp_mushroom.route('/mushroom/<id>')
def do_mushroom(id):
    try:
        mushroom = Mushroom.query.get(id)
        mushroom_name = mushroom.name
    except Exception as e:
        logging.error('Error while getting mushroom id: {}'.format(e))
        abort(404)

    return render_template('mushroom/mushroom.html', title=mushroom_name, mushroom=mushroom)


@bp_mushroom.route('/create_mushroom', methods=['GET', 'POST'])
def do_create_mushroom():
    if request.method == 'POST':

        try:
            name = request.form.get('mushroom_name')
            spawn_temp = request.form.get('spawn_temp')
            fruit_temp = request.form.get('fruit_temp')
            spawn_fae = request.form.get('spawn_fae')
            fruit_fae = request.form.get('fruit_fae')
            mushroom_img = request.form.get('mushroom_img')
        except Exception as e:
            logging.error('Error in do_create_mushroom: {}'.format(e))
            abort(404)

        mushroom = Mushroom(name=name,
                            spawn_temperature=spawn_temp,
                            fruit_temperature=fruit_temp,
                            spawn_fae=spawn_fae,
                            fruit_fae=fruit_fae,
                            mushroom_img=mushroom_img)

        try:
            db.session.add(mushroom)
            db.session.commit()
        except Exception as e:
            logging.error('Error in do_create_mushroom: {}'.format(e))
            abort(500)

        try:
            note_title = request.form.get('note_title')
            note_body = request.form.get('note_body')
        except Exception as e:
            logging.error('Error in do_create_mushroom: {}'.format(e))
            abort(404)

        note = Note(title=note_title,
                    body=note_body,
                    mushroom_id=mushroom.id)

        try:
            db.session.add(note)
            db.session.commit()
        except Exception as e:
            logging.error('Error in do_create_mushroom: {}'.format(e))
            abort(500)

        flash('Mushroom added', 'OK')
        return redirect(url_for('bp_mushroom.do_your_mushrooms'))

    return render_template('mushroom/create_mushroom.html', title='Create mushroom')


@bp_mushroom.route('/delete_mushroom/<id>', methods=["GET", "POST"])
def do_delete_mushroom(id):
    from myapp.bp_grow_run.model_grow_run import GrowRun
    # delete first notes
    # also growrun

    try:
        GrowRun.query.filter_by(mushroom_id=id).delete()
        Note.query.filter_by(mushroom_id=id).delete()
        Mushroom.query.filter_by(id=id).delete()
    except Exception as e:
        logging.error('Error in do_delete_mushroom: {}'.format(e))
        abort(500)

    try:
        db.session.commit()
    except Exception as e:
        logging.error('Error in delete_mushroom: {}'.format(e))
        abort(500)

    flash('Mushroom successfully deleted', 'OK')
    return redirect(url_for('bp_mushroom.do_your_mushrooms'))


@bp_mushroom.route('/edit_mushroom/<id>', methods=["GET", "POST"])
def do_edit_mushroom(id):
    try:
        mushroom = Mushroom.query.get(id)
    except Exception as e:
        logging.error('Error in do_edit_mushroom: {}'.format(e))
        abort(404)

    if request.method == 'POST':

        try:
            mushroom.name = request.form.get('edit_name')
            mushroom.spawn_temperature = request.form.get('edit_spawn_temp')
            mushroom.fruit_temperature = request.form.get('edit_fruit_temp')
            mushroom.spawn_fae = request.form.get('edit_spawn_fae')
            mushroom.fruit_fae = request.form.get('edit_fruit_fae')
            mushroom.mushroom_img = request.form.get('edit_img_url')
        except Exception as e:
            logging.error('Error in do_edit_mushroom: {}'.format(e))
            abort(404)

        try:
            db.session.commit()
        except Exception as e:
            logging.error('Error in do_edit_mushroom: {}'.format(e))
            abort(500)

        flash('Mushroom successfully updated.', 'OK')
        return redirect(url_for('bp_mushroom.do_mushroom', id=id))

    return render_template('mushroom/edit_mushroom.html', mushroom=mushroom)

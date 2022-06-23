import logging
from myapp import db
from datetime import datetime
from myapp.bp_grow_run import bp_grow_run
from myapp.bp_grow_run.model_grow_run import GrowRun, any_active
from flask import render_template, url_for, flash, redirect, request, abort

logging.basicConfig(filename='example.log', level=logging.ERROR)


@bp_grow_run.route('/grow_runs', methods=['GET', 'POST'])
def do_grow_runs():
    grow_runs = GrowRun.query.all()
    return render_template('grow_run/grow_runs.html', title='Grow runs', grow_runs=grow_runs)


@bp_grow_run.route('/grow_run/<id>', methods=['GET', 'POST'])
def do_grow_run(id):
    try:
        grow_run = GrowRun.query.get(id)
        temperature_objects = grow_run.temperatures

    except Exception as e:
        logging.error('Error in do_grow_run: {}'.format(e))
        abort(404)

    temperatures = []

    for temperature_obj in temperature_objects:
        temperatures.append(temperature_obj.celsius)

    temperatures = temperatures[-60:]

    if request.method == 'POST':
        if any_active():
            flash('You can only have 1 active grow run.', 'ERROR')

        if not any_active():
            flash('Grow run activated.', 'OK')

            try:
                grow_run.activate()
                db.session.commit()
            except Exception as e:
                logging.error('Error in do_grow_run: {}'.format(e))
                abort(500)

        mushroom_stage = int(request.form['flexRadioDefault'])
        spawn_start = grow_run.spawn_start
        fruit_start = grow_run.fruit_start

        if mushroom_stage == 0:
            spawn_start = datetime.now()
        if mushroom_stage == 1:
            fruit_start = datetime.now()

        grow_run.spawn_start = spawn_start
        grow_run.fruit_start = fruit_start

        try:
            db.session.add(grow_run)
            db.session.commit()
        except Exception as e:
            logging.error('Error in do_grow_run: {}'.format(e))
            abort(500)

        return redirect(url_for('bp_grow_run.do_grow_runs'))

    return render_template('grow_run/grow_run.html',
                           grow_run=grow_run,
                           temperatures=temperatures)


@bp_grow_run.route('/grow_runs/create', methods=['GET', 'POST'])
def do_create_grow_run():
    from myapp.bp_mushroom.model_mushroom import Mushroom
    mushrooms = Mushroom.query.all()

    if request.method == 'POST':

        try:
            mushroom_id = request.form.get('slim_select')
            grow_run_active = bool(request.form.get('flexSwitchCheckChecked'))
        except Exception as e:
            logging.error('Error in do_create_grow_run: {}'.format(e))
            abort(404)

        try:
            if grow_run_active and any_active():
                flash('You can only have 1 active grow run.', 'ERROR')
                return redirect(url_for('bp_grow_run.do_grow_runs'))
        except Exception as e:
            logging.error('Error in do_create_grow_run: {}'.format(e))
            abort(403)

        try:
            mushroom_stage = int(request.form['flexRadioDefault'])
        except Exception as e:
            logging.error('Error in do_create_grow_run: {}'.format(e))
            abort(404)

        spawn_start = None
        fruit_start = None

        if grow_run_active and not (mushroom_stage == 2):
            if mushroom_stage == 0:
                spawn_start = datetime.now()
            if mushroom_stage == 1:
                fruit_start = datetime.now()

        grow_run = GrowRun(mushroom_id=mushroom_id,
                           mushroom_stage=mushroom_stage,
                           active=grow_run_active,
                           spawn_start=spawn_start,
                           fruit_start=fruit_start)

        try:
            db.session.add(grow_run)
            db.session.commit()

        except Exception as e:
            logging.error('Error in do_create_grow_run: {}'.format(e))
            abort(500)

        flash('Grow run added.', 'OK')
        return redirect(url_for('bp_grow_run.do_grow_runs'))

    return render_template('grow_run/create_grow_run.html', mushrooms=mushrooms)


# deactivate
@bp_grow_run.route('/grow_run/deactivate/<id>')
def do_grow_run_deactivate(id):
    try:
        grow_run = GrowRun.query.get(id)
        grow_run.deactivate()
    except Exception as e:
        logging.error('Error in do_grow_run_deactivate: {}'.format(e))
        abort(404)

    try:
        db.session.commit()
    except Exception as e:
        logging.error('Error in do_grow_run_deactivate: {}'.format(e))
        abort(500)

    flash('Grow run deactivated', 'OK')
    return redirect(url_for('bp_grow_run.do_grow_runs'))

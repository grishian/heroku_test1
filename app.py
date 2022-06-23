import sys
from myapp import create_app, db
from myapp.bp_mushroom.model_mushroom import Mushroom, Note
from myapp.bp_grow_run.model_grow_run import GrowRun
from myapp.bp_temperature.model_temperature import Temperature

sys.dont_write_bytecode = True
app = create_app()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://bjezvhhfftcyrh:5630891f41f41d8fb1619a2b233d1d83e17fe47dcbd6a342ad1a3abfa5d0d4b2@ec2-3-234-131-8.compute-1.amazonaws.com:5432/dqll7ol23g1ct'


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Mushroom': Mushroom,
            'GrowRun': GrowRun,
            'Temperature': Temperature,
            'Note': Note}


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

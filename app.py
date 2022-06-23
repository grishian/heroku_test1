import sys
from myapp import create_app, db
from myapp.bp_mushroom.model_mushroom import Mushroom, Note
from myapp.bp_grow_run.model_grow_run import GrowRun
from myapp.bp_temperature.model_temperature import Temperature

sys.dont_write_bytecode = True
app = create_app()
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://mepibbmvvnbwfh:a14f94760b262eeef612998d44ec2f38e4915af5c9562f380ee468d9bf6021cc@ec2-52-73-184-24.compute-1.amazonaws.com:5432/d1705qth3lr9h4'


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Mushroom': Mushroom,
            'GrowRun': GrowRun,
            'Temperature': Temperature,
            'Note': Note}


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

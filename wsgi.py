from lore import create_app, db
from lore.models.fill import maker

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db':db,
            'maker':maker}
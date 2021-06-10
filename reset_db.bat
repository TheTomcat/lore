rmdir /S /Q ../migrations
del lore\app.db
flask db init
copy /Y script.py.mako migrations\script.py.mako
flask db migrate -m init
flask db upgrade
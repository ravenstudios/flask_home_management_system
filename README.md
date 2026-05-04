
# Flask Home Management System

Home management system for tasks for the family.





## Deployment

To deploy this project first create a virtual environment.
```
python3 -m venv venv
```

Activate environment.

```
source /venv/bin/activate
```

Download and install packages.

```
pip3 install -r requirements.txt
```
Set exports
```
export FLASK_APP=app
export FLASK_DEBUG=1
```
Run flask.

```
flask run
```

Make sure to create a .env file and set SECRET_KEY from command below

"SECRET_KEY=key from command below"
# python -c "import secrets; print(secrets.token_hex(32))"

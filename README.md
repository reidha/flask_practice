# flask_practice

## References

### Real Python

- https://realpython.com/flask-connexion-rest-api/
- https://realpython.com/flask-connexion-rest-api-part-2/
- https://realpython.com/flask-connexion-rest-api-part-3/

### Tutorial

- https://flask.palletsprojects.com/en/2.3.x/

### Other info

- https://stackoverflow.com/questions/61340890/split-openapi-paths-into-multiple-path-definition-files (How to split OpenAPI settings into many YAML files.)
- https://github.com/spec-first/connexion/issues/254#issuecomment-504699959 (How to load multiple YAML files via Connexion)

## Settings

### Environment variables

Name|Value|Purpose
---|---|---
PYTHONPATH|Path to this repository|Need to run scripts in `/tools/`

Sample commands
```
$ export PYTHONPATH="$PYTHONPATH:/path/to/..."
```

### Configuration files

Put configuration files in `/instance/`

Sample
```
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1/temp"
SQLALCHEMY_TRACK_MODIFICATIONS=False
DEBUG=True
TESTING=True
```

## Start the program

```
(.venv) $ python app.py 
(.venv) $ python app.py -e prod  # Use `-e` to select a configuration file
```

## Others

### Virtual environment

```
# Create a new environment
$ git clone 
$ python3 -m venv .venv

# Activate
$ source .venv/bin/activate

# Install libraries
$ pip install -r requirements.txt

# Deactivate
(.venv) $ deactivate
```

### Create requirements.txt

```
$ pip freeze > requirements.txt  
```

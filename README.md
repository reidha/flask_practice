# flask_practice

## References

### Real Python

- https://realpython.com/flask-connexion-rest-api/
- https://realpython.com/flask-connexion-rest-api-part-2/
- https://realpython.com/flask-connexion-rest-api-part-3/

### Tutorial

- https://flask.palletsprojects.com/en/2.3.x/

### Other info

- https://stackoverflow.com/questions/61340890/split-openapi-paths-into-multiple-path-definition-files

## Settings

### Environment variables

Name|Value|Purpose
---|---|---
PYTHONPATH|Path to this repository|Need to run scripts in `/tools/`

Sample commands
```
$ export PYTHONPATH="$PYTHONPATH:/path/to/..."
```

## Commands

### Start

```
(.venv) $ python app.py 
```

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

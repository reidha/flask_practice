# flask_sample_architecture

## References

### Real Python

- https://realpython.com/flask-connexion-rest-api/
- https://realpython.com/flask-connexion-rest-api-part-2/
- https://realpython.com/flask-connexion-rest-api-part-3/

### Official tutorial

- https://flask.palletsprojects.com/en/2.3.x/
- https://github.com/pallets/flask/tree/2.3.3/examples/tutorial

### Other info

- https://stackoverflow.com/questions/61340890/split-openapi-paths-into-multiple-path-definition-files (How to split OpenAPI settings into many YAML files.)
- https://github.com/spec-first/connexion/issues/254#issuecomment-504699959 (How to load multiple YAML files via Connexion)
- https://stackoverflow.com/questions/50355269/configure-python-flask-app-to-use-create-app-factory-and-use-database-in-model (About TestConfig)
- https://github.com/tanakatsu/flask-largeapp-sample (Define `db` in `models/__init__.py`)

### Other info (Non-English)

- https://ai-can-fly.hateblo.jp/entry/flask-directory-structure (Flask directory structure)
- https://qiita.com/mink0212/items/40e4f796eb4ba7868c08 (pytest)
- https://qiita.com/mink0212/items/34b9def61d58ab781714 (pytest-cov)
- https://qiita.com/_akiyama_/items/9ead227227d669b0564e (pytest: fixture)

## Settings

### Environment variables

Name|Value|Purpose
---|---|---
PYTHONPATH|Path to this repository|Run scripts in `/tools/`
FLASK_CONFIG|'prod'|If not set, 'default' will be used
FLASK_APP|File or directory name as the entry point|You have to set `"app"` to run this code

Sample commands
```
$ export PYTHONPATH="$PYTHONPATH:/path/to/..."
$ export FLASK_CONFIG="test"
$ export FLASK_APP="app"
```

### Secret configuration files

Put configuration files (`.cfg`) in `/instance/`. The file will not be uploaded to Git.

Sample (`/instance/default.cfg`)
```
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1/temp"
```

## Start the program

```
(.venv) $ flask run 
(.venv) $ flask run --debug
```

## Test

```
(.venv) $ pytest -v --cov --cov-branch
(.venv) $ pytest -v --cov --cov-branch --disable-warnings
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

### nb-clean

- Use `nb-clean` https://pypi.org/project/nb-clean/ to prevent ipynb outputs from being pushed to Git.
- Run `nb-clean add-filter --remove-empty-cells` once and it's valid as long as you keep the local repo. (If this becomes valid successfully, you can see the change in `.git/config`.)

### Install the environment

```sh
poetry install
```

### Run

```sh
poetry run python main.py
```

### Convert ui to py

```sh
bash convert.py
```

### Run tests / coverage

You can run tests / coverage simply by running the following commands:

```sh
poetry run coverage run -m unittest discover
```

If you want to go further, here is some usefull commands to use

```sh
coverage xml  # create the cobertura coverage.xml file -- do not commit it
coverage json # same file but in json -- do not commit it
coverage html # generate a htmlcov folder with coverage result as HTML file -- do not commit it
coverage report # get report in the console

poetry run python -m unittest discover # run only unittest and don't evaluate coverage
poetry run python -m unittest test_module1 test_module2  # run only some modules
poetry run python -m unittest test_module.TestClass      # run only one class in a module
poetry run python -m unittest test_module.TestClass.test_method # run only 1 test in a class
```

### Freeze the environment

In case you install a new dependency, don't forget to update the requirements.txt 😉

```sh
poetry export -f requirements.txt --output requirements.txt
```

# Links

[QT Designer](https://build-system.fman.io/qt-designer-download)
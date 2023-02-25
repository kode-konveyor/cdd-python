tests:
	PYTHONPATH=src:test python3 -m unittest discover -s test

mutation:
	PYTHONPATH=src:test mutmut run --runner "python -m unittest discover test"

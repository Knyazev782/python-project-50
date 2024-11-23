install:
	poetry install
lint:
	poetry run flake8 gendiff tests
check:
	poetry run flake8 .
	poetry run pytest
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml:coverage.xml

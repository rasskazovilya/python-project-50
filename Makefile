install:
	poetry install

run-gendiff:
	poetry run gendiff
	
build:
	poetry build

publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl
	
package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
	
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff
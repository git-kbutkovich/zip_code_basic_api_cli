install:
	poetry install


clean:
	rm -rf out
	rm -rf site

lint: clean
	@echo "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~ linting - black"
	poetry run black  --config pyproject.toml --check --diff ./
	@echo "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~ linting - mypy"
	poetry run mypy --config-file ./setup.cfg dags
	@echo "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~ linting - isort"
	poetry run isort --settings-path ./setup.cfg --check-only ./
	@echo "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~ linting - flake8"
	poetry run flake8 --config ./setup.cfg ./
	@echo "\n"

fix-lint:
	poetry run isort --settings-path ./setup.cfg ./
	poetry run black --config pyproject.toml ./


run:
	uvicorn main:app --reload

upload_zip_codes:
	poetry run python zip_code_files/upload_to_postgres.py

cli: # TODO: expand to accept zip_code parameter
	poetry run python ./zip_code/cli.py fetch-data --zip_code 85755

	

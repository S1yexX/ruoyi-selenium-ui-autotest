# Web Framework

This repository contains a Selenium-based web automation framework using pytest.

## Project structure

- `testcases/`: pytest test files and test data
- `poms/`: page object models
- `bases/`: base page classes and shared behavior
- `commons/`: utility modules
- `files/`: auxiliary files such as exported artifacts or attachments
- `report/`: generated Allure report output
- `temps/`: generated pytest/Allure temporary test results

## Run tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run pytest:

```bash
pytest
```

Generate Allure report:

```bash
allure generate -o report -c temps
```

# A few notes

## Clean up current environment
pip uninstall virtualenv</br>
pip uninstall pipenv</br>
pip install pipenv</br>

## Upgrade local pip
python.exe -m pip install --upgrade pip

## Install web-server environment
pipenv install uvicorn
pipenv install fastapi

## Run the server
pipenv run uvicorn main:app --reload
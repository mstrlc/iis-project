# iis-project
FIT VUT — IIS — information system for a public transport company

## Installation

- copy `.env.example` to `.myenv`
```
cp .env.example .myenv
```
- replace `DATABASE_URI` with your connection string in `.myenv`
```
DATABASE_URI=mysql+pymysql://root:<your_password>@localhost/transport
```
- run
```
virtualenv ven
set -a
. .myenv
set +a 
source venv/bin/activate
pip install -r requirements.txt
flask run --host=0.0.0.0
```

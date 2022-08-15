# ml-model-deploy
Datasets: https://www.kaggle.com/datasets/mirichoi0218/insurance

Local running.
To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

1. **Installation**

Clone the repo

```bash
git clone https://github.com/spacenew/ml-model-deploy.git
```
cd into the project root folder

```bash
cd ml-model-deploy
```
2. **Create virtual environment**

*via python**

Then you should create a virtual environment named .venv

Installing dependencies
```bash
python -m venv .venv
```
Install pipenv:

```bash
pip install pipenv
```

Install the dependencies:

```bash
pipenv install
```

 2.  Activate virtual env:

```bash
pipenv shell
```

 3. Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd ml-model-deploy/
 streamlit run health_insurance_app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
```

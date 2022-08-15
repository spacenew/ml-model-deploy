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

*via python*

Install pipenv:

```bash
pip install pipenv
```

Install the dependencies from Pipfile:

```bash
pipenv install
```

 2.  Activate virtual env:

```bash
pipenv shell
```

 3. **Build and run the Application Locally**.

 ```bash
 cd ml-model-deploy/
 streamlit run health_insurance_app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
```

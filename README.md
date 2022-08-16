# streamlit-health-insurance-predict


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
3. **Build and run the Application using gunicorn**
if you want to retrain the model and resave the model you can do it by running

```bash
python ./packages/train.py
```
To deploy the Flask app locally using gunicorn. 

*Run it directly via python file*
```bash
python predict.py
```
*Using gunicorn*

```bash
gunicorn --bind 0.0.0.0:9696 predict:app
```
Project should be running locally at http://localhost:9696

*Run the script to make test forecast*

```bash
python test.py
```

 4. **Build and run the Streamlit Application Locally**.

 ```bash
 streamlit run app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
  Network URL: http://192.168.0.71:8501
```

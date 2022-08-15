# ml-model-deploy


As a first step to becoming familiar with our web app's functioning, we recommend setting up a running instance on your own local machine.

To do this, follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):


1. Installing dependencies

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
    Network URL: http://192.168.43.41:8501
```

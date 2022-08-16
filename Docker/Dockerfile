FROM python:3.9.9-slim

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "predict.py", "./" ]
COPY [ "best_rf_model.b", "./models/" ]

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]
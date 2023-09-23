FROM python:3.10-slim

ENV PYTHONUNBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

# equivalent to the cd command in Linux
WORKDIR /app

# copy to app folder
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install dependencies and clean cache
RUN pipenv install --deploy --system && \
rm -rf /root/.cache

# copy project files to app folder
COPY ["*.py", "churn_model.bin", "./"]

# port our application will use
EXPOSE 9696

# how application should be started:
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"]
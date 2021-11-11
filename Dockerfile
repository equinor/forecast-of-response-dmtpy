# run stage
FROM python:3.8-slim as run


COPY . /gen/

WORKDIR /gen
RUN pip install -r requirements.txt -r requirements-dev.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

RUN pylint ForApp --errors-only


RUN python setup.py clean --all sdist bdist_wheel

RUN chmod +x publish.sh
ENTRYPOINT ["sh", "publish.sh"]
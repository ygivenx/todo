FROM python:3.8.2

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY poetry.lock pyproject.toml ./

ENV PATH="${PATH}:/root/.poetry/bin"

RUN poetry config virtualenvs.create false --local

RUN poetry install --no-dev

COPY . .

CMD ["python", "run.py"]

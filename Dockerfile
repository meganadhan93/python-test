FROM python:3
ADD account.py /
ADD account_test.py /
RUN pip install flake8 pytest
CMD ["pytest"]
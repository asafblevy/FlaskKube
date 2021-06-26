FROM python:3.8
LABEL "Maintainer"="Asaf Bein Levy"
LABEL version="1.0"
LABEL description="Simple flask application listening on port 3000."

EXPOSE 3000
EXPOSE 5000
RUN mkdir /app
WORKDIR /app
ADD app/ .
RUN pip install -r requirements.txt

CMD ["python", "/app/server.py" , "3000"]


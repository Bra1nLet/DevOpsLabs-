# Лабораторні роботи з DevOps
# Виконав студент групи ІО-06 
# Остапенко Богдан


Сервіс був написан на Django

Докерфайл для сервісу: 

```
FROM python:3.9-alpine
# RUN apt update && apt install -y gcc libmariadb-dev-compat
ENV PYTHONBUFFERED 1
RUN pip install gunicorn
WORKDIR /app
COPY Servicedjango /app
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
        && apk add gcc libc-dev linux-headers postgresql-dev \
        && pip install --upgrade pip \
        && pip install -r requirements.txt \
        && apk del .temp-build-deps

EXPOSE 8000

CMD python manage.py makemigrations appsch
CMD python manage.py makemigrations
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "Servicedjango.wsgi"]
```

Зібраний docker image був завантажен у dockerhub: 
> bra1let/djangodevops:0.2 

Маніфест kubectl для бази данних та сервісу знаходяться у папках(у сервісі 2 реплики, та налаштован livenes probe):
> k8s/postgress
> 
> k8s/django

![image](https://user-images.githubusercontent.com/98806855/208111814-1eceb771-9053-4476-a7e1-ab80e9c35e7b.png)
![image](https://user-images.githubusercontent.com/98806855/208111842-6e5169a5-afa1-4585-81e0-ea22d0a77d8e.png)

Для хелму були написані 2 версії чарта:
>helm/v1
>
>helm/v2

Сервіс також був розгорнут, та налаштован у Argo CD: 
![image](https://user-images.githubusercontent.com/98806855/208112528-728d0e52-edde-42a2-a890-01f24340f7c5.png)
![image](https://user-images.githubusercontent.com/98806855/208112567-2845241a-ba81-45a1-8c42-ec3218f12776.png)
![image](https://user-images.githubusercontent.com/98806855/208112605-7a89d24d-a6de-4d0b-83ce-d52628dd3e72.png)
![image](https://user-images.githubusercontent.com/98806855/208112724-712fc346-3e4b-4b21-9b36-b6116c93ab41.png)

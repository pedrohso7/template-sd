FROM python:3.10-slim

WORKDIR /app

COPY . .

# O banco de dados será criado pelo código, mas garantimos que o diretório existe
RUN mkdir -p data

EXPOSE 5000

CMD ["python", "main.py"]

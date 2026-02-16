FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# قم بتشغيل سكربت إنشاء القاعدة قبل بدء التطبيق
CMD ["sh", "-c", "python setup_dt.py && python main.py"]

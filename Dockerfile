# Используем официальный Python
FROM python:3.10

# Указываем папку, куда Render кладет файлы
WORKDIR /opt/render/project/src

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем бота
CMD ["python", "main.py"]
FROM python:3.10

# Install dependencies
ADD qr_generator.py .

RUN pip install qrcode

CMD [ "python", "./qr_generator.py" ]

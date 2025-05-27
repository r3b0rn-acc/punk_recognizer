FROM punk_recognizer_base AS web

COPY . .

COPY docker/scripts/web-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "wsgi:application", "--bind", "0.0.0.0:8000"]

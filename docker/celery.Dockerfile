FROM punk_recognizer_base AS celery

COPY . .

COPY docker/scripts/celery-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["celery", "-A", "celery_app:app", "worker", "--loglevel=info", "--concurrency=2", "--prefetch-multiplier=1"]

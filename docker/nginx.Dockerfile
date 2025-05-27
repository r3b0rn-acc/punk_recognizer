FROM nginx:latest

# It needs to export 2 types of nginx templates cuz malo gemora
COPY nginx/nginx.ssl.template /etc/nginx/templates/nginx.ssl.template
COPY nginx/nginx.dev.template /etc/nginx/templates/nginx.dev.template

COPY docker/scripts/nginx-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
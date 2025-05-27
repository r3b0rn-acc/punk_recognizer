FROM nginx:latest

COPY nginx-entrypoint.sh /nginx-entrypoint.sh
COPY nginx.conf.template /etc/nginx/templates/nginx.conf.template
RUN chmod +x /nginx-entrypoint.sh
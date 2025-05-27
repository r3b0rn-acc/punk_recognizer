FROM nginx:latest

# It needs to export 2 types of nginx templates cuz malo gemora
COPY nginx.ssl.template /etc/nginx/templates/nginx.ssl.template
COPY nginx.dev.template /etc/nginx/templates/nginx.dev.template

COPY nginx-entrypoint.sh /nginx-entrypoint.sh
RUN chmod +x /nginx-entrypoint.sh
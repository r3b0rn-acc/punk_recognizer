#!/bin/sh
set -e

echo "Generating nginx config"
if [ "$USE_SSL" = "1" ]; then
  TEMPLATE=/etc/nginx/templates/nginx.ssl.template
else
  TEMPLATE=/etc/nginx/templates/nginx.dev.template
fi

envsubst '$SERVER_NAME $SSL_CERTIFICATE $SSL_CERTIFICATE_KEY' < "$TEMPLATE" > /etc/nginx/conf.d/default.conf

echo "Launching nginx"
exec nginx -g 'daemon off;'
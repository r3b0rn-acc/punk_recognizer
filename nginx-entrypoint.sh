#!/bin/sh
set -e

echo "Generating nginx config"
envsubst '$SERVER_NAME' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/conf.d/default.conf

echo "Launching nginx"
exec nginx -g 'daemon off;'
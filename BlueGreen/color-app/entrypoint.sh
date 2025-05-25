#!/bin/sh

COLOR=${COLOR:-gray}

echo "<h1 style='color: $COLOR;'>$COLOR</h1>" > /usr/share/nginx/html/index.html

# Inicia o nginx
nginx -g "daemon off;"
::
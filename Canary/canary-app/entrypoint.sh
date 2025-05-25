#!/bin/sh

VERSION=${VERSION:-"v1"}
echo "<html><body><h1>Carany App - Versão $VERSION</h1></body></html>" > /usr/share/nginx/html/index.html

nginx -g "daemon off;"

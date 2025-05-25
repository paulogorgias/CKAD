FROM nginx:alpine

# Copia os arquivos
COPY entrypoint.sh /entrypoint.sh

# Torna o script executável
RUN chmod +x /entrypoint.sh

# Substitui o index.html dinâmicamente e inicia o nginx
CMD ["/entrypoint.sh"]

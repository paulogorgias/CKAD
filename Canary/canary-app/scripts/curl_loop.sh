#!/bin/bash

SERVICE_URL="http://localhost:8181"  # Altere para o endereço do seu serviço

echo "🔁 Aguardando até que a aplicação responda com 'v2'..."

while true; do
  output=$(curl -s "$SERVICE_URL")
  echo "$output"
  
  if echo "$output" | grep -q "v2"; then
    echo "✅ Versão v2 detectada. Encerrando loop."
    break
  fi

  sleep 2
done

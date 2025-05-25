# Probes

Este diretório contém exemplos e explicações sobre o uso de probes no Kubernetes. Probes são utilizados para verificar a saúde e a disponibilidade de containers em execução.

## Tipos de Probes

1. **Liveness Probe**: Verifica se o container está em um estado funcional. Se falhar, o container será reiniciado.
2. **Readiness Probe**: Determina se o container está pronto para receber tráfego. Se falhar, ele será removido do serviço.
3. **Startup Probe**: Garante que o container inicializou corretamente antes de outras probes serem executadas.

## Arquivos

- **`liveness.yaml`**: Exemplo de configuração de Liveness Probe.
- **`readiness.yaml`**: Exemplo de configuração de Readiness Probe.
- **`startup.yaml`**: Exemplo de configuração de Startup Probe.

## Como Usar

1. Edite os arquivos YAML conforme necessário.
2. Aplique os manifestos ao cluster Kubernetes:
    ```bash
    kubectl apply -f <arquivo>.yaml
    ```
3. Verifique os logs e o comportamento dos pods para validar as probes.

## Referências

- [Documentação Oficial do Kubernetes - Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
- [Exemplos no GitHub](https://github.com/kubernetes/examples)

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar os exemplos neste diretório.

---
**Nota**: Certifique-se de que o cluster Kubernetes está configurado corretamente antes de aplicar os manifestos.
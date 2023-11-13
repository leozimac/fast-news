# Uma breve explicação de cada campo preenchido no arquivo de manifesto (deployment.yaml)
## Deployment
- **apiVersion:** é a versão da API que vamos utilizar para criar um objeto no Kubernetes. Existem diversas APIs no Kubernetes que fazem a comunicação com o cluster para criar os objetos que desejamos. Para ver uma lista de versões das APIs podemos consultar a documentação ou executar o comando: **kubectl api-resources**

- **kind:** é o tipo do objeto que desejamos criar.

- **metadata:** declaramos os metadados do nosso objeto. Nesse caso estamos declarando o nome do nosso objeto Deployment.

- **spec:** aqui colocamos toda a especificação do objeto que será criado. As especificações variam de acordo com o objeto a ser declarado.

- **replicas:** indica a quantidade de replicas que desejamos ter, ou seja, quantos pods nós teremos com a API.

- **selector:** seleciona os recursos baseado no label especificado.
    - **matchLabels:** indica qual o elemento chave valor que será utilizado para selecionar o recurso pela label. Estamos selecionando pela chave valor “app: fastnewsapi”
    estrutura do pod que vamos utilizar.
    - **labels:** é o identificador chave valor dos nossos pods, e com isso conseguem ser selecionados pelos **selectors.** O label do pod será “app: fastnewsapi”.

- **containers:** especificamos quais containers serão executados nesse pod.
    - **- name:** o nome do container no cluster.
    - **image:** a imagem que será utilizada no container.

- **resources:** aqui nós podemos limitar a quantidade de recursos que o container utilizará.

- **ports, -containerPort:** indicamos qual a porta do container.


## Service
- **protocol:** indica qual o protocolo que será utilizado, segue lista de protocolos suportados https://kubernetes.io/docs/reference/networking/service-protocols/

- **selector:** o service seleciona os pods com a label “app:fastnewsapi” para aplicar as configurações.

- **targetPort:** é a porta alvo, ou seja, a porta 80 do nosso container.

- **nodePort:** para termos previsibilidade, indicamos aqui também a porta que configuramos para o nosso Node.
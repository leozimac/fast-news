# fast-news
Esse projeto tem a finalidade de colocar em prática meus conhecimentos sobre desenvolvimento de software, e principalmente os de DevOps.

A solução do projeto será simples e documentada com o que pode ser relevante/interessante.

## Tecnologias utilizadas

### API

**Python3** versão= 3.10.12

**FastAPI** versão= 0.104.1

**Pydantic** versão= 2.4.2

**Uvicorn** versão= 0.23.2


### Infra
**Kubernetes** para orquestrar os containers.

**k3d** para executar o cluster Kubernetes localmente.

**Docker** para criar as imagens e containers.

**MongoDb** como banco de dados da solução.

**Prometheus** para monitorar o Kubernetes.


## Documentação

Na pasta **k8s** tem os arquivos relacionados com o cluster Kubernetes, alguns conceitos e comandos.

**TO DO:** criar um Read.me para a API.
## Objetivos para as próximas versões
- Adicionar o MongoDb para armazenar as noticias.
  - Criar um container para o banco.
  - Adicionar no cluster
- Adicionar o Prometheus para monitorar a solução no Kubernetes:
  - Configurar.
  - Adicionar no cluster.
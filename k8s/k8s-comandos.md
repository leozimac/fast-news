# Comandos utilizados no desenvolvimento desta solução

**Criação do cluster single node** <br>
  `k3d cluster create labcluster`

**Criação do cluster single node com port binding** <br>
  `k3d cluster create labcluster -p "8000:30000@loadbalancer"`

**Visualizar o nó (ou nós) do cluster** <br>
  `kubeclt get nodes`

**Aplicar/Criar os elementos declarados no arquivo de manifesto** <br>
  `kubectl apply -f deployment.yaml`

**Visualizar os Services criados no cluster** <br>
  `kubectl get service`

**Visualizar o Deployment criado** <br>
  `kubectl get deployment`

**Visualizar os pods** <br>
  `kubectl get pods`
 
  `kubectl get po`

# Outros comandos relevantes

- **Criação de um cluster mult node** <br>
  `k3d cluster create nomedocluster --servers 3 --agents 3`

- **Iniciar um cluster criado anteriormente, e por algum motivo está parado** <br>
  `k3d cluster start nomedocluster`

- **Parar um cluster em execução** <br>
  `k3d cluster stop nomedocluster`
  
- **Parar todos os clusters em execução** <br>
  `k3d cluster stop -a`

- **Listar todos os clusters criados** <br>
  `k3d cluster list`

- **Deletar um cluster** <br>
  `k3d cluster delete nomedocluster`
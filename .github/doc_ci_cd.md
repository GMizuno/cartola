# Atualizando ligas

Documentação com o passo a passo para incluir **uma nova liga** na esteira de CI/CD.

OBS: Para subir uma nova liga utilize branches no seguinte formato **league*

### Console do Google Cloud

Para incluir uma nova será necessario deletar so Jobs manualmente no console

### Esteira de CI/CD

[Manifesto](workflows%2Fcloud_run.yml) responsável por realizar o deploy dos Cloud Run. Para atualizar basta seguir o seguinte passo a passo

 1 - Adcionaar as seguintes variaveis dentro do _include_; **IMG, LEAGUE_ID, SEASON_YEAR e TYPE**

### Delete Cloud Run

[Manifesto](workflows%2Fdelete_run.yml) responsável por deletear os Clouds Runners. Para atualizar basta seguir o seguinte passo a passo

1 - Padrão a nova liga **TYPE** (players-statistics, matchs-teams ou OBT) e **LEAGUE_ID** (Ex: 39)
2 - Adicionar a nova liga dentro de _cloud_run_

### Build and Push to Artifact Registry Geral

[Manifesto](workflows%2Fdocker.yml) responsável por buildar a imagem no Artifact Registry. Essa etapa não precisa de atualização
pois não contem variaveis de ambiente, craição do Cloud Run ou qualquer outra etapa q impacte nos jobs.

          
          
          
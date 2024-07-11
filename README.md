## Introdução

O projeto é desenvolver uma api que resolva o problema de classificação de textos(peças) do Direito, trata de uma classificação multilabel para os ramos do direito.
Os dados de Treino apresentou 22 classes.

Para a classificação usei uma tecnica de regressão com outra em cadeia no qual apresentou uma precisão de 67%, para alcançar este resultado eu diminur as classes de 22 para 5 principais ramos os outros ramos não havia dados de textes suficiente para ser treinado. Foi testado 3 modelos de machine learning tanto para classificação.

Coloquei o modelo em produção desenvolvendo uma api com acesso a toda documentação da mesma atravez do Swagger.

## Principais Libs

- _pandas_;
- _scikit-learn_;
- _scikit-multilearn_;
- _nltk_;
- _fastapi_;
- _docker_

## Estrutura

- O treinamento esta descrita no arquivo _primeiro_1.ipynb_;
- No diretorio _dados_ esta dados usados para o treinamento do modelo;
- O arquivo _main.py_ esta o codigo para desenvolvimento da api e o diretorio _ramos_direito/routers_ esta os arquivos de rotas para api;
- _Dockerfile_ arquivo docker para build a aplicação. 

### Colocando em produção

Esteja ciente que a aplicação esta diponivel em uma imagem docker e para isso terá que ter o docker instalado.

Faça o clone do projeto no github e execute

- _docker build -t convergencia-api ._
- _docker run -p 80:80 convergencia-api_

#### Acessando a API

No seu navegador acesse _http://0.0.0.0:80/busca_pecas/5_ lembrando que o ultimo parametro da url é o index da peça de direito a ser classificada.
Acessando _http://0.0.0.0:80/docs_ Acessara a api no Swagger.


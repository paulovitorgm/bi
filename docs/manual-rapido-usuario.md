# Manual rápido do usuário

Este manual orienta o uso diário do sistema **Base de Dados BI** para consulta
e manutenção de processos, pessoas e cadastros de apoio.

## 1. Acesso ao sistema

1. Abra o endereco informado pela equipe responsavel.
2. Informe seu usuario e senha na tela de acesso.
3. Depois de entrar, a pagina inicial mostra a quantidade de processos e
   pessoas cadastradas e oferece atalhos para os cadastros mais usados.

> Não compartilhe sua senha. Em computadores de uso compartilhado, encerre a
> sessão ao terminar.

## 2. Conhecendo o menu

- **Inicio:** resumo e atalhos do sistema.
- **Processos:** consulta e cadastro de processos, convenios e projetos.
- **Pessoas:** consulta e cadastro de pessoas vinculadas aos processos.
- **Cadastros:** manutencao das listas usadas nos formularios, como unidades,
  entidades parceiras, modalidades, naturezas, abrangencias, participes e
  tipos de instrumento.

## 3. Consultar processos

1. Acesse **Processos > Consultar processos**.
2. Use o campo **Buscar** para procurar pelo numero do processo SEI, numero do
   convenio, nome do processo ou coordenador.
3. Clique em **Filtrar**.
4. Se necessario, ajuste a quantidade de registros por pagina.
5. Use os botoes da lista:
   - **Ver:** abre todos os detalhes do processo.
   - **Editar:** altera as informacoes cadastradas.
   - **Excluir:** solicita confirmacao antes de remover o processo.

## 4. Cadastrar um processo

1. Acesse **Processos > Novo processo**.
2. Preencha o numero do **Processo SEI** somente com numeros. Esse numero nao
   pode ser repetido.
3. Informe os dados de identificacao, classificacao, responsaveis, valores e
   datas solicitados pelo formulario.
4. Nos campos de selecao, escolha um registro existente. Quando houver o botao
   **Novo**, ele permite cadastrar o item sem abandonar o formulario.
5. Em **Termos aditivos**, preencha apenas os termos que existirem para o
   processo. Deixe em branco as linhas que nao serao usadas.
6. Clique em **Salvar**.

Se uma data de termino for anterior a data de inicio, o sistema mostrara uma
mensagem e impedira o salvamento ate a correcao.

## 5. Consultar ou editar os detalhes de um processo

1. Na lista de processos, clique em **Ver**.
2. Confira identificacao, classificacao, responsaveis, valores, datas e termos
   aditivos.
3. Para corrigir ou completar dados, clique em **Editar**.
4. Revise as informacoes e clique em **Salvar**.

## 6. Cadastrar e manter pessoas

1. Acesse **Pessoas > Nova pessoa**.
2. Informe nome, matricula e unidade de lotacao.
3. Caso a unidade ainda nao exista, use o botao **Nova** ao lado do campo.
4. Clique em **Salvar Pessoa**.

Na tela **Consultar pessoas**, use a busca por nome ou matricula. Os botoes
**Editar** e **Excluir** ficam ao lado de cada registro.

> A matricula deve identificar uma unica pessoa. Se houver duplicidade, revise
> o cadastro existente em vez de criar outro registro.

## 7. Cadastros de apoio

Antes de criar um processo, confirme que os itens necessarios ja existem em
**Cadastros**. Essas listas alimentam os campos de selecao do formulario.

Para incluir um item:

1. Abra a categoria desejada no menu **Cadastros**.
2. Clique em **Novo cadastro** ou **Novo**.
3. Preencha os dados e salve.

Para corrigir um item, use **Editar**. Use **Excluir** somente quando ele nao
deve mais ser utilizado. Alguns registros vinculados a outros dados nao poderao
ser excluidos; nesse caso, ajuste os vinculos antes de tentar novamente.

## 8. Mensagens e erros mais comuns

| Situacao | O que fazer |
| --- | --- |
| Campo destacado em vermelho | Leia a mensagem abaixo do campo, corrija o valor e salve novamente. |
| Registro ja existente | Pesquise o cadastro antes de criar outro; processos, matriculas e algumas siglas nao podem ser repetidos. |
| Acesso negado (403) | Entre novamente ou solicite permissao a equipe responsavel. |
| Pagina nao encontrada (404) | Confira o endereco ou volte para a pagina inicial. |
| Erro interno (500) | Tente novamente. Se persistir, informe a equipe responsavel com o horario e a acao realizada. |
| Sistema indisponivel (503) | Aguarde alguns minutos e tente novamente; o banco de dados pode estar temporariamente indisponivel. |

## 9. Boas praticas

- Pesquise antes de cadastrar para evitar duplicidade.
- Revise datas, valores e numero do processo antes de salvar.
- Use nomes e siglas padronizados nos cadastros de apoio.
- Nao exclua registros sem verificar se sao usados por processos ou relatorios.
- Ao comunicar um problema, informe a tela acessada, a acao realizada, o horario
  aproximado e, se possivel, uma imagem da mensagem exibida.

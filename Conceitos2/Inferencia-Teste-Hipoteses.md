# Inferência Estatística e Testes de Hipóteses

## Inferência Estatística

### O Que é?

A Inferência Estatística é um ramo da Estatística que vai além da mera descrição de dados, permitindo tirar conclusões e fazer previsões sobre uma população a partir da análise de uma amostra representativa.

Em outras palavras, a Inferência Estatística nos ajuda a generalizar o que observamos em um grupo menor (a amostra) para o todo (a população).

### Como Funciona?

1. Coletar uma amostra aleatória da população que queremos estudar. Essa amostra deve ser representativa da população como um todo, ou seja, conter as mesmas características e proporções.
2. Utilizar métodos estatísticos para descrever e analisar os dados da amostra. Isso pode incluir calcular médias, medianas, desvios padrões, realizar testes de hipóteses, etc.
3. Com base na análise da amostra, fazemos inferências sobre as características da população. Ou seja, estimamos valores populacionais, como a média ou a proporção de um determinado evento.
4. Por fim, interpretamos os resultados da inferência e os comunicamos de forma clara e concisa. É importante lembrar que as inferências estatísticas sempre estão sujeitas a incerteza, por isso, devemos apresentar as margens de erro e o nível de confiança dos resultados.

### Aplicações:

A Inferência Estatística tem diversas aplicações em diversas áreas do conhecimento, como:

- **Pesquisas de opinião**: para estimar a opinião da população sobre um determinado tema.
- **Testes de produtos**: para avaliar a eficácia de um novo medicamento ou produto.
- **Controle de qualidade**: para monitorar a qualidade de um processo de produção.
- **Experimentos científicos**: para testar hipóteses sobre o comportamento de um fenômeno.

### Exemplos:

- Estimar a média da altura dos alunos de uma escola: Coletamos uma amostra aleatória de alunos e calculamos a média da altura dessa amostra. Com base nessa média, podemos estimar a média da altura de todos os alunos da escola.

- Testar se um novo medicamento é eficaz no tratamento de uma doença: Dividimos um grupo de pacientes com a doença em dois grupos: um grupo que recebe o novo medicamento e outro que recebe um placebo. Comparamos a taxa de cura dos dois grupos para testar se o novo medicamento é realmente eficaz.

- Prever o resultado de uma eleição: Coletamos dados sobre as intenções de voto de uma amostra de eleitores e usamos esses dados para prever o resultado da eleição.

> A inferência estatística permite que os Cientistas de Dados e Estatísticos façam generalizações prudentes e apoiadas por evidências a partir de dados limitados, incorporando a variabilidade e a incerteza inerentes aos dados amostrais.

## Testes de Hipóteses
### O que são?
Os testes de hipóteses são uma técnica fundamental em Estatística para decidir, com base em dados amostrais, se há evidências suficientes para rejeitar uma hipótese estabelecida sobre uma população. Essa técnica é amplamente utilizada em muitos campos, como pesquisa científica, economia, medicina e, claro, Data Science, para tomar decisões informadas e baseadas em evidências.


### Principais Componentes 

**Hipótese Nula (H₀)**: É a hipótese que afirma que não há diferença significativa ou efeito, ou que qualquer observação é resultado do acaso. Por exemplo, "não há diferença na média de altura entre homens e mulheres".

**Hipótese Alternativa (H₁ ou Ha)**: É a hipótese que o pesquisador realmente quer testar e geralmente representa uma nova teoria ou uma afirmação de diferença ou efeito. Por exemplo, "a média de altura dos homens é diferente da média de altura das mulheres".

**Nível de Significância (α)**: Este é um limiar pré-definido pelo pesquisador que determina quão forte a evidência deve ser para rejeitar a hipótese nula. Comumente, este valor é 0,05, o que significa que há uma probabilidade de 5% de rejeitar a hipótese nula quando ela é verdadeira (erro tipo I).

**Valor-p**: O valor-p é a probabilidade de obter um resultado pelo menos tão extremo quanto o resultado realmente observado, sob a suposição de que a hipótese nula é verdadeira. Se o valor-p é menor que o nível de significância α, então rejeita-se a hipótese nula.

**Tipo de Teste:** Dependendo da natureza dos dados e da pergunta de pesquisa, diferentes testes podem ser aplicados, como t-testes para médias, testes de chi-quadrado para frequências, testes ANOVA para comparações de várias médias, entre outros.

**Decisão**: Baseado no valor-p e no nível de significância, o pesquisador decide rejeitar ou não rejeitar a hipótese nula. Rejeitar a hipótese nula implica que os resultados são estatisticamente significativos, enquanto não rejeitar sugere que mais dados podem ser necessários para uma conclusão ou que a hipótese nula pode ser verdadeira.

>  Essencialmente, testes de hipóteses são uma maneira sistemática de testar afirmações ou teorias sobre um fenômeno, controlando ao mesmo tempo a taxa de erros cometidos, e são uma parte essencial do processo de inferência estatística.

## Erros Tipo I e Tipo II

Os conceitos de Erros Tipo I e Tipo II têm por objetivo auxiliar a entender as limitações e interpretações dos testes de hipóteses. 

Esses erros representam as duas principais maneiras pelas quais um teste de hipóteses pode chegar a uma conclusão incorreta. Vamos detalhar cada um:

### Erro Tipo I:

Ocorre quando a hipótese nula 𝐻0 é rejeitada incorretamente, apesar de ser verdadeira. Esse erro é também conhecido como um "falso positivo".

A probabilidade de cometer um Erro Tipo I é denotada por α (alfa), que é o nível de significância estabelecido para o teste.

Por exemplo, se α é definido como 0.05, isso significa que há uma chance de 5% de rejeitar a hipótese nula quando ela é verdadeira.

### Erro Tipo II: 
Ocorre quando a hipótese nula 𝐻0 não é rejeitada, apesar de a hipótese alternativa 𝐻1 ser verdadeira.

Esse erro é também conhecido como um "falso negativo".

A probabilidade de cometer um Erro Tipo II é denotada por β (beta). A potência do teste, que é 1 - β, representa a capacidade do teste de corretamente rejeitar a hipótese nula quando a hipótese alternativa é verdadeira.


### Relação entre os erros:

Há uma relação de troca entre o Erro Tipo I e o Erro Tipo II. Diminuir o risco de cometer um Erro Tipo I (reduzindo α) geralmente aumenta o risco de cometer um Erro Tipo II, e vice-versa. Isso ocorre porque ao tornar o teste mais conservador em rejeitar a hipótese nula, pode-se perder a capacidade de detectar um efeito real quando ele existe.

A escolha do nível de significância α e a potência do teste (1 - β) são essenciais no planejamento de um estudo. Elas devem equilibrar os riscos desses erros com as consequências práticas de cometê-los.

Por exemplo, em um contexto médico, um Erro Tipo I pode significar a aprovação de um medicamento ineficaz, enquanto um Erro Tipo II pode resultar no descarte de um tratamento eficaz. Portanto, a escolha de α e β deve considerar as implicações de ambos os erros, especialmente em áreas críticas como a saúde.

## Testes Unilaterais e Bilaterais

Os testes unilaterais e bilaterais são dois tipos de abordagens utilizadas em testes de hipóteses para determinar a relação entre dados e hipóteses. Cada tipo de teste tem suas aplicações específicas, dependendo do que está sendo investigado. Aqui está uma explicação mais detalhada:

### Testes Unilaterais
Um teste unilateral é utilizado quando a hipótese alternativa é direcionada a uma direção específica. Ou seja, você está interessado em testar se um parâmetro é maior ou menor que um valor de referência, mas não ambos.

- Hipótese Alternativa Direita: Testa se os parâmetro é maior que o valo de referência.
Por Exemplo, $H_1 : \mu > \mu_0$

- Hipótese Alternativa Esquerda: Testa se os parâmetro é menor que o valo de referência.
Por Exemplo, $H_1 : \mu < \mu_0$

Os testes unilaterais são geralmente utilizados quando uma mudança em uma direção específica tem implicações práticas, como no caso de verificar se uma nova máquina produz menos defeitos que o modelo anterior.

### Testes Bilaterais

Um teste bilateral é usado quando as implicações de uma diferença em qualquer direção são relevantes. Esse teste verifica se o parâmetro difere (para mais ou para menos) de um valor de referência.

- Hipótese ALternativa: $H_1 : \mu \neq \mu_{0}$ onde $\mu$ é a média da população e $\mu_0$ é um valor específico.

Esse tipo de teste é apropriado quando não há uma razão específica para acreditar que a diferença estará em uma direção particular, ou quando ambas as direções da diferença são igualmente importantes, como testar se um novo tratamento é diferente (melhor ou pior) do tratamento padrão.

### Considerações na Escolha do Teste
Poder Estatístico: Testes bilaterais dividem o nível de significância α entre as duas caudas da distribuição do teste, o que pode torná-los menos poderosos que testes unilaterais para detectar uma diferença em uma direção específica.

Interpretação e Consequências: A escolha entre teste unilateral e bilateral também deve levar em conta as consequências de possíveis erros tipo I e tipo II, e o que é mais crítico para evitar no contexto da pesquisa.

## Testes para Médias, Proporções e Variâncias

Em Estatística, dependendo do tipo de dado e do objetivo do estudo, diferentes tipos de testes são usados para analisar médias, proporções e variâncias.

Cada tipo de teste tem características próprias que o tornam adequado para certas situações. Vamos descrever cada um destes testes para lhe dar uma ideia de como são utilizados:

### Testes para médias:
1. **t-teste (Teste t de Student)**: Usado para comparar as médias de duas amostras independentes ou pareadas para verificar se elas provêm de distribuições com médias iguais. Há também a versão do t-teste para uma amostra, que compara a média de uma única amostra com uma média populacional conhecida.

 * Independentes: Comparar duas amostras diferentes, como dois grupos em um estudo controlado.

 * Pareadas: Comparar duas medidas tomadas no mesmo grupo de sujeitos, como antes e depois de um tratamento.

2. **ANOVA (Análise de Variância)**: Quando há mais de dois grupos, a ANOVA é utilizada para determinar se há diferenças significativas entre as médias dos grupos. Existem várias formas de ANOVA, como ANOVA de um fator ou de múltiplos fatores, dependendo da complexidade do desenho experimental.

### Testes para proporções:

1. **Teste z para uma proporção:** Usado para comparar a proporção observada em uma amostra com uma proporção populacional conhecida.

2. **Teste z para duas proporções**: Comparar as proporções entre duas amostras independentes para verificar se há diferença significativa entre elas.

3. **Teste Qui-quadrado**: Usado para testar hipóteses sobre frequências observadas em categorias. É útil para testar a independência de duas variáveis em uma tabela de contingência ou a adequação de uma distribuição de frequências observadas a uma distribuição esperada.


### Testes para variâncias:

1. **Teste F** para Comparação de Duas Variâncias: Usado para comparar as variâncias de duas amostras independentes. Este teste é importante, por exemplo, no uso preliminar antes de realizar um t-teste, pois muitos t-testes assumem que as variâncias são iguais entre os grupos.

2. **Teste de Levene ou Teste de Bartlett**: Utilizados para verificar a homogeneidade das variâncias entre três ou mais grupos, o que é uma suposição comum em testes como ANOVA.



### Considerações Adicionais
**Suposições**: Cada teste tem suposições que precisam ser atendidas para que os resultados sejam válidos, como normalidade dos dados e independência das observações.

**Tamanho da Amostra e Poder Estatístico**: O tamanho da amostra afeta a capacidade de detectar uma verdadeira diferença ou efeito (poder do teste). Testes inadequados para o tamanho da amostra podem levar a conclusões errôneas.

**Escolha do Teste**: A escolha do teste adequado depende não apenas do tipo de dados, mas também da questão de pesquisa, do desenho do estudo e das suposições específicas associadas a cada teste.

> Ao planejar análises estatísticas, é importante escolher o teste apropriado baseado nas características dos dados e nos objetivos da pesquisa para garantir interpretações corretas e válidas dos resultados.

## Como Definir as Hipóteses no Teste de Hipóteses?

Definir corretamente as hipóteses em um teste de hipóteses é fundamental para garantir que a análise seja válida e os resultados sejam interpretáveis. As hipóteses determinam o foco do teste e orientam a escolha do método estatístico apropriado.

Etapas e considerações principais para definir as hipóteses no teste de hipóteses:

### 1. Identificar o Problema de Pesquisa

Antes de formular as hipóteses, é fundamental entender claramente o problema de pesquisa.

Determine o que você deseja explorar ou provar com seu estudo.

Por exemplo, você pode estar interessado em saber se um novo medicamento é mais eficaz que o tratamento atual.

### 2. Formular a Hipótese Nula (H0)

A hipótese nula é uma declaração de ausência de efeito ou diferença. Ela serve como ponto de partida para o teste e é formulada de modo que possa ser objetivamente testada por meio de dados.

A hipótese nula tipicamente propõe que:

Não há diferença entre os grupos (em termos de média, proporção, etc.).
Não há associação entre as variáveis testadas.

Por exemplo:

H0: A média de pressão arterial para pacientes tomando o novo medicamento é igual à média para aqueles tomando o medicamento padrão. Ou seja, não há diferença.

### 3. Formular a Hipótese Alternativa (H1 ou Ha)

A hipótese alternativa é o que você espera que seja verdade se a hipótese nula for rejeitada. Esta hipótese é formulada com base no objetivo da pesquisa:

Pode indicar uma diferença específica (testes unilaterais) ou qualquer diferença (testes bilaterais).

 Deve ser lógica, baseada em teoria ou em estudos anteriores.

Por exemplo:

H1: A média de pressão arterial para pacientes tomando o novo medicamento é menor do que para aqueles tomando o medicamento padrão (teste unilateral). Ou seja, há diferença.

### 4. Considerar o Tipo de Teste

A escolha entre teste unilateral ou bilateral depende de sua hipótese alternativa:

 * Unilateral: Use se a direção da diferença é importante (maior que ou menor que).
 * Bilateral: Use se qualquer diferença (maior ou menor) é relevante.

### 5. Verificar Suposições

Cada teste estatístico tem suposições que precisam ser verificadas antes de conduzir o teste. Por exemplo, normalidade dos dados para t-testes, homogeneidade de variâncias para ANOVA, etc.

As hipóteses devem ser compatíveis com as suposições do teste escolhido.

### 6. Definir o Nível de Significância (α)

O nível de significância, geralmente fixado em 0,05 (5%), é a probabilidade de rejeitar a hipótese nula quando ela é verdadeira (erro tipo I). A escolha de α impacta a sensibilidade do teste.


> Ao definir as hipóteses, seja claro, específico e assegure que elas sejam testáveis. As hipóteses devem refletir o objetivo da pesquisa e ser formuladas antes da coleta de dados para evitar viés. A correta formulação das hipóteses é fundamental para direcionar toda a análise estatística subsequente e interpretar corretamente os resultados.

## Potência do Teste e Tamanho do Efeito

A **potência de um teste** estatístico é a probabilidade de rejeitar corretamente a hipótese nula quando ela é falsa. Em outras palavras, é a capacidade do teste de detectar um efeito real, quando de fato existe um. A potência do teste é influenciada por vários fatores:

1. **Tamanho do Efeito**: Quanto maior o efeito real que estamos tentando detectar, mais fácil é para o teste identificá-lo.

2. **Tamanho da Amostra**: Maiores amostras proporcionam mais informação e, portanto, aumentam a potência do teste. Por isso Big Data é tão relevante.

3. **Nível de Significância (α)**: Um α maior (como 0,05 em vez de 0,01) aumenta a potência do teste, mas também aumenta a probabilidade de um erro tipo I.

4. **Variabilidade dos Dados**: Menos variabilidade nos dados aumenta a potência, pois o efeito se torna mais discernível contra o "ruído" dos dados.

> Idealmente, deseja-se uma potência de teste alta (comumente 0,80 ou 80% é considerado um bom padrão), o que significa que há uma boa chance de detectar um efeito significativo se ele realmente existir.

O **tamanho do efeito** é uma medida quantitativa da magnitude de um fenômeno. Em Estatística, ele ajuda a determinar se uma diferença ou associação é apenas estatisticamente significativa ou também clinicamente relevante. Existem várias maneiras de medir o tamanho do efeito, dependendo do tipo de dados e do teste utilizado:

1. **Diferença de Médias:** Por exemplo, a diferença entre as médias de dois grupos.

2. **Razão de Odds ou Riscos:** Comumente usado em estudos epidemiológicos para comparar as probabilidades de um evento entre dois grupos.

3. **Tamanho do Efeito de Cohen's d**: Uma medida comum para comparar a diferença entre dois meios em termos de desvio padrão.

Interpreta-se geralmente como:

Pequeno: d = 0,2
Médio: d = 0,5
Grande: d = 0,8

#### Cálculo e Importância

Calcular a potência de um teste geralmente envolve o uso de software estatístico que pode realizar análises de poder e tamanho de amostra. Essas análises permitem aos pesquisadores estimar quantos participantes são necessários para detectar um efeito de tamanho dado com um determinado nível de confiança.

A consideração cuidadosa do tamanho do efeito e da potência do teste é essencial no planejamento de estudos científicos. Isso garante que o estudo tenha recursos suficientes para detectar diferenças significativas, evitando desperdícios de recursos em estudos que são muito pequenos para detectar diferenças práticas importantes.

> Ao planejar um estudo, o tamanho do efeito desejado e a potência necessária devem ser considerados para determinar o tamanho da amostra adequado. Isso maximiza a eficiência do estudo e a probabilidade de resultados úteis, equilibrando a necessidade de precisão estatística com a viabilidade prática.
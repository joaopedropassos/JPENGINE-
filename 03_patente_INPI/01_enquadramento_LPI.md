# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 01 — Enquadramento LPI | ETAPA 0

este texto não substitui agente da propriedade industrial, não constitui protocolo no INPI, não gera prioridade oficial e não é parecer jurídico.

## 1. Objeto e inventor

- **Inventor (PF):** João Pedro Pereira Passos, Palmas/TO.  
- **Afiliação:** UFT / Rede BIONORTE; leciona UNITINS.  
- **Cotitularidade:** PENDENTE — inventor deve verificar contrato/política institucional **antes** de protocolar.  
- **Objeto candidato:** processo implementado em computador (IIC) para planejamento de caminhos em grafo derivado de layout espacial estável (armazém, pátio ou planta industrial), com pré-processamento offline e consultas origem–destino (O-D) online.

## 2. Trilho A versus Trilho B

| Trilho | Instrumento | O que protege | O que NÃO protege | Status recomendado |
|--------|-------------|----------------|-------------------|--------------------|
| **A** | Registro de programa de computador (e-Software) | Expressão do código (via hash) | Ideia, processo, API, marca, efeito técnico do algoritmo | **Executar agora** |
| **B** | Pedido de patente de invenção (IIC) | Processo/sistema com requisitos LPI (novidade, atividade inventiva, aplicação industrial) e fora do art. 10 | Software «em si»; método matemático puro; mera apresentação de informação | **Alto risco** se delta = só ALT+FPS |

Fontes oficiais de registro (Trilho A): Guia Básico INPI — Programas de Computador; FAQ Programas de Computador; Manual do Usuário e-Software; Tabela de Retribuições (Portaria INPI/PR nº 10/2025 / tabela 20_dez_25).  
Diretrizes IIC (Trilho B): **Portaria INPI/PR nº 411, de 23 de dezembro de 2020** (institui Diretrizes de Exame de Pedidos de Patente envolvendo IIC; vigência 01/01/2021; revoga Res. INPI/PR nº 158/2016) — texto confirmado em fonte oficial gov.br. Nomenclatura «Portaria INPI/DIRPA n. 411» **não** coincide com o título oficial do ato; usar **INPI/PR nº 411/2020**.

## 3. Artigo 10, inciso I, LPI — métodos matemáticos

O planejamento de caminho mínimo / shortest path, A*, ALT e desigualdades triangulares com landmarks são, em abstração, **métodos matemáticos / algoritmos de grafo**.  
**Risco:** se as reivindicações se limitarem a «calcular o caminho mais curto com landmarks e desigualdade triangular», o examinador pode enquadrar a matéria no **art. 10, I**, como não invenção.

Mitigação candidata (não garantia): descrever **processo técnico** aplicado a layout industrial concreto (grafo de corredores/obstáculos de armazém/pátio/planta), com etapas de aquisição/atualização do mapa, invalidação de prior, integração a consultas repetidas O-D e efeito técnico mensurável em expansão de estados / tempo de consulta — **sem** reduzir a reivindicação a fórmula matemática isolada.

## 4. Artigo 10, inciso V, LPI — programa de computador em si

O **programa de computador em si** (expressão / código) **não** é considerado invenção (art. 10, V).  
Consequência:  
- Trilho A protege a expressão via registro.  
- Trilho B exige reivindicar **processo** ou **sistema** técnico, não o código-fonte nem o «aplicativo» como tal.

## 5. Efeito técnico candidato versus o que NÃO é efeito técnico

### 5.1 Efeito técnico candidato (hipótese — não deferido)

Nos testes internos informados pelo inventor:  
- **v5**, 1000 consultas: 100% otimalidade; variante geométrica reduziu nós expandidos e tempo versus A* com heurística fixa.  
- **v7:** quando DG = d_grafo / d_Manhattan cresce, landmarks geométricos vencem A*; seleção por geradores topológicos **não** superou FPS.  
- **v6:** variar só beta1 com stretch ~1 **não** deu vantagem topológica sobre geométrica.

**Efeito técnico candidato (não deferido pelo INPI):** redução de estados expandidos e/ou tempo de CPU em **consultas O-D repetidas no mesmo mapa estável**, mantendo otimalidade (admissibilidade da heurística) intacta nos testes internos.

### 5.2 O que NÃO constitui, por si, efeito técnico

- Ganho puramente abstrato de complexidade sem domínio técnico aplicado.  
- Melhoria «de negócio» (margem, opex, NPS) sem nexo técnico.  
- Interface / UX / apresentação de mapa.  
- Meras vantagens comerciais ou de marketing.  
- Afirmação de superioridade topológica (TDA) **sem** suporte experimental — v6/v7 apontam o contrário.

## 6. Núcleo a reivindicar (orientação de redação)

- Offline: prior estrutural + **landmarks geométricos** (ex. FPS) + tabelas de distância.  
- Online: consultas O-D com busca informada tipo ALT, admissibilidade, otimalidade.  
- Reuso do prior enquanto o layout permanecer válido; invalidação quando o mapa mudar.  
- Homologia / Wasserstein / persistência: **não** nas independentes; no máximo 1 dependente opcional com nota v6/v7.

## 7. Pendências críticas do inventor

1. Verificar cotitularidade UFT / órgão público / UNITINS.  
2. Datas e conteúdo de paper interno, one-pager, e-mails Delage/Automni, vídeo.  
3. Linguagens e versão do código a registrar (Trilho A).  
4. Isolar, se existir, delta inventivo **além** de ALT+FPS, com evidência.  
5. Decisão documentada: só Trilho A nesta semana, ou Trilho A + preparação cautelosa de Trilho B sob agente PI.

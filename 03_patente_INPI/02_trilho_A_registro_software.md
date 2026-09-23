# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 02 — Trilho A | Registro de programa de computador | ETAPA 1

**Objetivo:** checklist operacional fiel ao fluxo oficial INPI (e-Software), sem anexar código-fonte a este dossiê.

Fontes: https://www.gov.br/inpi/pt-br/servicos/programas-de-computador/guia-basico ; FAQ Programas de Computador; Manual do Usuário e-Software; Tabela de Retribuições (Portaria INPI/PR nº 10/2025 / tabela 20_dez_25).

## Checklist operacional (1–8)

### 1. Cadastro e-INPI
- [ ] Inventor (ou titular) possui cadastro ativo no **e-INPI**.  
- PENDENTE: confirmar login e dados cadastrais atualizados (CPF, endereço Palmas/TO).

### 2. Certificado digital ICP-Brasil (e-CPF)
- [ ] Dispor de **e-CPF** (pessoa física) emitido por AC credenciada à **ICP-Brasil**.  
- **Gov.br e ACOAB NÃO são aceitos** para assinar a Declaração de Veracidade (DV) no e-Software.  
- Validar assinatura em https://validar.iti.gov.br/  
- PENDENTE: inventor confirmar validade e prazo do certificado.

### 3. Titularidade e cotitularidade
- Autoria/inventor informado: **João Pedro Pereira Passos (PF)**.  
- Flag: afiliação UFT / Rede BIONORTE / UNITINS → **verificar contrato ANTES de protocolar**.  
- PENDENTE: parecer interno ou declaração sobre existência ou não de cotitularidade institucional / cessão.

### 4. Preparação do hash (NÃO anexar fonte neste dossiê)
- Manual recomenda algoritmo **SHA-512** ou mais recente.  
- Informar no formulário: **nome do algoritmo** + **texto hexadecimal** do resumo.  
- Se múltiplos arquivos: gerar **ZIP** do conjunto de fontes e hashear o ZIP.  
- [ ] Hash gerado e arquivado sob custódia do inventor.  
- PENDENTE: algoritmo efetivamente usado; valor hex; lista de arquivos incluídos no ZIP.

### 5. GRU código 730 — pagar ANTES do protocolo
- Serviço: Pedido de Registro de Programa de Computador – RPC (eletrônico / e-Software).  
- Valor de referência (Portaria INPI/PR nº 10/2025 / tabela 20_dez_25): **R$ 210,00**.  
- **Não há desconto** para serviços relativos a programa de computador (art. 2º da Portaria INPI/PR nº 10/2025 não abrange esses serviços).  
- [ ] Emitir GRU 730; [ ] pagar; [ ] guardar **«Nosso Número»**.  
- **Valor a confirmar na tabela vigente** no dia do pagamento.

### 6. Declaração de Veracidade (DV) e anexos
- Anexos obrigatórios ao e-Software: **DV** assinada digitalmente; **procuração** somente se houver procurador.  
- Sem procurador: titular assina DV com e-CPF.  
- [ ] DV baixada (disponível no fluxo GRU / sistema); [ ] assinada; [ ] validada.

### 7. Preenchimento e-Software (único meio aceito)
Protocolo **somente** via **e-Software** (não há via papel para depósito desse pedido).  
Campos modelo (rascunho — ajustar no formulário oficial):

#### 7.1 Títulos sóbrios (escolher um; variantes para teste de formulário)
1. Sistema de planejamento de rotas em layouts industriais com pré-processamento de landmarks geométricos  
2. Módulo de consultas origem-destino em grafo de layout espacial estável  
3. Software de roteamento offline-online para mapas de armazém, pátio ou planta  

#### 7.2 Linguagens
- **PENDENTE** — inventor não informou neste dossiê.  
- Exemplos a confirmar (não afirmados como fato): Python; C++; TypeScript.  
- Informar no formulário apenas o que for verdadeiro para a versão hasheada.

#### 7.3 Campo de aplicação / funcionalidades (sem revelar núcleo de seletor topológico)
- Campo sugerido: **planejamento de rotas em layouts industriais**.  
- Funcionalidades (nível de registro — expressão, não know-how secreto):  
  - ingestão/representação de mapa de layout (corredores, obstáculos, nós);  
  - pré-processamento offline de estruturas auxiliares de distância;  
  - atendimento a consultas O-D;  
  - reutilização de estruturas enquanto o mapa permanece válido;  
  - sinalização de necessidade de reprocessamento quando o layout é alterado.  
- **Não** descrever no formulário de registro o detalhe do seletor topológico, parâmetros internos de TDA, nem pseudocódigo reprodutível do diferencial confidencial.

#### 7.4 Autoria
- Autor: João Pedro Pereira Passos.  
- Demais autores/cotitulares: PENDENTE de verificação institucional.

### 8. Após pagamento confirmado
- Referência oficial: até **10 dias corridos** para expedição/disponibilização do certificado (contados conforme orientação do Guia Básico — **não é SLA contratual**).  
- Acompanhar RPI (terças) e/ou Meus Pedidos / BuscaWeb.  
- Validade do registro: da ordem de **~50 anos** (Convenção de Berna), conforme Guia Básico INPI.  
- Lembrete: o registro **protege a expressão** (hash); **não** cobre ideia, processo, API nem marca.

## Limites do Trilho A (comunicação clara)

| Cobre | Não cobre |
|-------|-----------|
| Expressão do código registrado (prova de autoria/titularidade via hash) | Ideia do algoritmo ALT/FPS |
| | Processo IIC / método de planejamento |
| | API, protocolos, marcas |
| | Segredo industrial não depositado |

## Pendências para fechar o Trilho A nesta semana
1. e-CPF ICP-Brasil válido.  
2. Decisão de titularidade (PF isolada vs cotitulares).  
3. Hash SHA-512 (ou mais recente) + hex.  
4. Pagamento GRU 730 (R$ 210,00 — a confirmar na tabela vigente).  
5. DV assinada.  
6. Preenchimento e-Software com título sóbrio e funcionalidades sem revelar seletor topológico.

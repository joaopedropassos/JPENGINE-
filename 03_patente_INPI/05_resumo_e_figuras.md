# RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO

# 05 — Resumo e figuras | ETAPA 4

## Resumo (≈ 210 palavras)

Processo implementado em computador para planejamento de caminhos em grafo obtido de layout espacial estável de ambiente industrial (armazém, pátio ou planta). Em fase offline, constrói-se um prior estrutural do grafo, selecionam-se landmarks geométricos — por exemplo mediante amostragem do tipo farthest-point sampling — e pré-computam-se tabelas de distância entre nós e landmarks. Em fase online, consultas origem–destino são atendidas por busca informada do tipo ALT, com heurística admissível baseada em desigualdades triangulares, preservando otimalidade do caminho. O prior é reutilizado em múltiplas consultas enquanto o mapa permanece válido e é invalidado quando o layout sofre alteração material, forçando novo pré-processamento. O efeito técnico candidato, observado em testes internos (versão v5: mil consultas com otimalidade integral; versão v7: vantagem geométrica quando a razão entre distância de grafo e distância de Manhattan cresce), consiste na redução de estados expandidos e/ou do tempo de consulta frente a A* com heurística fixa, sem prejuízo do ótimo. Abordagens topológicas auxiliares foram avaliadas (v6/v7) sem superioridade sobre a seleção geométrica. A matéria destina-se a aplicação industrial em roteamento repetido sobre o mesmo mapa. Este resumo é rascunho e não constitui pedido protocolado.

*(Contagem aproximada: 210 palavras.)*

## Figuras (descrição para desenho — linhas pretas; sem foto de cliente; sem logo)

### Figura 1 — Visão geral offline / online
Fluxograma em caixas: Entrada do mapa → Grafo → Seleção de landmarks geométricos → Tabelas de distância → Prior persistido → (seta) Consulta O-D → Busca informada tipo ALT → Caminho ótimo. Nota lateral: «invalidação se layout mudar».

### Figura 2 — Layout esquemático de armazém (DG ilustrativo)
Planta esquemática com corredores em «U»/«S», obstáculos retangulares, origem O e destino D. Indicar caminho de grafo vs linha Manhattan. Rótulo: «DG = d_grafo / d_Manhattan elevado».

### Figura 3 — Landmarks geométricos (FPS — esquemático)
Mesmo layout da Fig. 2 com k pontos marcados como L1…Lk espalhados; sem revelar pseudocódigo.

### Figura 4 — Uso da desigualdade triangular (ALT)
Diagrama de três pontos: nó u, destino t, landmark L; setas com distâncias pré-computadas; caixa «heurística admissível h(u)».

### Figura 5 — Comparativo qualitativo de expansão (v5/v7)
Dois painéis lado a lado: «A* heurística fixa» (nuvem de nós maior) vs «busca com prior de landmarks geométricos» (nuvem menor). Rodapé: «ilustração qualitativa — dados internos v5/v7; não é certificado INPI».

### Figura 6 — Amortização do pré-processamento (Q*)
Gráfico esquemático eixo X = número de consultas; eixo Y = custo médio por consulta; curva caindo até patamar; marcar Q* de break-even como «PENDENTE DE MEDIÇÃO em mapa-alvo».

### Figura 7 — Invalidação do prior
Diagrama de estados: Prior válido → Evento de mudança de layout → Prior inválido → Reexecução offline → Prior válido.

### Figura 8 — Integração lógica (API sem código)
Caixas: «Cliente de consulta O-D» → «Interface de serviço (sem listar endpoints secretos)» → «Motor offline/online» → «Armazenamento do prior». Proibir listagem de código.

### Figura 9 — Fronteira do que não se reivindica como essencial
Nuvem tracejada «TDA / homologia / Wasserstein / persistência» com carimbo «não essencial — ver nota v6/v7».

### Figura 10 — (Opcional) Posicionamento frente ao estado da técnica
Tabela visual simples: Dijkstra | A* | ALT | JPS | CH | Presente proposta (offline/online + landmarks geométricos + reuso/invalidação). Sem números de patente inventados na figura.

**Instruções ao desenhista:** traço preto em fundo branco; tipografia legível; sem logotipos; sem fotografias de instalações de terceiros; sem dados de cliente.

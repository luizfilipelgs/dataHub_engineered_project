# ⚙️ DataHub Engineered

**DataHub Engineered** é uma plataforma full-stack idealizada para atender às necessidades de **gestão técnica, operacional e colaborativa** em projetos de engenharia. Seu propósito é integrar em um só ambiente: dados operacionais, equipes, comunicação em tempo real, processamento de mídia e análise de desempenho — oferecendo suporte completo à tomada de decisão em ambientes complexos como indústrias, usinas, canteiros de obra e plantas de produção.

---

## 🎯 Objetivo

O sistema foi concebido como um **hub central de dados e operações técnicas**, com foco em:

- Armazenamento e visualização de **registros técnicos e operacionais**;
- Gestão de **equipes, cargos e projetos** de engenharia;
- Comunicação em tempo real entre membros da equipe;
- **Processamento de imagens e vídeos** de campo com suporte a IA;
- **Dashboards analíticos** para tomada de decisão;
- **Notificações em tempo real** com base em eventos e regras.

---

## 📦 Módulos Idealizados

| Módulo | Descrição |
|--------|-----------|
| 📋 **Registros Técnicos** | Cadastro de medições e eventos com visualização por gráficos e tabelas |
| 👥 **Gestão de Equipes** | Controle de funcionários, cargos e permissões por projeto |
| 🧱 **Projetos e Atividades** | Organização de frentes de obra, etapas, progresso e arquivos |
| 💬 **Chat em Tempo Real** | Comunicação via WebSockets e Redis |
| 🖼️ **Processamento de Imagens** | Upload e análise automática de fotos (OCR, detecção de falhas, progresso) |
| 📹 **Streaming de Vídeo com Processamento** | Monitoramento por câmeras em tempo real com IA embarcada |
| 📊 **Dashboards e Relatórios** | Indicadores de desempenho técnico e financeiro |
| 📡 **Notificações em Tempo Real** | Alertas automáticos por evento, cargo ou situação crítica |

---

## 🛠️ Tecnologias

| Camada | Stack |
|--------|-------|
| **Frontend** | React, TypeScript, React Query, Axios, MUI/ShadCN |
| **Backend** | FastAPI (Python), SQLModel, REST + GraphQL (Strawberry) |
| **Banco de Dados** | SQLite (MVP), PostgreSQL (produção), Redis (cache) |
| **Mensageria e Realtime** | WebSockets, Redis, RabbitMQ |
| **Mídia e Processamento** | OpenCV, FastAPI Worker, WebRTC/WebSocket |
| **Infraestrutura (futuro)** | Docker, CI/CD, Kubernetes, S3-like storage |

---

## 📍 Etapas de Desenvolvimento

### ✅ Etapa atual: MVP inicial (v0.1)
- [x] Estruturação do projeto frontend e backend
- [x] Cadastro e listagem de registros técnicos via REST
- [x] Visualização básica com gráfico (Chart.js)
- [x] Integração inicial com GraphQL (Strawberry + FastAPI)

### 🔜 Próximas etapas
- [ ] Filtros por tipo e data nos registros
- [ ] Sistema de usuários e autenticação
- [ ] Módulo de chat com WebSocket + Redis
- [ ] Upload de imagens e pipeline com RabbitMQ
- [ ] Integração de processamento de vídeo com OpenCV
- [ ] Dashboards interativos com dados dos registros
- [ ] Notificações por cargo, evento e regra de negócio

---

## 🧩 Arquitetura Modular

O projeto é desenvolvido com foco modular, permitindo que cada funcionalidade possa ser isolada, testada e implantada de forma independente no futuro.


# SPIKE-OC-CRIT03 - OpenCode Responsibility Mapping

Status: completed / accepted as input for CRIT-03

Decision status: evidencia tecnica solamente; no es decision final de arquitectura; no aprueba CRIT-03.

## 1. Resumen Ejecutivo

- [accepted] Este spike queda persistido como evidencia tecnica para preparar CRIT-03 Agent Responsibilities.
- [accepted] OpenCode no debe tratarse como runtime agents-only para disenar responsabilidades CAFL.
- [accepted] OpenCode ofrece varios mecanismos relevantes para asignar responsabilidades: agents, commands, SDK/server/OpenAPI, permissions, rules/AGENTS.md, skills, config y ejecucion no interactiva.
- [draft] CRIT-03 debe decidir responsabilidades y mecanismo candidato por responsabilidad: human, agent, command, SDK-server-script, rule-config o mixed.
- [draft] Los agents LLM son candidatos fuertes para razonamiento, manejo de ambiguedad, analisis funcional, diseno tecnico, asistencia de implementacion, revision y redaccion de evidencia.
- [draft] El control deterministico es mejor candidato para estado, trazabilidad, permissions, token budget, validaciones estructurales DoR/DoD, ejecucion de pruebas y limites de rework.
- [accepted] Este spike no aprueba agentes finales, commands finales, prompts, permissions, archivos runtime, contratos, gates, uso de SDK ni arquitectura OpenCode final.

## 2. Alcance Y Fuentes

### Fuentes Revisadas

- [accepted] Documentacion oficial de OpenCode: Agents, Commands, SDK, Server, Permissions, Rules, Skills, Config, CLI, Tools, Plugins y MCP servers.
- [accepted] Documentos disponibles en `project-truth/` al momento del spike.
- [superseded] `framework/agents/*.agent.md` y documentos bajo `framework/` fueron evidencia secundaria historica para este spike; CRIT-07 supersedio su uso: `framework/` fue eliminado como artefacto contaminado y no es evidencia secundaria utilizable ni input de TOM/Blueprint.

### Limites

- [accepted] El spike no modifico archivos bajo `framework/`.
- [accepted] El spike no creo agents ejecutables ni commands ejecutables.
- [accepted] El spike no implemento configuracion OpenCode, integracion SDK, contratos ni gates.
- [accepted] El spike es input para CRIT-03, no aprobacion de CRIT-03.

## 3. Capacidades OpenCode Relevantes Para CRIT-03

| Capability | Que es | Para que sirve | Para que no sirve bien | Relevancia CAFL | Riesgos |
| --- | --- | --- | --- | --- | --- |
| agents | Asistentes IA especializados con prompt, modelo, modo y permissions. Modos: `primary`, `subagent` y `all`. | Razonamiento, analisis, diseno, generacion de codigo, revision e investigacion dirigida. | Validacion deterministica, estado durable o gobierno de permisos por si solos. | Candidatos para analisis funcional, arquitectura, construccion, QA, compliance y evidencia. | Un diseno agents-only crea solapamiento, autoridad implicita, costo de tokens y fragilidad por prompts. |
| primary agents | Asistentes principales usados directamente en la sesion. Built-ins: Build y Plan. | Separar planificacion de construccion. | Garantizar control final si permissions siguen siendo aprobables. | Utiles para separar plan/build. | Plan/build no debe ser el unico mecanismo de gobierno. |
| subagents | Asistentes especializados invocados manualmente o por Task. Built-ins: General, Explore y Scout. | Investigacion paralela, exploracion read-only y consulta externa. | Autoridad final u orquestacion con estado. | Utiles para investigacion y revision enfocada. | Un subagent oculto puede seguir siendo invocado por el modelo si permissions lo permiten; el usuario puede invocar subagents directamente. |
| commands | Slash commands que envian plantillas de prompt reutilizables, con argumentos, agente/modelo opcional, referencias a archivos y salida shell. | Flujos repetibles y entradas controladas. | Control deterministico o validacion final. | Candidatos para iniciar fases como elicitacion, PRD, SDD, testing y revision de gates. | Siguen siendo prompt-driven; pueden inyectar demasiado contexto; pueden sobrescribir built-ins. |
| SDK/server/OpenAPI | Interfaz programatica HTTP/server y SDK JS/TS generado desde OpenAPI. | Automatizacion de sesiones, salida estructurada, inspeccion de estado, invocacion de commands, eventos, lectura/busqueda de archivos y respuesta a permisos. | Reemplazar juicio funcional o tecnico. | Candidato futuro para control de flujo, validacion, evidencia y reduccion de tokens. | Requiere diseno de seguridad; CRIT-07 dejo SDK/server fuera de core V1 salvo spike favorable. |
| permissions | Reglas runtime `allow`, `ask` y `deny`, globales o por agent, con patrones granulares. | Separar planificacion, edicion, bash, subagent invocation, skills y acceso externo. | Definir responsabilidades de negocio o gates por si solas. | Soporte esencial para autoridad de roles una vez CRIT-03 defina limites conceptuales. | OpenCode parte de defaults permisivos; patrones malos pueden sobrepermitir o bloquear indebidamente. |
| rules/AGENTS.md | Instrucciones de proyecto/global incluidas en contexto del modelo. | Reglas invariantes, autoridad documental y convenciones de proyecto. | Cargar toda la metodologia CAFL. | Utiles para reglas globales y source-of-truth. | Contexto global excesivo contamina sesiones y consume tokens. |
| skills | Paquetes de instrucciones reutilizables cargados on-demand por la herramienta skill. | Playbooks modulares y context routing. | Estado, permissions o validacion deterministica. | Buen candidato para guias especificas por tarea sin cargar todo por defecto. | Descripciones malas o exceso de skills degradan routing; permissions deben controlarse. |
| config | Configuracion runtime mergeada para agents, commands, permissions, modelos, compaction, sharing, instructions, plugins y MCP. | Politica runtime y defaults. | Decidir roles y responsabilidades CAFL. | CRIT-03 puede identificar config como mecanismo candidato; CRIT-07 aprobo direccion candidata y la configuracion concreta queda para Blueprint/spikes post-CRIT-07. | Precedencia y overrides pueden generar drift. |
| run/headless/non-interactive | `opencode run`, `opencode serve`, attach mode y salida JSON. | Automatizacion, scripting, ejecucion repetible y flujos tipo CI. | Flujos largos autonomos sin estado/gates explicitos. | Candidato para ejecucion futura de framework autonomo. | Auto-aprobacion peligrosa o auth debil rompe control. |
| tools/MCP/plugins | Tools built-in, herramientas MCP externas y hooks/custom tools via plugins. | Integraciones, hooks y helpers deterministas futuros. | Habilitar demasiadas herramientas por defecto. | Posible soporte futuro para RAG, validacion y protecciones. | Bloat de contexto por MCP/tools y mayor superficie de riesgo. |

## 4. Recomendacion De Mapeo De Responsabilidades

| Responsabilidad CAFL | Mecanismo candidato | Recomendacion | Por que | Riesgos | Decision necesaria en CRIT-03 |
| --- | --- | --- | --- | --- | --- |
| Coordinacion/orquestacion | mixed | Orquestacion asistida por agent mas estado/control deterministico futuro. | La coordinacion requiere razonamiento y control durable. | Orquestacion solo con agent puede confundir narrativa con estado real. | Definir autoridad para avanzar, bloquear, replanificar y escalar. |
| Analisis funcional | agent + command + human | LLM para elicitacion; commands para entrada repetible; owner solo en decisiones criticas. | La ambiguedad funcional es adecuada para interaccion LLM. | Preguntas infinitas o microgestion. | Definir profundidad, salida y condiciones de bloqueo. |
| Diseno tecnico Odoo | agent + skills + rule-config | Rol tipo arquitecto con contexto y fuentes controladas. | Requiere juicio tecnico y uso de fuentes oficiales. | Decisiones Odoo alucinadas. | Definir autoridad y suficiencia de fuentes. |
| Construccion | agent + command + permissions | Builders solo despues de PRD/SDD/task packet suficiente. | La generacion de codigo sirve con limites claros. | Scope creep y edicion prematura. | Definir granularidad de builders y autoridad de edicion. |
| Verificacion/testing | mixed | QA agent para plan/diagnostico/reporte; commands/scripts deterministas para evidencia de ejecucion. | Las pruebas deben ejecutarse, no solo describirse. | Falsa confianza si no se ejecutan tests. | Definir autoridad QA para rechazar o enviar a rework. |
| Seguridad/riesgo/compliance | agent + human + rule-config | Revision especializada con escalamiento humano para riesgo legal/compliance critico. | CRIT-01/CRIT-02 hacen compliance central. | Falsa seguridad legal o bloqueos excesivos. | Definir alcance y autoridad de escalamiento. |
| Evidencia/cierre | mixed | LLM puede redactar evidencia; checks deterministas deben validar existencia/consistencia en Blueprint/spikes post-CRIT-07. | El cierre debe ser auditable. | Evidencia narrativa sin trazabilidad. | Definir quien propone, valida y acepta cierre. |
| Context routing | rule-config + SDK-server-script + agent | Separar de la ejecucion; LLM puede recomendar, control futuro puede hacer cumplir. | CRIT-02 prohibe leer todo el repo por defecto. | Contaminacion de contexto y bloat de tokens. | Definir dueno y autoridad de routing. |
| Token budget | rule-config + SDK-server-script + command | Tratar como regla operativa, no preferencia del agent. | Los agents tienden a leer de mas sin limites. | Costo, latencia y contexto irrelevante. | Definir quien fija y quien puede exceder budget. |
| Task/context packet generation | mixed | Agent puede generar; receptor o capa de control valida readiness. | El packet requiere juicio y estructura. | Packets genericos crean falsa readiness. | Definir productor, consumidor y autoridad de rechazo. |
| DoR validation | mixed | Receptor valida suficiencia conceptual; checks futuros validan campos. | Evita iniciar con contexto insuficiente. | Autoaprobacion por ejecutor. | Definir quien declara Ready. |
| DoD validation | mixed + human | QA/evidencia/orquestacion validan; owner o gate definido acepta cierre critico final. | CRIT-01 exige modulos testeados, documentados y auditables. | Cierre prematuro. | Definir niveles de cierre. |
| Rework control | mixed | Orquestacion cuenta intentos y escalation; agents ejecutan rework acotado. | CRIT-02 prohibe tareas interminables. | Loops infinitos y scope change oculto. | Definir limites de rework. |
| Escalation to owner | human + agent + rule-config | Agents detectan; politica decide; owner resuelve items criticos. | Balancea autonomia y control. | Escalar demasiado o muy poco. | Definir categorias de escalamiento. |

## 5. Recomendacion Preliminar

### Conviene Que CAFL Sea Agents-Only?

- [draft] No. CAFL no deberia disenar sus responsabilidades como agents-only.
- [draft] Los agents sirven para razonamiento y generacion, pero no bastan para estado, permissions, evidencia, validacion deterministica, token budget, ejecucion de tests ni control de rework.

### Conviene Combinar Agents, Commands Y SDK/Server/Scripts?

- [draft] Si. Un mixed responsibility model es el candidato mas robusto.
- [draft] CRIT-03 debe decidir responsabilidades y mecanismos candidatos a nivel conceptual.
- [accepted] CRIT-07 aprobo direccion candidata de runtime y viabilidad; setup runtime concreto, configuracion OpenCode, SDK/server/scripts si aplican y permissions quedan para Blueprint/spikes post-CRIT-07.

### Mejor Ajuste Para LLM Reasoning

- [draft] Elicitacion y analisis funcional.
- [draft] Analisis de alcance y deteccion de ambiguedades.
- [draft] Diseno tecnico y trade-offs.
- [draft] Generacion de codigo bajo task/context packet.
- [draft] Revision y diagnostico de fallas.
- [draft] Redaccion de evidencia y resumen de riesgos.

### Mejor Ajuste Para Control Deterministico

- [draft] Estado y trazabilidad.
- [draft] Enforcement de token budget.
- [draft] Enforcement de context routing.
- [draft] Validacion estructural DoR/DoD.
- [draft] Ejecucion de tests y captura de evidencia.
- [draft] Permission boundaries.
- [draft] Contadores de rework y triggers de escalamiento.

### Decisiones Para CRIT-03

- [open-question] Cual es el conjunto minimo de roles/capacidades?
- [open-question] Que responsabilidades se mapean a human, agent, command, SDK-server-script, rule-config o mixed?
- [open-question] Que autoridad tiene cada rol para avanzar, bloquear, pedir contexto, replanificar, escalar o cerrar?
- [open-question] Que responsabilidades no deben resolverse con agents?
- [superseded] Los limites de implementacion tecnica fueron tratados por CRIT-07; la materializacion concreta queda para TOM/Blueprint/spikes post-CRIT-07.

### Queda Para CRIT-07

- [accepted] Configuracion runtime OpenCode final.
- [accepted] Permissions finales y politica de aprobaciones automaticas.
- [accepted] Decisiones de implementacion SDK/server/scripts.
- [accepted] Nombres de archivos runtime y modelo de instalacion.
- [accepted] Spikes OpenCode que requieren ejecucion.
- [accepted] Entorno Odoo y verificacion ejecutable.

## 6. Riesgos Identificados Por El Spike

- [draft] Asumir agents-only puede forzar todas las responsabilidades a prompt design y crear solapamiento, bloat de tokens y control debil.
- [draft] Usar prompts como unico mecanismo de control puede generar gobierno falso sin permissions, estado o validacion verificable.
- [draft] No separar LLM reasoning de control deterministico puede producir falsa autonomia y cierre no reproducible.
- [draft] Asignar context routing y token budget solo a agents puede producir contexto excesivo, costo y contaminacion por evidencia secundaria.
- [draft] Tratar commands como automatizacion final puede ocultar que siguen siendo plantillas de prompt si no se combinan con checks deterministas.
- [draft] Tratar SDK/server como arquitectura final en CRIT-03 invadiria CRIT-07.

## 7. Inputs De Elicitacion Para CRIT-03

| Area de decision | Pregunta al owner | Opciones | Recomendacion preliminar | Trade-off | Decision requerida |
| --- | --- | --- | --- | --- | --- |
| Modelo de responsabilidad | CAFL debe ser agents-only o mixed? | agents-only; agents + commands; mixed con control deterministico; human-led | Mixed | Mas piezas, mas control | Decidir si mecanismos no-agent pueden ser candidatos de responsabilidad. |
| Granularidad de roles | Que roles/capacidades minimas se necesitan? | 8 agents draft actuales; roles consolidados; capacidades dinamicas | Capacidades consolidadas con especialistas opcionales | Menos agents reducen overhead; muy pocos crean ambiguedad | Aprobar lista minima de roles/capacidades. |
| Orquestacion | Quien controla alcance, estado, riesgo y avance de fase? | human; orchestrator agent; estado deterministico; mixed | Mixed | Mas gobierno, menos falsa autonomia | Definir autoridad conceptual. |
| Division de desarrollo | Como dividir construccion Odoo? | builder unico; backend/frontend; especialistas por artefacto | Backend mas frontend condicional para V1 | Coordinacion mas simple, menor especializacion | Definir granularidad inicial y criterio de division. |
| Seguridad/compliance | Compliance es rol separado o check transversal? | separado; checklist QA; arquitecto; mixed | Mixed con escalamiento | Evita dilucion, agrega revision | Definir autoridad de blocker y escalamiento. |
| Context routing | Quien selecciona contexto aplicable? | ejecutor; orquestador; script futuro; mixed | Separado del ejecutor | Mas handoff, menos contaminacion | Definir dueno de routing. |
| Token budget | Token budget es sugerencia o regla exigible? | ninguno; sugerido; regla por fase; automatizado futuro | Regla obligatoria por fase/tarea | Puede limitar exploracion | Definir autoridad de budget. |
| Commands | Que deben hacer los commands? | nada; prompts libres; entradas de fase; solo tests | Entradas repetibles de fase | Estandarizacion sin control final | Definir responsabilidades candidatas sin crear commands. |
| SDK/server/scripts | Son mecanismos candidatos validos? | no; solo CRIT-07; capa de control candidata | Candidato para control deterministico futuro | Puede sobreingenierizar si se adopta temprano | Permitir como mecanismo candidato y diferir implementacion a CRIT-07. |
| Escalamiento | Que siempre escala al owner? | todo; solo final; categorias criticas | Categorias criticas de CRIT-01/CRIT-02 | Menos microgestion, requiere criterios claros | Definir categorias por rol. |

## 8. Estado De Evidencia

- [accepted] Persistido como evidencia tecnica para CRIT-03.
- [accepted] Debe revisarse durante CRIT-03.
- [accepted] No aprueba CRIT-03.
- [accepted] No aprueba agentes finales, commands finales, prompts, permissions, scripts, contratos, gates ni arquitectura OpenCode final.

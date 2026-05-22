# Critical Map

Status: draft

## Regla De Uso

- [accepted] Este mapa organiza sesiones criticas de elicitacion antes de implementar.
- [accepted] Ningun punto critico produce contratos finales, gates finales, comandos ejecutables o agentes ejecutables por si solo.
- [draft] Si un tema aparece como critico pero es subpunto de otro, se clasifica dentro del punto que decide su autoridad y consecuencias.

## Clasificacion De Subpuntos

- [accepted] OpenCode ya esta aceptado como runtime principal por CRIT-01; CRIT-07 solo debe definir restricciones de entorno de desarrollo y setup operativo del runtime.
- [accepted] OpenSpec y OpenProject no son dependencias funcionales del producto CAFL; si se evaluan, sera como herramientas auxiliares fuera del producto.
- [draft] Instalacion local/global, permisos y herramientas auxiliares pertenecen a CRIT-07.
- [draft] Aprobaciones automaticas pertenecen a CRIT-02 si afectan flujo operativo y a CRIT-05 si dependen de gates.
- [draft] Granularidad de agentes pertenece a CRIT-03, no a implementacion.
- [draft] Formato de contratos pertenece a CRIT-04, no a tooling.
- [draft] Evidencia, fuentes y trazabilidad pertenecen a CRIT-06, aunque alimenten gates y contratos.

## CRIT-01: Intent And Scope

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Reconstruir la intencion real del owner y delimitar el alcance minimo antes de cualquier implementacion. |
| Why it is critical | [accepted] Sin intencion y alcance claros, el repo puede seguir expandiendo una interpretacion incorrecta. |
| What was answered | [accepted] CAFL es un framework/plataforma operativo sobre OpenCode para soluciones empresariales Odoo; usuario inicial owner; Odoo unico dominio; autonomia completa con control humano en decisiones criticas; V1 end-to-end con modulo real y acotado; testing/documentacion/evidencia obligatorios; despliegue productivo fuera de alcance inicial. |
| What must NOT be decided yet | [accepted] Arquitectura interna detallada, flujo operativo final, lista final de agentes, contratos finales, gates finales, modelo de trazabilidad detallado y backlog de implementacion. |
| Inputs reviewed | [accepted] Respuestas y aclaraciones CRIT-01 del owner como fuente primaria; `project-truth/` como bootstrap; repo previo solo como evidencia secundaria. |
| Expected outputs | [accepted] Declaracion de intencion, decisiones aceptadas/rechazadas, pendientes derivados, riesgos y glosario actualizados. |
| Acceptance criteria | [accepted] Verificacion independiente CRIT-01: APPROVED; CRIT-01 queda approved para intencion y alcance del producto. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-01; CRIT-03 a CRIT-07 siguen sin resolverse. |
| Dependencies | [accepted] CRIT-01 alimenta CRIT-02, CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07, pero no los resuelve. |

## CRIT-02: Operating Flow

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir el flujo operativo desde idea del owner hasta modulo Odoo listo para produccion tecnica, sin asumir el pipeline actual. |
| Why it is critical | [accepted] El flujo determina que artefactos, roles funcionales, decisiones humanas, gates y evidencias seran necesarios en sesiones posteriores. |
| What was answered | [accepted] CAFL usara flujo hibrido controlado; jerarquia modulo -> capability/feature -> tarea verificable; PRD y SDD ligeros obligatorios; task/context packet y DoR obligatorios; context routing y token budget; bloqueo selectivo por contexto critico; funciones minimas; shift-left verification; risk-based testing; rework acotado; cierre verificable; OpenCode spikes derivados a CRIT-07. |
| What must NOT be decided yet | [accepted] Agentes finales, contratos finales, gates finales, trazabilidad final, arquitectura OpenCode, planificacion detallada, comandos ejecutables, CI/CD final y formatos finales. |
| Inputs reviewed | [accepted] CRIT-01 approved, `project-truth/` y respuesta del owner a CRIT-02 como fuente primaria; repo previo solo como evidencia secundaria. |
| Expected outputs | [accepted] Mapa operativo aprobado, con decisiones de flujo y derivaciones explicitas a CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |
| Acceptance criteria | [accepted] Cada fase/tarea debe tener salida esperada, evidencia minima, criterios de aceptacion, condicion de bloqueo, rework acotado y cierre verificable. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-02; implementacion concreta queda derivada a CRIT-03 a CRIT-07. |
| Dependencies | [accepted] Depende de CRIT-01 approved y alimenta CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |

## CRIT-03: Agent Responsibilities

Status: draft

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir responsabilidades, limites y autoridad de agentes antes de crear o modificar agentes. |
| Why it is critical | [draft] Agentes ambiguos generan duplicacion, brechas, decisiones opacas y handoffs debiles. |
| What must be decided | [open-question] Lista de roles necesarios, granularidad, autoridad, entradas, salidas, no-responsabilidades y escalamiento. |
| What must NOT be decided yet | [draft] Prompt final, formato runtime, permisos tecnicos finales y nombres exactos de archivos. |
| Inputs to review | [draft] `framework/AGENT_CONTRACTS.md`, `framework/agents/*.agent.md`, `BACKLOG.md`, `RISKS.md`. |
| Expected outputs | [draft] Matriz candidata de agentes o roles, con limites y dudas abiertas. |
| Acceptance criteria | [draft] Cada rol candidato tiene razon de existir, no-responsabilidades y handoff principal. |
| Open questions | [open-question] Deben existir agentes especialistas por area Odoo o agentes generalistas con checklists? |
| Dependencies | [draft] Depende de CRIT-01 y CRIT-02; alimenta CRIT-04, CRIT-05 y CRIT-07. |

## CRIT-04: Contracts

Status: draft

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir que contratos son necesarios para coordinar fases, agentes y entregables. |
| Why it is critical | [draft] Contratos incompletos permiten avanzar con entradas ambiguas y salidas no verificables. |
| What must be decided | [open-question] Tipos de contratos, nivel de detalle, campos minimos, formato, versionado y relacion con trazabilidad. |
| What must NOT be decided yet | [draft] Contenido final de cada contrato, schemas definitivos y tooling de validacion. |
| Inputs to review | [draft] `framework/CONTRACT_CATALOG.md`, plantillas en `framework/templates/contracts/`, `framework/PRE_PLANNING_ELICITATION.md`. |
| Expected outputs | [draft] Inventario de contratos candidatos y reglas para decidir cuales son obligatorios. |
| Acceptance criteria | [draft] Cada contrato candidato tiene proposito, consumidor, productor, entrada, salida y criterio de suficiencia. |
| Open questions | [open-question] Que contrato minimo evita perder control sin crear burocracia excesiva? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02 y CRIT-03; alimenta CRIT-05 y CRIT-06. |

## CRIT-05: Gates And Verification

Status: draft

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir como se decide avanzar, bloquear, replanificar o escalar. |
| Why it is critical | [draft] Gates debiles o no verificables crean confianza falsa y no controlan riesgo. |
| What must be decided | [open-question] Gates minimos, severidades, evidencias, criterios verificables, acciones por fallo y responsabilidad de decision. |
| What must NOT be decided yet | [draft] Implementacion automatizada, scripts CI finales, comandos locales y cobertura tecnica exhaustiva. |
| Inputs to review | [draft] `framework/GATE_CATALOG.md`, `framework/ci/contract/PIPELINE_CONTRACT.md`, `RISKS.md`, `PROJECT_CONTROL.md`. |
| Expected outputs | [draft] Mapa de gates candidatos con evidencias requeridas y consecuencias operativas. |
| Acceptance criteria | [draft] Cada gate candidato puede responder que verifica, con que evidencia, quien decide y que pasa si falla. |
| Open questions | [open-question] Que fallas bloquean siempre y cuales pueden registrarse como deuda aceptada? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02, CRIT-04 y CRIT-06; alimenta CRIT-07. |

## CRIT-06: State, Evidence And Traceability

Status: draft

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir como se conserva estado, evidencia, decisiones y trazabilidad sin depender de memoria o conversaciones externas. |
| Why it is critical | [draft] Sin trazabilidad se pierden causas de decisiones, fuentes, riesgos, aprobaciones y cambios. |
| What must be decided | [open-question] Ubicacion del estado, IDs, fuentes, evidencia minima, matriz de trazabilidad, decision log y politica de cambios. |
| What must NOT be decided yet | [draft] Herramientas finales de almacenamiento, schemas definitivos, automatizacion RAG o dashboards. |
| Inputs to review | [draft] `DECISIONS.md`, `ELICITATION_RECORD.md`, `PROJECT_CONTROL.md`, templates de trazabilidad, RAG y CI. |
| Expected outputs | [draft] Modelo minimo de estado y evidencia con reglas de actualizacion y auditoria. |
| Acceptance criteria | [draft] Una decision puede rastrearse a fuente, fecha, estado, impacto, riesgos y artefactos afectados. |
| Open questions | [open-question] Que evidencia es obligatoria para aceptar una decision o entrega? |
| Dependencies | [draft] Depende de CRIT-01 y CRIT-02; alimenta CRIT-04, CRIT-05 y CRIT-07. |

## CRIT-07: Implementation Risks And Resources

Status: draft

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Validar recursos, restricciones, herramientas y riesgos antes de comprometer implementacion. |
| Why it is critical | [draft] Integrar herramientas o prometer automatizacion sin recursos disponibles puede consumir la V1 sin validar valor. |
| What must be decided | [open-question] Entorno Odoo, restricciones de entorno de desarrollo, setup operativo del runtime OpenCode, herramientas auxiliares fuera del producto si aportan valor, RAG, CI/CD, Playwright, permisos, datos, esfuerzo, secuencia, recortes de alcance y modulo piloto exacto. |
| What must NOT be decided yet | [draft] Codigo, instaladores finales, configuracion activa, infraestructura productiva y optimizaciones. |
| Inputs to review | [draft] `framework/INSTALLATION_MODEL.md`, `framework/rag/`, `framework/ci/`, `framework/examples/`, `RISKS.md`. |
| Expected outputs | [draft] Mapa de recursos, restricciones, riesgos bloqueantes y secuencia candidata de implementacion. |
| Acceptance criteria | [draft] Cada herramienta candidata tiene justificacion, prerequisito, costo, riesgo y decision de incluir/excluir/postergar. |
| Open questions | [open-question] Que recursos, restricciones y herramientas auxiliares son necesarios para construir V1 en 2 meses sin convertirlas en dependencias funcionales del producto CAFL? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02, CRIT-05 y CRIT-06; desbloquea planificacion tecnica. |

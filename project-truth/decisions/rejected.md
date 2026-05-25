# Rejected Decisions

Status: bootstrap + CRIT-03 approved

| ID | Rejected decision | Source | Truth status | Notes |
| --- | --- | --- | --- | --- |
| DEC-REJECTED-001 | Tratar el repo actual como verdad oficial del proyecto. | Prompt del owner | rejected | El owner indico explicitamente que el repo actual puede no reflejar su intencion real. |
| DEC-REJECTED-002 | Definir CAFL como framework generico multi-stack o plataforma general para desarrollar en cualquier tecnologia. | CRIT-01 owner | rejected | Rechazo de alcance/producto: CAFL queda especializado en Odoo. |
| DEC-REJECTED-003 | Incluir despliegue real en servidor productivo como alcance inicial de CAFL. | CRIT-01 owner | rejected | Rechazo de alcance inicial: `listo para produccion` significa readiness tecnica y funcional, no deployment real. |
| DEC-REJECTED-004 | Incluir gestion de proyectos en plataformas externas tipo Scrum Master o PMBOK como componente inicial del producto CAFL. | CRIT-01 owner | rejected | Rechazo de alcance/producto: no impide usar herramientas auxiliares fuera del producto si se decide despues. |
| DEC-REJECTED-005 | Tratar OpenSpec u OpenProject como dependencias funcionales u obligatorias del producto CAFL. | CRIT-01 owner | rejected | Rechazo de alcance/producto: no rechaza su uso auxiliar para desarrollar o coordinar el proyecto fuera del producto. |
| DEC-REJECTED-006 | Considerar completa una solucion solo porque genero codigo. | CRIT-01 owner | rejected | Rechazo de comportamiento del producto: debe existir testing, documentacion, evidencia, trazabilidad, revision proporcional y aceptacion. |
| DEC-REJECTED-007 | Permitir que CAFL invente o implemente cuando falte contexto suficiente. | CRIT-01 owner | rejected | Rechazo de comportamiento del producto: debe bloquear, explicar lo faltante, preguntar y continuar solo con informacion suficiente o decision explicita. |
| DEC-REJECTED-008 | Imponer Test-Driven Development estricto como obligacion universal para toda tarea. | CRIT-02 owner | rejected | TDD queda aceptado como capacidad ligera de diseno, validacion y planificacion de pruebas; obligatoriedad estricta se evalua por tipo de tarea, riesgo y valor real. |
| DEC-REJECTED-009 | Leer todo el repo por defecto para cada fase o tarea. | CRIT-02 owner | rejected | CRIT-02 aprobo context routing, token budget y task/context packet para minimizar contexto y evitar contradicciones. |
| DEC-REJECTED-010 | Cerrar tareas o fases solo por opinion del ejecutor. | CRIT-02 owner | rejected | CRIT-02 exige salida esperada, evidencia minima, criterios de aceptacion y cierre verificable. |
| DEC-REJECTED-011 | Disenar CAFL como modelo agents-only. | CRIT-03 owner | rejected | CRIT-03 aprobo modelo mixto con agents, commands, control deterministico futuro, rules/config/skills y owner para decisiones criticas. |
| DEC-REJECTED-012 | Asumir que cada capacidad minima de CRIT-03 debe ser un agente ejecutable separado. | CRIT-03 owner | rejected | CRIT-03 aprobo capacidades consolidadas y mecanismo candidato por responsabilidad. |
| DEC-REJECTED-013 | Usar prompts LLM como unico mecanismo de control operativo, estado, gates, evidencia, testing, permisos o rework. | CRIT-03 owner | rejected | CRIT-03 separo LLM reasoning de control deterministico candidato; implementacion queda para CRIT-07. |
| DEC-REJECTED-014 | Crear especialistas permanentes por cada artefacto Odoo desde el inicio. | CRIT-03 owner | rejected | CRIT-03 aprobo backend base, frontend/OWL condicional y especialistas por artefacto solo por SDD, riesgo o complejidad. |
| DEC-REJECTED-015 | Fusionar o absorber compliance de forma prematura hasta diluirlo dentro de QA generico o seguridad tecnica. | CRIT-03 owner | rejected | CRIT-03 preservo seguridad/riesgo/compliance como responsabilidad explicita y `odoo-legal-risk-reviewer` queda analyze later / maybe merge as capability. |
| DEC-REJECTED-016 | Aprobar RAG completo como parte de V1 sin justificacion posterior. | CRIT-03 owner | rejected | CRIT-03 aclaro que RAG completo no queda aprobado para V1 salvo justificacion en CRIT-07. |

# CRIT-02: Operating Flow

Status: approved

## Session Objective

- [accepted] Definir el flujo operativo minimo desde una idea del owner hasta un modulo Odoo listo para produccion tecnica.
- [accepted] CRIT-02 decide operating flow, no implementacion ni formatos finales.
- [accepted] CRIT-02 no define agentes finales, contratos finales, gates finales, trazabilidad final, arquitectura OpenCode ni planificacion detallada.

## Source And Authority

- [accepted] Fuente primaria: respuesta del owner a la sesion CRIT-02 Operating Flow Technical Elicitation.
- [accepted] CRIT-01 sigue siendo autoridad para intencion, alcance, dominio Odoo, autonomia, testing, documentacion, evidencia y no-alcance de despliegue productivo.
- [accepted] El flujo operativo actual del repo sigue siendo evidencia secundaria y no queda aprobado por esta sesion.
- [accepted] Las decisiones aceptadas aqui deben implementarse o detallarse solo en las sesiones criticas correspondientes: CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07.

## Approved Operating Flow

- [accepted] CAFL operara con un flujo hibrido controlado: fases minimas obligatorias, iteraciones acotadas, avance por evidencia y retrabajo controlado.
- [accepted] El flujo debe transformar una idea breve del owner en PRD minimo suficiente antes de diseno tecnico.
- [accepted] Antes de escribir codigo debe existir SDD ligero obligatorio, ampliado solo por riesgo, complejidad o impacto arquitectonico.
- [accepted] El flujo conceptual minimo es: idea/entrada -> elicitacion -> PRD ligero -> SDD ligero -> planificacion de capabilities/tareas -> construccion -> verificacion/testing -> documentacion/evidencia -> cierre tecnico.
- [accepted] Este flujo conceptual no aprueba contratos finales, gates finales, comandos ejecutables ni agentes finales.

## Approved Decisions

### DEC-CRIT02-01: Forma del flujo end-to-end

- [accepted] CAFL usara flujo hibrido controlado.
- [accepted] Deben existir fases minimas obligatorias, iteraciones acotadas, avance por evidencia y retrabajo controlado.

### DEC-CRIT02-02: Unidad de control del trabajo

- [accepted] La unidad de control sera jerarquica: modulo -> capability/feature -> tarea tecnica verificable.
- [accepted] La jerarquia debe permitir trazabilidad desde idea hasta codigo, pruebas, documentacion y evidencia.

### DEC-CRIT02-03: Entrada inicial y PRD

- [accepted] CAFL debe aceptar una idea breve del owner y convertirla mediante elicitacion en PRD minimo antes del diseno tecnico.
- [accepted] CAFL no debe exigir requerimientos perfectos al owner antes de iniciar.
- [accepted] CAFL no debe disenar ni implementar sin PRD minimo suficiente.

### DEC-CRIT02-04: SDD y decisiones tecnicas

- [accepted] SDD ligero es obligatorio antes de escribir codigo.
- [accepted] El SDD se ampliara solo por riesgo, complejidad o impacto arquitectonico.
- [accepted] ADR minimo queda aceptado para decisiones tecnicas relevantes, sin burocracia pesada.

### DEC-CRIT02-05: Artefactos internos PRD, SDD, CDD y TDD

- [accepted] PRD y SDD son obligatorios en version ligera.
- [accepted] CDD queda aceptado como capacidad interna ligera orientada a construccion cuando aporte valor.
- [accepted] TDD queda aceptado como capacidad interna ligera de diseno, validacion y planificacion de pruebas.
- [accepted] TDD no queda aprobado como obligacion estricta de Test-Driven Development para toda tarea.
- [accepted] La obligatoriedad estricta de TDD debe evaluarse por tipo de tarea, riesgo y valor real.

### DEC-CRIT02-06: Task/context packet y Definition of Ready

- [accepted] Ninguna unidad operativa debe iniciar sin task/context packet y Definition of Ready minimo.
- [accepted] El task/context packet sera el mecanismo base para reducir tokens, evitar lectura innecesaria del repo y controlar contexto.

### DEC-CRIT02-07: Context routing, autoridad documental y token budget

- [accepted] CAFL usara context routing obligatorio por autoridad documental.
- [accepted] CAFL debe distinguir fuente autoritativa, contexto aplicable, evidencia secundaria y documento prohibido/no relevante.
- [accepted] Debe existir token budget por fase/tarea.
- [accepted] Queda prohibido leer todo el repo por defecto.

### DEC-CRIT02-08: Bloqueo por falta de contexto

- [accepted] CAFL debe bloquear cuando la falta de contexto afecte alcance, legal/compliance, seguridad, arquitectura, datos, pruebas, aceptacion o riesgo relevante.
- [accepted] CAFL no debe inventar ni implementar con contexto insuficiente.
- [accepted] CAFL tampoco debe convertir dudas menores en microgestion constante del owner.

### DEC-CRIT02-09: Interaccion minima entre roles funcionales

- [accepted] CRIT-02 define interacciones funcionales minimas sin decidir agentes finales.
- [accepted] Funciones minimas aceptadas a nivel de flujo: owner, coordinacion/orquestacion, analisis funcional, diseno tecnico, construccion, verificacion/testing, seguridad/riesgo/compliance y evidencia/cierre.
- [accepted] La funcion de seguridad/riesgo/compliance incluye compliance legal y normativo como parte central de la intencion aprobada en CRIT-01.
- [accepted] Estas funciones no significan todavia que cada funcion sea un agente separado.

### DEC-CRIT02-10: Verificacion dentro del flujo

- [accepted] CAFL usara verificacion shift-left en cada transicion importante y verificacion tecnica final antes del cierre.
- [accepted] Risk-based testing queda aprobado como principio operativo.
- [accepted] Gates finales y criterios exactos de testing quedan derivados a CRIT-05.

### DEC-CRIT02-11: Avance, retrabajo y cierre

- [accepted] CAFL solo debe avanzar si cumple salida esperada, evidencia minima y criterios de aceptacion.
- [accepted] El retrabajo debe ser acotado, trazable y con escalamiento si falla repetidamente o cambia el alcance.
- [accepted] CAFL no debe permitir tareas interminables ni cierre basado solo en opinion del ejecutor.

### DEC-CRIT02-12: Uso operativo de OpenCode y spikes necesarios

- [accepted] CRIT-02 deriva a CRIT-07 un set de spikes acotados y obligatorios sobre OpenCode.
- [accepted] Los spikes deben cubrir subagentes, comandos, contexto, permisos, aprobaciones, estado, archivos fuente vs runtime, limites de tokens y ejecucion verificable.
- [accepted] OpenCode ya queda aceptado como runtime principal; los spikes no reabren esa decision.

## Methodological Decisions

- [accepted] PRD ligero obligatorio.
- [accepted] SDD ligero obligatorio.
- [accepted] CDD como capacidad interna ligera.
- [accepted] TDD como capacidad interna ligera, no obligatoria estrictamente para todo.
- [accepted] ATDD parcial mediante criterios de aceptacion testeables.
- [accepted] ADR minimo para decisiones tecnicas significativas.
- [accepted] Definition of Ready.
- [accepted] Definition of Done como principio operativo; detalle posterior en CRIT-05 y CRIT-07.
- [accepted] Risk-based testing.
- [accepted] Shift-left validation.
- [accepted] Context engineering.
- [accepted] Task/context packet.
- [accepted] Human-in-the-loop approval solo para decisiones criticas.
- [accepted] Escalation policies.
- [accepted] Verification loops.
- [accepted] Rework loops acotados.
- [accepted] BDD formal no queda como obligacion general de V1; puede usarse en features con comportamiento complejo o cuando aporte claridad funcional.
- [rejected] Scrum/PMBOK formal como parte del producto CAFL V1.
- [rejected] OpenSpec/OpenProject como dependencia funcional del producto CAFL.

## Context Routing And Token Control

- [accepted] Cada fase/tarea debe recibir solo el contexto minimo requerido para su objetivo.
- [accepted] El task/context packet debe identificar fuente autoritativa, contexto aplicable, evidencia secundaria y documentos prohibidos/no relevantes.
- [accepted] Documentos antiguos, preliminares o contradictorios no deben usarse como verdad sin validacion explicita.
- [accepted] La lectura amplia del repo no es comportamiento normal permitido; debe justificarse por una necesidad concreta.

## Advancement, Blockage, Rework And Closure

- [accepted] Una fase/tarea avanza solo si cumple su salida esperada, evidencia minima y criterios de aceptacion.
- [accepted] Una fase/tarea bloquea si falta contexto critico, hay contradiccion relevante, riesgo legal/compliance/seguridad, cambio arquitectonico importante, cambio de alcance o falla de verificacion que no pueda resolverse localmente.
- [accepted] Una fase/tarea puede retrabajarse de forma acotada y trazable.
- [accepted] Rework repetido, scope creep o cambio de supuestos debe escalarse.
- [accepted] El cierre debe ser verificable y no puede depender solo de opinion del ejecutor.

## Downstream Derivations

- [accepted] CRIT-03 debe definir roles/agentes, responsabilidades, limites y autoridad, tomando como insumo las funciones minimas aprobadas aqui.
- [accepted] CRIT-04 debe definir contratos internos, task/context packet, formatos, campos, versionado y criterios de suficiencia.
- [accepted] CRIT-05 debe definir gates, severidades, DoD verificable, evidencia y testing, tomando como insumo shift-left validation y risk-based testing.
- [accepted] CRIT-06 debe definir estado, fuentes, evidencia y trazabilidad, tomando como insumo context routing, token budget y jerarquia modulo -> capability/feature -> tarea.
- [accepted] CRIT-07 debe definir viabilidad, entorno Odoo, runtime OpenCode, spikes, recursos, secuencia y plan de 2 meses.

## Non-Goals For This Session

- [accepted] No disenar agentes finales.
- [accepted] No disenar contratos finales.
- [accepted] No disenar gates finales.
- [accepted] No disenar trazabilidad final.
- [accepted] No disenar implementacion OpenCode final.
- [accepted] No crear comandos ejecutables.
- [accepted] No configurar OpenSpec.
- [accepted] No modificar `framework/`.
- [accepted] No asumir que el repo actual es correcto.

## Acceptance Criteria Status

- [accepted] CRIT-02 queda documentado como flujo operativo aprobado.
- [accepted] CAFL operara con flujo hibrido controlado.
- [accepted] Queda aprobada la jerarquia modulo -> capability/feature -> tarea verificable.
- [accepted] PRD y SDD ligeros quedan obligatorios.
- [accepted] Task/context packet y DoR quedan obligatorios.
- [accepted] Context routing y token budget quedan como principios obligatorios.
- [accepted] Queda aprobado bloqueo selectivo por falta de contexto critico.
- [accepted] Quedan registradas funciones minimas, incluyendo seguridad/riesgo/compliance.
- [accepted] Shift-left verification y risk-based testing quedan como principios de flujo.
- [accepted] Rework acotado y cierre verificable quedan aprobados.
- [accepted] OpenCode spikes quedan derivados a CRIT-07.
- [accepted] CRIT-02 no aprueba todavia CRIT-03, CRIT-04, CRIT-05, CRIT-06 ni CRIT-07.

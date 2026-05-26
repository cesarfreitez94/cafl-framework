# Superseded Decisions

Status: CRIT-07 approved / superseded decisions registered

| ID | Superseded decision | Replaced by | Source | Truth status | Notes |
| --- | --- | --- | --- | --- | --- |
| DEC-SUPERSEDED-001 | [superseded] Restriccion bootstrap de no modificar `framework/` bajo ninguna condicion. | CRIT-07 aprobo eliminar `framework/` como artefacto contaminado mediante limpieza separada, sin convertirlo en fuente de diseno. | Bootstrap inicial + CRIT-07 owner approval | superseded | No autoriza recrear `framework/`; solo registra que la restriccion historica fue superada para la eliminacion aprobada. |
| DEC-SUPERSEDED-002 | [superseded] Uso de `framework/` como evidencia secundaria utilizable para preparar decisiones posteriores. | CRIT-07 descarto `framework/` como input: no es evidencia secundaria utilizable, no es input de TOM, no es input de Blueprint y no es candidato de supervivencia. | CRIT-07 owner approval | superseded | Las referencias pre-CRIT-07 a `framework/` quedan historicas. |
| DEC-SUPERSEDED-003 | [superseded] Cualquier referencia pre-CRIT-07 que permita conservar, auditar, migrar o rescatar `framework/` como base de layout, agents, commands, contracts, gates, schemas, validators, runtime o knowledge base. | Diseno greenfield desde `project-truth/` y decisiones CRIT-01..07 aprobadas; `framework/` no debe auditarse ni migrarse por defecto. | CRIT-07 owner approval | superseded | Mantiene historia minima sin duplicar `accepted.md`. |

# Risks

## R-001: V1 Demasiado Grande

Severidad: critical.

Categoria: alcance.

Descripcion: la V1 puede crecer si se intenta incluir fabrica completa, RAG, testing, CI/CD y motor legal avanzado.

Mitigacion: mantener V1 sin motor legal avanzado y validar con modulo simple.

## R-002: Agentes Auto-Descubiertos Durante Desarrollo

Severidad: major.

Categoria: tecnica.

Descripcion: si los agentes viven en `.opencode`, OpenCode puede cargarlos mientras se estan creando.

Mitigacion: mantener fuentes en `framework/` y usar instaladores para runtime.

## R-003: Ambiguedad En Responsabilidades De Agentes

Severidad: critical.

Categoria: operacion.

Descripcion: agentes con responsabilidades solapadas pueden generar handoffs debiles o trabajo duplicado.

Mitigacion: fase previa de contratos de agente y gates por fase.

## R-004: RAG Consume Mas Tiempo Que La Metodologia

Severidad: major.

Categoria: tecnica.

Descripcion: indexar repo y docs oficiales puede retrasar el pipeline base.

Mitigacion: definir RAG minimo viable con fuentes Odoo oficiales primero.

## R-005: Testing Frontend Odoo Complejo

Severidad: major.

Categoria: tecnica.

Descripcion: tours, QUnit/OWL y Playwright pueden requerir entorno Odoo estable y datos reproducibles.

Mitigacion: usar piloto simple y perfiles configurables de entorno.

## R-006: Riesgo Legal Por Autonomia

Severidad: critical.

Categoria: legal.

Descripcion: si no hay aprobaciones humanas obligatorias, el sistema podria avanzar con interpretaciones legales incorrectas.

Mitigacion: bloquear riesgo critico, contradiccion normativa o fuente insuficiente.

## R-007: CI/CD Agnostico Crece Demasiado

Severidad: major.

Categoria: alcance.

Descripcion: soportar multiples plataformas puede expandir la V1.

Mitigacion: definir contrato comun, comandos estandar y plantillas basicas.

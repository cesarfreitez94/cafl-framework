# Decisions

## D-001: Framework OpenCode

Se construira un framework para OpenCode, no una aplicacion independiente como primer objetivo.

## D-002: Fuente Fuera De `.opencode`

El framework fuente vivira en `framework/`, no en `.opencode`, para evitar que OpenCode descubra agentes, skills o comandos mientras se desarrollan.

## D-003: Instalacion Separada

Los instaladores futuros materializaran el runtime hacia `.opencode` local de un proyecto o hacia la configuracion global de OpenCode.

## D-004: Odoo Community v18

La V1 apunta a Odoo v18 Community.

## D-005: Fuentes Oficiales

La base de conocimiento debe priorizar documentacion oficial Odoo, repo oficial Odoo y fuentes normativas oficiales cuando aplique.

## D-006: RAG Con pgvector

El indice local usara PostgreSQL con pgvector.

## D-007: V1 Sin Motor Legal Avanzado

La V1 incluye estructura base de riesgo legal critico, pero no implementa el motor normativo chileno completo.

## D-008: Testing Estricto

Todos los tests aplicables deben pasar para aprobar un modulo.

## D-009: CI/CD Agnostico

La V1 debe entregar contrato de pipeline, comandos estandar y plantillas para distintas plataformas.

## D-010: Control En Markdown

El estado del proyecto se mantiene en documentos Markdown versionados.

## D-011: Espanol Tecnico

Los artefactos, agentes y reportes operaran por defecto en espanol tecnico.

## D-012: Fase Previa Obligatoria

Antes de planificar la implementacion se ejecutara meta-elicitacion para cerrar agentes, contratos, gates, responsabilidades y granularidad.

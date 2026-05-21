# RAG Ingestion Plan

## Tecnologia

- PostgreSQL.
- pgvector.
- Snapshots auditables.

## Ingesta V1

- Clonar o snapshot del repo oficial Odoo 18.
- Snapshot de documentacion oficial Odoo 18.
- Metadata de fuente, fecha, version/hash y responsable.
- Chunking y embeddings.
- Validacion de citas.

## Pendiente

- Definir modelo de embeddings.
- Definir esquema de tablas.
- Definir comandos de ingesta.
- Definir actualizacion manual/programada.

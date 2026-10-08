
## Databricks Retail Analytics Project Overview

- Developed a **retail analytics platform on Databricks** using the **Medallion Architecture** to centralize data from multiple sources.
- Integrated data from **Salesforce, PostgreSQL, and cloud storage** to create a unified analytics platform.
- Built scalable data pipelines to process **CRM, sales, inventory, and transaction data**.
- Created interactive **retail dashboards** to provide insights into customers, products, sales, and inventory.
- Implemented **Databricks Genie AI** to enable business users to perform self-service analytics using natural language.

## Key Components

| Layer | Technology | Purpose |
| --- | --- | --- |
| **Data Sources** | PostgreSQL, Salesforce, Blob Storage | Source retail data
| **Ingestion** | Lakeflow Connect, Auto Loader | Ingest batch/streaming data |
| **Transformation** | Spark, Lakeflow Declarative Pipelines | Clean and transform data |
| **Storage** | Delta Lake | Reliable and scalable data storage |
| **Medallion Layers** | Bronze, Silver, Gold | Progressive data refinement |
| **Semantic Layer** | Metric Views | Define reusable business metrics |
| **Orchestration** | Databricks Jobs | Schedule and manage pipelines |
| **Governance** | Unity Catalog | Security, governance, and access control |
| **Consumption** | Databricks Dashboards, Genie | Analytics and self-service insights |
| **AI Development** | Databricks Genie Code | AI-assisted development and productivity |


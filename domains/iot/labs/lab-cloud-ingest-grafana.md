# Lab: Cloud Ingest → TimescaleDB → Grafana

> [← Labs](./README.md) | [Cloud guide](../cloud/ingest-shadow-timeseries.md)

## Mục tiêu
Pipeline MQTT → (optional Kafka) → TimescaleDB → dashboard + offline alert.

## Minimal path (không Kafka)
Mosquitto/EMQX → small Python/Node consumer → Postgres/Timescale → Grafana.

## Schema
```sql
CREATE TABLE readings (
  device_id text,
  ts timestamptz NOT NULL,
  temp double precision,
  battery double precision,
  PRIMARY KEY (device_id, ts)
);
SELECT create_hypertable('readings', 'ts', if_not_exists => TRUE);
```

## Acceptance
- [ ] ≥1 device ghi rows liên tục
- [ ] Panel temp theo thời gian
- [ ] Alert “no data 5m”
- [ ] Alert battery < 20%

## Stretch
Thêm Kafka topic `iot.sensors` + JDBC sink như production sketch trong case study.

> **Last Updated:** August 2026

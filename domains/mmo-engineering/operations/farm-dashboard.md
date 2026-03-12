# 📈 Farm Dashboard Setup

> Grafana/Metabase stack để theo dõi 1.000+ account, proxy và doanh thu.

## 1. Datasource
- **Prometheus/Influx:** metrics real-time (heartbeat, latency, temp) từ agent.
- **Postgres/ClickHouse:** log business (revenue/account, checkpoint events).
- **Loki/ELK:** text log để drill-down khi có alert.

## 2. Grafana Panels
| Panel | Metric | Mô tả |
| --- | --- | --- |
| Account Survival | `online_accounts / total_accounts` | target > 90% |
| Checkpoint Rate | `checkpoint_events / active_accounts` | alert nếu > 5%/giờ |
| Revenue per Account | `revenue_rolling_24h / active_accounts` | feed từ BI DB |
| Proxy Health | RTT, success% theo provider | heatmap highlight provider lỗi |
| Queue Backlog | pending tasks/action per minute | đo nghẽn script |

## 3. Metabase Boards
- **Revenue vs Cost:** join ROI sheet với ops metrics.
- **Account Cohort:** hiển thị survival theo batch/reg date.
- **Alert Insights:** chart checkpoint burst theo proxy, device model.

## 4. Dashboard Hygiene
- Template dùng `variables` (farm, geo, campaign).
- Annotation từ CI/CD (deploy tool mới) + incident log.
- Auto refresh 15s cho Grafana real-time, Metabase 5 phút.

## 5. Access Control
- Viewer (ops) vs Editor (engineer).
- Log audit khi export screenshot/báo cáo.
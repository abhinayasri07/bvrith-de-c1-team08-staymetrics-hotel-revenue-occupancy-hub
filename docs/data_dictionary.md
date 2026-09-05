## 5. Silver Candidate Table Design

The Silver Candidate layer is the typed and standardized pre-DQ layer.
All candidate tables preserve the source grain and retain Bronze lineage fields.

### 5.1 silver_bookings_candidate

| Field | Data Type | Transformation / Derivation | Business Meaning |
|---|---|---|---|
| booking_id | string | TRIM | Unique booking identifier |
| property_id | string | TRIM | Hotel property identifier |
| guest_id | string | TRIM | Guest reference |
| rate_plan_id | string | TRIM | Rate plan reference |
| requested_room_type | string | TRIM | Requested room type |
| booking_date | date | CAST | Date booking was created |
| arrival_date | date | CAST | Guest arrival date |
| departure_date | date | CAST | Guest departure date |
| booking_status | string | TRIM + UPPER | Standardized booking status |
| market_segment | string | TRIM | Market segment |
| channel | string | TRIM | Booking channel |
| adults | bigint | Typed numeric field | Number of adults |
| children | bigint | Typed numeric field | Number of children |
| rooms_booked | bigint | Typed numeric field | Number of rooms booked |
| lead_time_days | bigint | Typed numeric field | Days between booking and arrival |
| nightly_rate | double | Typed numeric field | Nightly room rate |
| discount_amount | double | Typed numeric field | Discount amount |
| tax_amount | double | Typed numeric field | Tax amount |
| refund_amount | double | Typed numeric field | Refund amount |
| booked_amount | double | Typed numeric field | Original booked amount |
| net_booking_value | double | Typed numeric field | Net booking value |
| cancellation_ts | timestamp | CAST | Cancellation timestamp |
| checkin_ts | timestamp | CAST | Check-in timestamp |
| checkout_ts | timestamp | CAST | Check-out timestamp |
| ingestion_timestamp | timestamp | Retained from Bronze | Source ingestion timestamp |
| source_file_name | string | Retained from Bronze | Source file lineage |
| source_system | string | Retained from Bronze | Source system lineage |
| batch_id | string | Retained from Bronze | Batch lineage |

### 5.2 silver_guests_candidate

| Field | Data Type | Transformation | Business Meaning |
|---|---|---|---|
| guest_id | string | TRIM | Guest identifier |
| guest_segment | string | TRIM + UPPER | Standardized guest segment |
| origin_region | string | TRIM + UPPER | Standardized origin region |
| loyalty_tier | string | TRIM + UPPER | Standardized loyalty tier |
| repeat_guest_flag | boolean / integer | Typed flag | Indicates repeat guest |
| ingestion_timestamp | timestamp | Retained | Source ingestion timestamp |
| source_file_name | string | Retained | Source file lineage |
| source_system | string | Retained | Source system lineage |
| batch_id | string | Retained | Batch lineage |

### 5.3 silver_rate_plans_candidate

| Field | Data Type | Transformation | Business Meaning |
|---|---|---|---|
| rate_plan_id | string | TRIM | Rate plan identifier |
| property_id | string | TRIM | Property identifier |
| room_type | string | TRIM + UPPER | Standardized room type |
| channel | string | TRIM + UPPER | Standardized booking channel |
| effective_from | date | Typed date | Rate validity start |
| effective_to | date | Typed date | Rate validity end |
| nightly_rate | double | Typed numeric field | Nightly rate |
| meal_plan | string | TRIM + UPPER | Standardized meal plan |
| cancellation_policy | string | TRIM | Cancellation policy |
| discount_pct | double | Typed numeric field | Discount percentage |
| ingestion_timestamp | timestamp | Retained | Source ingestion timestamp |
| source_file_name | string | Retained | Source file lineage |
| source_system | string | Retained | Source system lineage |
| batch_id | string | Retained | Batch lineage |

### 5.4 silver_rooms_candidate

Room candidate records standardize property, room type, active dates, capacity and service/availability flags while preserving the original room-level grain and Bronze lineage.

### 5.5 silver_room_nights_candidate

Room-night candidate records preserve the room-night business key and one-row-per-room/date allocation. Stay dates, service/occupancy flags and recognized revenue are explicitly typed and standardized.

## 6. Week 5 Derivations

| Derivation | Description |
|---|---|
| stay_nights | Number of nights between arrival_date and departure_date |
| party_size | Adults + children |
| booking_month | Month derived from booking_date |
| stay_length_band | Categorizes stay duration into defined bands |

## 7. Reconciliation

Bronze and Silver Candidate row counts were compared after transformation.

| Table | Bronze Rows | Silver Candidate Rows |
|---|---:|---:|
| bookings | 80,000 | 80,000 |
| guests | 55,000 | 55,000 |
| rate_plans | 3,000 | 3,000 |
| room_nights | 210,000 | 210,000 |
| rooms | 1,200 | 1,200 |

No records were intentionally dropped during the Candidate transformation stage. Failed casts are retained for later Data Quality evaluation.

## 8. Lineage

Silver Candidate tables retain Bronze lineage fields including ingestion timestamp, source file name, source system and batch ID. Candidate transformation is performed before Data Quality validation and Trusted Silver promotion.

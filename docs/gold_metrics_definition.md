# StayMetrics Gold Metrics Definition

## Purpose

The Gold layer provides governed dimensions, facts, summaries and KPI formulas for
hotel revenue and occupancy analysis.

The model follows the StayMetrics grain rules:
- Booking facts are at one row per trusted booking.
- Room-night facts are at one row per trusted room-night.
- Occupancy, ADR, RevPAR and recognized room revenue use room-night grain.
- Room nights are aggregated before joining to booking-level outputs.

## Gold Dimensions

### gold_dim_property
One row per property.

Key:
- property_id

### gold_dim_room_type
One row per property and room type.

Business key:
- property_id + room_type

### gold_dim_guest_segment
One row per guest/market segment.

Key:
- guest_segment

## Gold Facts

### gold_fact_booking

Grain: one trusted booking.

Important measures and derived fields:
- booked_amount
- net_booking_value
- stay_nights
- party_size
- booking_month
- stay_length_band

### gold_fact_room_night

Grain: one trusted room-night.

Important measures:
- occupied_flag
- available_flag
- revenue_eligible_flag
- recognized_room_revenue
- out_of_service_flag

`available_for_sale_flag` is derived as available inventory excluding
out-of-service room nights.

## Daily Gold Summaries

### Daily Property Summary
Grouped by:
- property_id
- stay_date

Contains occupied room nights, available room nights,
recognized room revenue and occupancy rate.

### Daily Room-Type Summary
Grouped by:
- property_id
- room_type
- stay_date

### Daily Channel/Segment Summary
Grouped by:
- booking_date
- channel
- market_segment

### Daily Rate-Plan Summary
Grouped by:
- property_id
- rate_plan_id
- stay_date

## KPI Definitions

### Total Bookings
COUNT(DISTINCT booking_id) from gold_fact_booking.

### Occupied Room Nights
SUM(occupied_flag) from gold_fact_room_night.

### Available Room Nights
SUM of room nights where:
- available_flag = 1
- out_of_service_flag = 0

### Occupancy Rate
occupied room nights / available room nights × 100.

### Recognized Room Revenue
SUM(recognized_room_revenue) for revenue-eligible trusted room nights.

### ADR
recognized room revenue / occupied room nights.

### RevPAR
recognized room revenue / available room nights.

### Cancellation Rate
cancelled bookings / total trusted bookings × 100.

### No-show Rate
no-show bookings / trusted bookings eligible for the no-show denominator × 100.
Cancelled bookings are excluded from the denominator.

### Average Length of Stay
Average stay_nights for bookings excluding cancelled and no-show bookings.

## Zero-Denominator Handling

All ratio KPIs use safe denominator logic.

If the denominator is zero, the KPI returns 0 rather than producing
a divide-by-zero error.

## Validation

Week 7 validation includes:
- unique Gold dimension keys
- unique booking fact keys
- unique room-night fact keys
- daily summary reconciliation
- one property/date spot check
- one anchor booking spot check

The manual spot check confirmed that the Gold summary values matched the
underlying trusted Gold fact values.

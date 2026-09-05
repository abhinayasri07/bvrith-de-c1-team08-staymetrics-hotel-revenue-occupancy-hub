"""
StayMetrics Data Quality Rules
Week: 6

Reusable PySpark helper functions for StayMetrics data quality checks.

Rule IDs:
    DQ-BKG-001 - Booking integrity
    DQ-CAP-001 - Capacity / occupancy validity
    DQ-DAT-001 - Date validity
    DQ-MNY-001 - Monetary validity
    DQ-RAT-001 - Rate-plan validity
    DQ-REF-001 - Reference integrity
    DQ-RMN-001 - Room-night integrity
    DQ-STS-001 - Booking status consistency
"""


# ============================================================
# DQ-BKG-001 : Booking Integrity
# ============================================================

def required_field_rule(df, field_name):
    """
    Return records where a required field is null.
    """
    return df.filter(df[field_name].isNull())


def duplicate_key_rule(df, key_field):
    """
    Return duplicate keys and their occurrence counts.
    """
    return (
        df.groupBy(key_field)
        .count()
        .filter("count > 1")
    )


# ============================================================
# DQ-CAP-001 : Capacity / Occupancy Validity
# ============================================================

def positive_value_rule(df, field_name):
    """
    Return records where a required numeric value is
    null, zero, or negative.
    """
    return df.filter(
        df[field_name].isNull()
        | (df[field_name] <= 0)
    )


def capacity_rule(df, party_size_field, capacity_field):
    """
    Return records where party size exceeds room capacity.
    """
    return df.filter(
        df[party_size_field].isNotNull()
        & df[capacity_field].isNotNull()
        & (df[party_size_field] > df[capacity_field])
    )


# ============================================================
# DQ-DAT-001 : Date Validity
# ============================================================

def invalid_date_range_rule(df, start_field, end_field):
    """
    Return records where the start date is not before
    the end date.
    """
    return df.filter(
        df[start_field].isNotNull()
        & df[end_field].isNotNull()
        & (df[start_field] >= df[end_field])
    )


def booking_after_arrival_rule(
    df,
    booking_date_field="booking_date",
    arrival_date_field="arrival_date"
):
    """
    Return bookings where booking date occurs after arrival date.
    """
    return df.filter(
        df[booking_date_field].isNotNull()
        & df[arrival_date_field].isNotNull()
        & (df[booking_date_field] > df[arrival_date_field])
    )


def checkout_before_checkin_rule(
    df,
    checkin_field="checkin_ts",
    checkout_field="checkout_ts"
):
    """
    Return records where checkout occurs before check-in.
    """
    return df.filter(
        df[checkin_field].isNotNull()
        & df[checkout_field].isNotNull()
        & (df[checkout_field] < df[checkin_field])
    )


# ============================================================
# DQ-MNY-001 : Monetary Validity
# ============================================================

def non_negative_rule(df, field_name):
    """
    Return records where a numeric field is negative.
    """
    return df.filter(
        df[field_name].isNotNull()
        & (df[field_name] < 0)
    )


# ============================================================
# DQ-RAT-001 : Rate-Plan Validity
# ============================================================

def rate_plan_match_rule(
    bookings_df,
    rate_plans_df,
    booking_rate_plan_field="rate_plan_id",
    rate_plan_field="rate_plan_id"
):
    """
    Return bookings whose rate plan ID does not exist
    in the reference rate-plan table.
    """
    return bookings_df.join(
        rate_plans_df,
        bookings_df[booking_rate_plan_field]
        == rate_plans_df[rate_plan_field],
        "left_anti"
    )


def effective_rate_plan_rule(
    bookings_df,
    rate_plans_df,
    booking_id_field="booking_id",
    property_field="property_id",
    room_type_field="requested_room_type",
    rate_plan_field="rate_plan_id",
    booking_date_field="booking_date"
):
    """
    Return bookings that do not have a valid rate-plan match
    for property, room type, rate plan, and effective date.

    A rate plan is considered valid when:

        booking.property_id = rate_plan.property_id
        booking.requested_room_type = rate_plan.room_type
        booking.rate_plan_id = rate_plan.rate_plan_id
        booking.booking_date >= effective_from
        booking.booking_date <= effective_to

    If effective_to is NULL, the rate plan remains active.
    """

    b = bookings_df.alias("b")
    rp = rate_plans_df.alias("rp")

    valid_matches = (
        b.join(
            rp,
            (
                (b[property_field] == rp["property_id"])
                & (
                    b[room_type_field]
                    == rp["room_type"]
                )
                & (
                    b[rate_plan_field]
                    == rp[rate_plan_field]
                )
                & (
                    b[booking_date_field]
                    >= rp["effective_from"]
                )
                & (
                    rp["effective_to"].isNull()
                    | (
                        b[booking_date_field]
                        <= rp["effective_to"]
                    )
                )
            ),
            "left_semi"
        )
    )

    return b.join(
        valid_matches.select(
            booking_id_field
        ).distinct(),
        booking_id_field,
        "left_anti"
    )


# ============================================================
# DQ-REF-001 : Reference Integrity
# ============================================================

def valid_reference_rule(
    fact_df,
    reference_df,
    fact_key,
    reference_key
):
    """
    Return fact records whose reference key does not exist.
    """
    return fact_df.join(
        reference_df,
        fact_df[fact_key] == reference_df[reference_key],
        "left_anti"
    )


def composite_reference_rule(
    fact_df,
    reference_df,
    fact_property_field,
    fact_room_type_field,
    reference_property_field="property_id",
    reference_room_type_field="room_type"
):
    """
    Return fact records whose property + room type combination
    does not exist in the reference table.
    """
    return fact_df.join(
        reference_df,
        (
            (
                fact_df[fact_property_field]
                == reference_df[reference_property_field]
            )
            &
            (
                fact_df[fact_room_type_field]
                == reference_df[reference_room_type_field]
            )
        ),
        "left_anti"
    )


# ============================================================
# DQ-RMN-001 : Room-Night Integrity
# ============================================================

def room_night_required_field_rule(
    df,
    field_name
):
    """
    Return room-night records where a required field is null.
    """
    return df.filter(
        df[field_name].isNull()
    )


def room_night_duplicate_rule(
    df,
    room_night_id_field="room_night_id"
):
    """
    Return duplicate room-night IDs and their counts.
    """
    return (
        df.groupBy(room_night_id_field)
        .count()
        .filter("count > 1")
    )


def occupied_room_overlap_rule(
    df,
    room_field="room_id",
    date_field="stay_date",
    status_field="occupancy_status"
):
    """
    Return occupied room/date combinations that occur
    more than once.

    Multiple occupied records for the same room and date
    indicate an occupancy overlap.
    """
    return (
        df.filter(
            df[status_field] == "OCCUPIED"
        )
        .groupBy(
            room_field,
            date_field
        )
        .count()
        .filter("count > 1")
    )


# ============================================================
# DQ-STS-001 : Booking Status Consistency
# ============================================================

def status_timestamp_rule(
    df,
    status_field="booking_status",
    checkin_field="checkin_ts",
    checkout_field="checkout_ts"
):
    """
    Return records with inconsistent booking
    status/timestamp combinations.

    CHECKED-IN / CHECKED-OUT / CHECKED bookings
    should have a check-in timestamp.

    CHECKED-OUT bookings should also have
    a checkout timestamp.
    """
    return df.filter(
        (
            df[status_field].isin(
                "CHECKED-IN",
                "CHECKED-OUT",
                "CHECKED"
            )
            & df[checkin_field].isNull()
        )
        |
        (
            (df[status_field] == "CHECKED-OUT")
            & df[checkout_field].isNull()
        )
    )


# ============================================================
# Utility Functions
# ============================================================

def rule_result_count(df):
    """
    Return the number of records failing a rule.
    """
    return df.count()


def add_rule_metadata(
    df,
    rule_id,
    severity,
    failure_reason
):
    """
    Add standard metadata columns to a DQ result DataFrame.
    """
    from pyspark.sql import functions as F

    return (
        df.withColumn(
            "failed_rule_id",
            F.lit(rule_id)
        )
        .withColumn(
            "dq_severity",
            F.lit(severity)
        )
        .withColumn(
            "dq_failure_reason",
            F.lit(failure_reason)
        )
    )

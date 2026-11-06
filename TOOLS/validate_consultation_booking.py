"""Validation helpers for consultation booking data (standard library only)."""

from datetime import date
import re
from typing import Any


_PHONE_RE = re.compile(r"^\+?[0-9][0-9 .()-]*[0-9]$")


def validate_booking(payload: Any) -> list[str]:
    """Return validation errors for a booking payload; [] means valid.

    Required keys: customer_name, phone, service, appointment_date.
    Dates must be real calendar dates in YYYY-MM-DD form.
    Phone numbers may contain common separators and must contain 8–15 digits.
    """
    errors: list[str] = []

    if not isinstance(payload, dict):
        return ["Dữ liệu đặt lịch phải là một đối tượng."]

    name = payload.get("customer_name")
    if not isinstance(name, str) or not name.strip():
        errors.append("Tên khách hàng không được để trống.")

    phone = payload.get("phone")
    if not isinstance(phone, str):
        errors.append("Số điện thoại không đúng định dạng.")
    else:
        normalized_phone = phone.strip()
        digit_count = sum(character.isdigit() for character in normalized_phone)
        if not _PHONE_RE.fullmatch(normalized_phone) or not 8 <= digit_count <= 15:
            errors.append("Số điện thoại phải có từ 8 đến 15 chữ số và đúng định dạng.")

    service = payload.get("service")
    if not isinstance(service, str) or not service.strip():
        errors.append("Dịch vụ không được để trống.")

    appointment_date = payload.get("appointment_date")
    if not isinstance(appointment_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", appointment_date):
        errors.append("Ngày hẹn phải có định dạng YYYY-MM-DD.")
    else:
        try:
            date.fromisoformat(appointment_date)
        except ValueError:
            errors.append("Ngày hẹn không tồn tại trên lịch.")

    return errors

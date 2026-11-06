import unittest

from validate_consultation_booking import validate_booking


class ValidateBookingTests(unittest.TestCase):
    def setUp(self):
        self.valid = {
            "customer_name": "Nguyen Van A",
            "phone": "+84901234567",
            "service": "Tu van nang mui",
            "appointment_date": "2026-11-10",
        }

    def test_valid_booking(self):
        self.assertEqual(validate_booking(self.valid), [])

    def test_non_object_payload(self):
        self.assertEqual(validate_booking(None), ["Dữ liệu đặt lịch phải là một đối tượng."])

    def test_blank_customer_name(self):
        data = {**self.valid, "customer_name": "  "}
        self.assertIn("Tên khách hàng không được để trống.", validate_booking(data))

    def test_non_string_customer_name(self):
        data = {**self.valid, "customer_name": 123}
        self.assertIn("Tên khách hàng không được để trống.", validate_booking(data))

    def test_invalid_phone(self):
        data = {**self.valid, "phone": "abc123"}
        self.assertTrue(any("Số điện thoại" in error for error in validate_booking(data)))

    def test_phone_with_too_few_digits(self):
        data = {**self.valid, "phone": "1234567"}
        self.assertTrue(any("8 đến 15 chữ số" in error for error in validate_booking(data)))

    def test_phone_with_too_many_digits(self):
        data = {**self.valid, "phone": "+1234567890123456"}
        self.assertTrue(any("8 đến 15 chữ số" in error for error in validate_booking(data)))

    def test_blank_service(self):
        data = {**self.valid, "service": ""}
        self.assertIn("Dịch vụ không được để trống.", validate_booking(data))

    def test_invalid_date_format(self):
        data = {**self.valid, "appointment_date": "10/11/2026"}
        self.assertIn("Ngày hẹn phải có định dạng YYYY-MM-DD.", validate_booking(data))

    def test_impossible_calendar_date(self):
        data = {**self.valid, "appointment_date": "2026-02-30"}
        self.assertIn("Ngày hẹn không tồn tại trên lịch.", validate_booking(data))

    def test_multiple_errors_are_returned(self):
        data = {"customer_name": "", "phone": "x", "service": " ", "appointment_date": "bad"}
        self.assertEqual(len(validate_booking(data)), 4)

    def test_missing_fields_are_reported(self):
        self.assertEqual(len(validate_booking({})), 4)


if __name__ == "__main__":
    unittest.main()

from colmi_r02_client.hr_settings import parse_heart_rate_log_settings, HeartRateLogSettings


def test_parse():
    resp = bytearray(b"\x16\x01\x01<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00T")
    expected = HeartRateLogSettings(enabled=True, interval=60)

    result = parse_heart_rate_log_settings(resp)

    assert result == expected

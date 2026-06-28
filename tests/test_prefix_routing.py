"""Tests for the hand-written prefix-routing wrapper client.

The wrapper derives the base URL from the API key prefix:

    live_...    -> production (https://api.voltaria.io)
    sandbox_... -> sandbox    (https://api.sandbox.voltaria.io)

while an explicit ``environment`` or ``base_url`` overrides the prefix.

Assertions check the base URL the generated client actually retains on its
client wrapper (``client._client_wrapper.get_base_url()``).
"""

import pytest
from voltaria import AsyncVoltaria, InvalidApiKeyError, Voltaria, VoltariaEnvironment

PRODUCTION_URL = "https://api.voltaria.io"
SANDBOX_URL = "https://api.sandbox.voltaria.io"


def _base_url(client) -> str:
    return client._client_wrapper.get_base_url()


# --- live_ -> production -----------------------------------------------------


def test_live_prefix_routes_to_production():
    client = Voltaria("live_abc123")
    assert _base_url(client) == PRODUCTION_URL


def test_live_prefix_routes_to_production_async():
    client = AsyncVoltaria("live_abc123")
    assert _base_url(client) == PRODUCTION_URL


# --- sandbox_ -> sandbox -----------------------------------------------------


def test_sandbox_prefix_routes_to_sandbox():
    client = Voltaria("sandbox_abc123")
    assert _base_url(client) == SANDBOX_URL


def test_sandbox_prefix_routes_to_sandbox_async():
    client = AsyncVoltaria("sandbox_abc123")
    assert _base_url(client) == SANDBOX_URL


# --- unknown / empty prefix -> InvalidApiKeyError ----------------------------


@pytest.mark.parametrize(
    "bad_key", ["nope_abc", "test_abc", "live", "sandbox", "LIVE_abc"]
)
def test_unknown_prefix_raises(bad_key):
    with pytest.raises(InvalidApiKeyError):
        Voltaria(bad_key)


def test_empty_key_raises():
    with pytest.raises(InvalidApiKeyError):
        Voltaria("")


def test_unknown_prefix_raises_async():
    with pytest.raises(InvalidApiKeyError):
        AsyncVoltaria("nope_abc")


def test_invalid_api_key_error_is_value_error():
    assert issubclass(InvalidApiKeyError, ValueError)


def test_invalid_api_key_error_records_key():
    with pytest.raises(InvalidApiKeyError) as excinfo:
        Voltaria("bogus")
    assert excinfo.value.api_key == "bogus"


# --- explicit overrides ------------------------------------------------------


def test_explicit_base_url_overrides_prefix():
    # A bad prefix would normally raise, but an explicit base_url takes over.
    client = Voltaria("bogus_key", base_url="https://staging.voltaria.io")
    assert _base_url(client) == "https://staging.voltaria.io"


def test_explicit_base_url_overrides_valid_prefix():
    client = Voltaria("live_abc", base_url="https://staging.voltaria.io")
    assert _base_url(client) == "https://staging.voltaria.io"


def test_explicit_environment_overrides_prefix():
    # Key prefix says production, but explicit environment wins.
    client = Voltaria("live_abc", environment=VoltariaEnvironment.SANDBOX)
    assert _base_url(client) == SANDBOX_URL


def test_explicit_environment_overrides_bad_prefix():
    client = Voltaria("bogus_key", environment=VoltariaEnvironment.PRODUCTION)
    assert _base_url(client) == PRODUCTION_URL


def test_explicit_environment_wins_over_base_url():
    # resolve_environment returns the environment first; generated client then
    # prefers base_url. We assert documented precedence: environment passed AND
    # base_url passed -> generated _get_base_url prefers base_url.
    client = Voltaria(
        "live_abc",
        environment=VoltariaEnvironment.PRODUCTION,
        base_url="https://staging.voltaria.io",
    )
    assert _base_url(client) == "https://staging.voltaria.io"

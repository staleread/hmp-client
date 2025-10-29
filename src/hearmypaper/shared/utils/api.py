import cbor2
import requests
from result import Result, Ok, Err


def check_response(
    r: requests.Response, raw_data: bool = False, cbor_data: bool = False
) -> Result[dict | bytes, str]:
    """
    Check HTTP response and return Result.

    Args:
        r: HTTP response
        raw_data: If True, return raw bytes instead of parsing
        cbor_data: If True, parse response as CBOR instead of JSON

    Returns:
        Result with data (dict or bytes) or error message
    """
    if raw_data:
        if r.status_code in [200, 201]:
            return Ok(r.content)
        elif r.status_code == 401:
            return Err("Authentication required. Please log in again.")
        elif r.status_code == 403:
            return Err(
                "Access forbidden. You don't have permission for this operation."
            )
        elif r.status_code == 404:
            return Err("Resource not found.")
        elif r.status_code >= 500:
            return Err("Server error. Please try again later.")
        else:
            return Err(f"{r.status_code}: Request failed")

    try:
        if cbor_data:
            data = cbor2.loads(r.content)
        else:
            data = r.json()
    except (ValueError, cbor2.CBORDecodeError):
        return Err(f"{r.status_code}: Invalid response format")

    if r.status_code in [200, 201]:
        return Ok(data)
    elif r.status_code == 401:
        return Err("Authentication required. Please log in again.")
    elif r.status_code == 403:
        return Err("Access forbidden. You don't have permission for this operation.")
    elif r.status_code == 404:
        return Err("Resource not found.")
    elif r.status_code >= 500:
        return Err("Server error. Please try again later.")
    else:
        error_message = data.get("detail", data.get("error", "Something went wrong"))
        return Err(f"{r.status_code}: {error_message}")

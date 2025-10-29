import cbor2
from result import Result, Err
from typing import Any
from pydantic import TypeAdapter

from ..shared.utils import api as api_utils
from ..shared.utils.session import ApiSession
from . import dto


def list_submissions(session: ApiSession) -> Result[list[dto.SubmissionResponse], str]:
    response = session.get("/submission")
    result = api_utils.check_response(response)

    return result.map(
        lambda d: TypeAdapter(list[dto.SubmissionResponse]).validate_python(d)
    )


def upload_submission(
    session: ApiSession, project_id: int, title: str, encrypted_content: bytes
) -> Result[int, str]:
    payload: dict[str, Any] = {
        "project_id": project_id,
        "title": title,
        "encrypted_content": encrypted_content,
    }
    cbor_bytes = cbor2.dumps(payload)

    response = session.post(
        "/submission",
        headers={"Content-Type": "application/cbor"},
        data=cbor_bytes,
    )

    result = api_utils.check_response(response)
    return result.map(lambda d: d["id"] if isinstance(d, dict) and "id" in d else 0)


def get_instructor_key(session: ApiSession, project_id: int) -> Result[str, str]:
    response = session.get(
        "/submission/instructor_key", params={"project_id": project_id}
    )

    result = api_utils.check_response(response)
    return result.map(lambda d: d["public_key"] if isinstance(d, dict) else "")


def get_submission_hash(
    session: ApiSession, submission_id: int
) -> Result[dto.SubmissionHashResponse, str]:
    response = session.get(f"/submission/{submission_id}/hash")

    result = api_utils.check_response(response)
    return result.map(
        lambda d: TypeAdapter(dto.SubmissionHashResponse).validate_python(d)
    )


def download_submission_content(
    session: ApiSession, submission_id: int
) -> Result[bytes, str]:
    response = session.get(f"/submission/{submission_id}/content")

    result = api_utils.check_response(response, raw_data=True)
    # Ensure we return bytes only
    return result.map(lambda d: d if isinstance(d, bytes) else b"")


def get_server_public_key(session: ApiSession) -> Result[str, str]:
    try:
        response = session.get("/credentials/public-key")
        result = api_utils.check_response(response)
        return result.map(lambda d: d["public_key"] if isinstance(d, dict) else "")
    except Exception as e:
        return Err(f"Network error: {e}")


def get_upload_key(session: ApiSession) -> Result[dto.UploadKeyResponse, str]:
    try:
        response = session.get("/pdf-to-audio/upload-key")
        result = api_utils.check_response(response)
        return result.map(
            lambda data: TypeAdapter(dto.UploadKeyResponse).validate_python(data)
        )
    except Exception as e:
        return Err(f"Network error: {e}")


def execute_pdf_to_audio(
    session: ApiSession, req: dto.PdfToAudioRequest
) -> Result[dto.PdfToAudioResponse, str]:
    try:
        payload = {
            "encrypted_file": req.encrypted_file,
            "encrypted_aes_key": req.encrypted_aes_key,
            "speed": req.speed,
        }
        cbor_bytes = cbor2.dumps(payload)

        response = session.post(
            "/pdf-to-audio/execute",
            headers={
                "Content-Type": "application/cbor",
                "Content-Length": str(len(cbor_bytes)),
            },
            data=cbor_bytes,
        )
        result = api_utils.check_response(response, cbor_data=True)
        return result.map(
            lambda data: TypeAdapter(dto.PdfToAudioResponse).validate_python(data)
        )
    except Exception as e:
        return Err(f"Network error: {e}")

"""Windows Credential Manager storage; never writes secrets to app files."""
import ctypes
from ctypes import wintypes
import json
import os
import sys

TARGET = 'BaekJaeYeol.Stockbot.Toss.v1'


class CredentialError(RuntimeError):
    pass


def validate(value):
    if not isinstance(value, dict) or set(value) != {'client_id', 'client_secret', 'account_seq'}:
        raise CredentialError('인증정보 형식을 확인하세요.')
    if any(not isinstance(v, str) or '\x00' in v for v in value.values()):
        raise CredentialError('인증정보 형식을 확인하세요.')
    if not value['client_id'].strip() or not value['client_secret'].strip():
        raise CredentialError('Client ID와 Client Secret을 입력하세요.')
    if value['account_seq'] and not value['account_seq'].isdigit():
        raise CredentialError('계좌 선택 값은 숫자여야 합니다.')
    if len(json.dumps(value).encode('utf-8')) > 2560:
        raise CredentialError('인증정보가 너무 깁니다.')
    return value


class WindowsVault:
    def __init__(self, target=TARGET):
        self.target = target

    def api(self):
        if sys.platform != 'win32':
            raise CredentialError('인증정보 저장은 Windows에서만 지원합니다.')
        class Credential(ctypes.Structure):
            _fields_ = [('Flags', wintypes.DWORD), ('Type', wintypes.DWORD),
                        ('TargetName', wintypes.LPWSTR), ('Comment', wintypes.LPWSTR),
                        ('LastWritten', wintypes.FILETIME), ('CredentialBlobSize', wintypes.DWORD),
                        ('CredentialBlob', ctypes.POINTER(ctypes.c_ubyte)), ('Persist', wintypes.DWORD),
                        ('AttributeCount', wintypes.DWORD), ('Attributes', ctypes.c_void_p),
                        ('TargetAlias', wintypes.LPWSTR), ('UserName', wintypes.LPWSTR)]
        api = ctypes.WinDLL('Advapi32.dll', use_last_error=True)
        api.CredWriteW.argtypes = [ctypes.POINTER(Credential), wintypes.DWORD]
        api.CredWriteW.restype = wintypes.BOOL
        api.CredReadW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(ctypes.POINTER(Credential))]
        api.CredReadW.restype = wintypes.BOOL
        api.CredDeleteW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD]
        api.CredDeleteW.restype = wintypes.BOOL
        api.CredFree.argtypes = [ctypes.c_void_p]
        api.CredFree.restype = None
        return api, Credential

    def load(self):
        if sys.platform != 'win32':
            return None
        api, credential = self.api()
        pointer = ctypes.POINTER(credential)()
        if not api.CredReadW(self.target, 1, 0, ctypes.byref(pointer)):
            if ctypes.get_last_error() == 1168:
                return None
            raise CredentialError('Windows 인증정보를 읽을 수 없습니다.')
        try:
            size = pointer.contents.CredentialBlobSize
            if not 0 < size <= 2560:
                raise CredentialError('저장된 인증정보 형식 오류')
            return validate(json.loads(ctypes.string_at(pointer.contents.CredentialBlob, size).decode('utf-8')))
        except (ValueError, UnicodeError, TypeError):
            raise CredentialError('저장된 인증정보를 다시 등록하세요.') from None
        finally:
            api.CredFree(pointer)

    def save(self, value):
        raw = json.dumps(validate(value)).encode('utf-8')
        api, credential = self.api()
        buffer = (ctypes.c_ubyte * len(raw)).from_buffer_copy(raw)
        item = credential()
        item.Type = 1  # CRED_TYPE_GENERIC
        item.TargetName = self.target
        item.UserName = 'Toss Open API'
        item.Persist = 2  # Same Windows user, subsequent logon sessions, this computer.
        item.CredentialBlobSize = len(raw)
        item.CredentialBlob = ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte))
        try:
            if not api.CredWriteW(ctypes.byref(item), 0):
                raise CredentialError('Windows 인증정보 저장 실패. 기존 저장 값은 변경하지 않았습니다.')
        finally:
            ctypes.memset(buffer, 0, len(raw))

    def delete(self):
        api, _ = self.api()
        if not api.CredDeleteW(self.target, 1, 0) and ctypes.get_last_error() != 1168:
            raise CredentialError('Windows 인증정보 삭제 실패')


def environment_credentials():
    return validate({'client_id': os.environ.get('TOSS_CLIENT_ID', ''),
                     'client_secret': os.environ.get('TOSS_CLIENT_SECRET', ''),
                     'account_seq': os.environ.get('TOSS_ACCOUNT_SEQ', '')})


def resolve_credentials():
    # A saved complete bundle wins; never mix an ID and secret from different sources.
    return WindowsVault().load() or environment_credentials()

"""Thread-owned Windows idle-sleep request. Does not alter power plans/display."""
import ctypes
import sys
import threading

ES_CONTINUOUS=0x80000000
ES_SYSTEM_REQUIRED=0x00000001

class SleepGuard:
    def __init__(self,*,platform=None,native=None):
        self.supported=(sys.platform if platform is None else platform)=='win32'
        self.native=native;self.active=False;self.previous=None;self.owner=None;self.error=None

    def acquire(self):
        if not self.supported:return True # Other platforms retain their existing execution behavior.
        if self.active:return self.owner==threading.get_ident()
        try:
            if self.native is None:
                from ctypes import wintypes
                self.native=ctypes.WinDLL('kernel32',use_last_error=True).SetThreadExecutionState
                self.native.argtypes=[wintypes.DWORD];self.native.restype=wintypes.DWORD
            previous=self.native(ES_CONTINUOUS|ES_SYSTEM_REQUIRED)
            if not previous:raise OSError('Sleep request failed')
        except (OSError,AttributeError):
            self.error='acquire';return False
        self.previous=previous;self.owner=threading.get_ident();self.active=True;self.error=None
        return True

    def release(self):
        if not self.active:return True
        if self.owner!=threading.get_ident():self.error='release';return False
        try:
            # Preserve execution flags that predated this application's request.
            if not self.native(self.previous|ES_CONTINUOUS):raise OSError('Sleep request release failed')
        except (OSError,AttributeError):
            self.error='release';return False
        self.active=False;self.owner=None;self.error=None
        return True

    def label(self):
        if self.error=='release':return '절전 방지 해제 실패 · 종료 후 전원 상태 확인'
        if self.error=='acquire':return '절전 방지 요청 실패 · 자동 실행 차단'
        if not self.supported:return '절전 방지 미지원 · Windows 전용'
        return '절전 방지 요청 적용' if self.active else '절전 방지 요청 해제'

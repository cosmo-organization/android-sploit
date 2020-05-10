import socket
class Session:
    def __init__(self,_host,_port,_unique_session_id=None):
        self._host=_host
        self._port=_port
        self._sock=socket.socket()
        self.closed=True
        self._unique_session_id=_unique_session_id
    def start_session(self):
        self._sock.connect((self._host,self._port))
        self.closed=False
    def get_connection(self):
        return self._sock
    def stop_session(self):
        self._sock.close()
    def is_closed(self):
        return self.closed
    def get_session_id(self):
        return self._unique_session_id
class SessionManager:
    def __init__(self):
        self._sessions=[]
    def add_session(self,_open_session):
        self.sync_session()
        if self.validate_session_id(_open_session):
           self._sessions.append(_open_session)
    def sync_session(self):
        for _session in self._sessions:
            if _session.is_closed():
                self._sessions.remove(_session)
    def validate_session_id(self,_open_session):
        for _session in self._sessions:
            if _open_session.get_session_id() is None:
                return True
            elif _session.get_session_id() is _open_session.get_session_id():
                print(f"Session ID:{_open_session.get_session_id()} is duplicate")
                return False
        return True
    def remove_session(self,_unique_session_id):
        for _session in self._sessions:
            if _session.get_session_id() is _unique_session_id:
                self._sessions.remove(_session)
    def remove_session(self,_open_session):
        if _open_session.is_closed():
          self._sessions.remove(_open_session)
        else:
            print("Session is opened can't remove session from SessionManager")
    def get_session(self,_unique_session_id):
        for _session in self._sessions:
            if _session.get_session_id() is _unique_session_id:
                return _session
    def get_session(self,_index):
        return self._sessions[_index]
    def close_all_session(self):
        for _session in self._sessions:
            _session.stop_session()
    def remove_all_closed_session(self):
        for _session in self._sessions:
            if _session.is_closed():
                self._sessions.remove(_session)


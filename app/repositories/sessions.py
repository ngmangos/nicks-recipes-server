from utils.json_store import load_data, save_data
from schemas import Session

FILE = "data/session.json"

def store_session(session: Session):
    sessions = load_data(FILE)
    sessions[session.id] = session.dict()
    save_data(FILE, sessions)
    return session.id
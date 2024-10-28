from .interface import Pipeline

def load_pipeline(name: str, **params) -> Pipeline:
    if name == "streamkohaku":
        from .streamkohaku import StreamKohaku
        return StreamKohaku(**params)
    elif name == "liveportrait":
        from .liveportrait import LivePortrait
        return LivePortrait(**params)
    raise ValueError(f"Unknown pipeline: {name}")

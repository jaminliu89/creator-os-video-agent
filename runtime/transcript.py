from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List

STAMP = re.compile(r'^\s*\[?(?:(\d{1,2}):)?(\d{1,2}):(\d{2})(?:[\.,](\d{1,3}))?\]?\s*(.*)$')


def _seconds(h: str|None, m: str, s: str, ms: str|None) -> float:
    return (int(h or 0)*3600)+(int(m)*60)+int(s)+(int(ms or 0)/(10**len(ms) if ms else 1))


def normalize_text(text: str) -> Dict[str, Any]:
    segments: List[Dict[str, Any]]=[]
    pending=[]
    for raw in text.splitlines():
        line=raw.strip()
        if not line: continue
        match=STAMP.match(line)
        if match:
            if pending and segments:
                segments[-1]['text'] += ' ' + ' '.join(pending); pending=[]
            h,m,s,ms,body=match.groups()
            segments.append({'id':f'seg-{len(segments)+1}','start':_seconds(h,m,s,ms),'text':body.strip()})
        elif segments:
            segments[-1]['text'] += (' ' if segments[-1]['text'] else '') + line
        else:
            pending.append(line)
    if not segments:
        body=' '.join(pending).strip()
        if body: segments=[{'id':'seg-1','start':0.0,'text':body}]
    for i,seg in enumerate(segments):
        next_start=segments[i+1]['start'] if i+1<len(segments) else None
        seg['end']=next_start
    return {'version':'1.0','segments':segments,'has_timestamps':any(s['start']>0 for s in segments)}


def normalize_file(source: Path, target: Path) -> Dict[str, Any]:
    result=normalize_text(Path(source).read_text(encoding='utf-8'))
    import json
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    return result

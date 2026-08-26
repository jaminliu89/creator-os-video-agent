from __future__ import annotations

from typing import Any, Dict


def compile_storyboard(director_ir: Dict[str, Any]) -> Dict[str, Any]:
    scenes=[]
    for index, seg in enumerate(director_ir.get('segments', []), start=1):
        scenes.append({
            'scene_id': f'scene-{index}',
            'source_segment_id': seg.get('id'),
            'start': seg.get('start'),
            'end': seg.get('end'),
            'transcript': seg.get('transcript',''),
            'narrative_function': seg.get('narrative_function','exposition'),
            'director_intent': seg.get('director_intent','preserve_clarity'),
            'attention_target': seg.get('attention_target'),
            'shot': seg.get('shot_decision',{}),
            'edit': seg.get('edit_decision',{}),
            'camera': seg.get('camera_intent',{}),
            'motion': seg.get('motion_intent',{}),
            'caption': seg.get('caption_intent',{}),
            'audio': seg.get('audio_intent',{}),
            'broll': seg.get('broll_intent',{}),
            'performance': seg.get('performance_intent',{}),
            'confidence': seg.get('confidence'),
        })
    return {
        'version':'1.0',
        'source':director_ir.get('source'),
        'scene_count':len(scenes),
        'scenes':scenes,
    }

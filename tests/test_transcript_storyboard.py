from runtime.transcript import normalize_text
from runtime.storyboard import compile_storyboard


def test_plain_transcript_normalizes_to_single_segment():
    r=normalize_text('第一句。\n第二句。')
    assert r['version']=='1.0'
    assert r['segments'][0]['start']==0.0
    assert '第二句' in r['segments'][0]['text']


def test_timestamped_transcript_preserves_boundaries():
    r=normalize_text('[00:01] 第一段\n[00:03] 第二段')
    assert len(r['segments'])==2
    assert r['segments'][0]['start']==1.0
    assert r['segments'][0]['end']==3.0
    assert r['has_timestamps'] is True


def test_storyboard_compiles_director_ir_without_provider_fields():
    d={'source':{'type':'video'},'segments':[{'id':'s1','start':0,'end':2,'transcript':'其实问题不是流量。','narrative_function':'revelation','director_intent':'force_audience_refocus','camera_intent':{'movement':'subtle-push-in'},'motion_intent':{'enter':'blur-fade-rise'},'confidence':.8}]}
    s=compile_storyboard(d)
    assert s['scene_count']==1
    scene=s['scenes'][0]
    assert scene['director_intent']=='force_audience_refocus'
    assert scene['camera']['movement']=='subtle-push-in'
    assert 'provider' not in scene

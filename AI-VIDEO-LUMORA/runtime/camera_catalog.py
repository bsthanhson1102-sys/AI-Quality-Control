"""Camera-motion vocabulary sourced from the 16-slide NBOX AI reference.

Reference: https://docs.google.com/presentation/d/1HbZA208TCIW721A6NL0w3N2qdqA-VBnf/htmlpresent
This is a prompt-planning aid, not an actual camera control or video renderer.
"""
from dataclasses import dataclass

GROUPS = {
    "A_orbit": """orbit 360|orbit left|orbit right|half orbit|slow orbit|fast orbit|arc shot|orbit and rise|orbit and descend|spiral up|spiral down|360 turntable""",
    "B_drone": """drone fly|drone fly over|drone fly through|drone reveal|drone pull back|drone push in|aerial view|top down shot|top down rotate|FPV drone|FPV dive|flyover landscape""",
    "C_dolly": """dolly in|dolly out|push in|pull out|slow push in|fast push in|dolly zoom|reverse dolly zoom|truck left|truck right|tracking shot|follow shot|lead shot|parallax slide""",
    "D_pan_tilt": """pan left|pan right|slow pan|whip pan|tilt up|tilt down|tilt up reveal|dutch angle|camera roll|barrel roll|pan and tilt|swing shot""",
    "E_crane": """pedestal up|pedestal down|crane up|crane down|jib shot|boom shot|rise and reveal|ground to sky""",
    "F_lens": """zoom in|zoom out|crash zoom|snap zoom|slow zoom|earth zoom out|earth zoom in|macro zoom|eye zoom|fisheye lens|wide angle|telephoto compression|anamorphic lens|tilt shift""",
    "G_focus": """focus pull|rack focus|shallow depth of field|deep focus|bokeh background|focus reveal|split diopter|soft focus""",
    "H_time": """time lapse|day to night time lapse|hyperlapse|slow motion|super slow motion|speed ramp|freeze frame|bullet time|reverse motion|motion blur""",
    "I_handheld": """handheld|shaky cam|steadicam|gimbal shot|POV shot|walking POV|car mount shot|camera shake impact""",
    "J_composition": """epic shot|establishing shot|low angle|high angle|worm's eye view|over the shoulder|extreme close up|close up|medium shot|wide shot|symmetrical shot|silhouette shot""",
    "K_special": """through the window|through the keyhole|portal transition|match cut transition|infinite zoom|vertigo effect|levitation float|underwater move|lens flare sweep|light leak""",
}
EXPECTED_COUNTS = (12, 12, 14, 12, 8, 14, 8, 10, 8, 12, 10)
CAMERA_TERMS = tuple(term for raw in GROUPS.values() for term in raw.split("|"))
COMBOS = (
    ("slow push in", "shallow depth of field"),
    ("drone reveal", "golden hour"),
    ("orbit 360", "slow motion"),
    ("time lapse", "crane up"),
    ("FPV dive", "motion blur"),
)
STYLE_TERMS = {"golden hour", "smooth", "slow", "fast"}
# Medical footage should not use spectacular camera effects to misrepresent outcomes.
MEDICAL_REVIEW_REQUIRED = True


def validate_catalog():
    counts = tuple(len(v.split("|")) for v in GROUPS.values())
    return counts == EXPECTED_COUNTS and len(CAMERA_TERMS) == 120 and len(set(CAMERA_TERMS)) == 120


def build_camera_prompt(scene, movements, style=None, *, medical=False):
    if not isinstance(scene, str) or not scene.strip():
        raise ValueError("Scene description required")
    if not isinstance(movements, (list, tuple)) or not 1 <= len(movements) <= 2:
        raise ValueError("Use one or two camera/effect keywords per shot")
    if any(m not in CAMERA_TERMS for m in movements):
        raise ValueError("Unknown source camera term")
    if len(set(movements)) != len(movements):
        raise ValueError("Duplicate camera terms")
    if style is not None and style not in STYLE_TERMS:
        raise ValueError("Unknown style modifier")
    if medical and any(m in {"dolly zoom", "reverse dolly zoom", "fisheye lens", "tilt shift", "eye zoom", "infinite zoom"} for m in movements):
        raise ValueError("Potentially misleading medical visual effect requires manual planning")
    prompt = scene.strip() + ", " + ", ".join(movements)
    if style:
        prompt += ", " + style
    return {"prompt": prompt, "source_terms": list(movements), "medical_review_required": bool(medical), "rendered": False}

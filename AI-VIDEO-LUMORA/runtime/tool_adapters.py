"""Tool-neutral camera technique adapter for AI-EDIT.

Generates instructions only; does not claim to operate CapCut/Canva or render media.
"""
from camera_catalog import CAMERA_TERMS, build_camera_prompt

AI_PROMPT_TOOLS = {"flow", "kling", "wan", "runway", "generic_ai"}
TIMELINE_TOOLS = {"capcut", "canva", "premiere", "davinci", "ffmpeg"}
TOOLS = AI_PROMPT_TOOLS | TIMELINE_TOOLS

# Approximation means editing existing footage; it does not create new 3D viewpoints.
TIMELINE_RECIPES = {
    "slow push in": "Animate scale smoothly upward over the shot using keyframes; crop safely and preserve face proportions.",
    "push in": "Increase scale progressively with keyframes, or use footage from a physical dolly move.",
    "dolly in": "Prefer footage captured moving forward; digital scale animation is only a 2D approximation.",
    "dolly out": "Prefer footage captured moving backward; digital scale animation is only a 2D approximation.",
    "pan left": "Animate horizontal framing to the left within available source margins.",
    "pan right": "Animate horizontal framing to the right within available source margins.",
    "tilt up": "Animate vertical framing upward within available source margins.",
    "tilt down": "Animate vertical framing downward within available source margins.",
    "zoom in": "Animate scale upward with keyframes; inspect crop and resolution.",
    "zoom out": "Animate scale downward; ensure the frame has enough background.",
    "slow zoom": "Use gradual scale keyframes with smooth interpolation.",
    "freeze frame": "Freeze the selected source frame for the desired duration.",
    "slow motion": "Reduce playback speed; inspect frame cadence or optical flow artifacts.",
    "speed ramp": "Use a speed curve with gradual interpolation and check audio synchronization.",
    "shallow depth of field": "Use authentic shallow-DOF footage or selectively blur background with subject masking.",
    "bokeh background": "Prefer authentic optical bokeh; artificial blur is an approximation.",
    "rack focus": "Prefer footage with real focus shift; masked blur transitions are an approximation.",
    "match cut transition": "Align framing, shape, or action across two source shots before cutting.",
    "light leak": "Use a licensed light-leak overlay with restrained opacity.",
}
# Effects that need source footage, 3D, AI generation or a tool-specific verified feature.
NOT_SIMPLE_2D = {
    "orbit 360", "orbit left", "orbit right", "half orbit", "slow orbit",
    "drone fly", "drone fly over", "drone fly through", "drone reveal",
    "FPV drone", "FPV dive", "dolly zoom", "reverse dolly zoom",
    "bullet time", "earth zoom out", "earth zoom in", "infinite zoom",
    "through the keyhole", "portal transition",
}


def adapt_shot(scene, techniques, tool, *, medical=False):
    if tool not in TOOLS:
        raise ValueError("Unsupported target tool")
    base = build_camera_prompt(scene, techniques, medical=medical)
    if tool in AI_PROMPT_TOOLS:
        return {**base, "tool": tool, "mode": "prompt", "instructions": [base["prompt"]], "capability_verified": False}
    instructions = []
    limitations = []
    for term in techniques:
        if term in TIMELINE_RECIPES:
            instructions.append(TIMELINE_RECIPES[term])
        elif term in NOT_SIMPLE_2D:
            limitations.append(f"{term}: requires suitable footage, 3D, or supported AI generation; cannot be recreated faithfully from a single flat image")
        else:
            limitations.append(f"{term}: verify feature availability in {tool} or supply suitable footage; no universal recipe verified")
    return {**base, "tool": tool, "mode": "timeline_plan", "instructions": instructions, "limitations": limitations, "capability_verified": False}

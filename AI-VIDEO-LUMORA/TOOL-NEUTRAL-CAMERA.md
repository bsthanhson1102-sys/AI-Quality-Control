# AI-EDIT camera techniques: tool-neutral execution

The 120 source camera/effect keywords in `runtime/camera_catalog.py` are **creative vocabulary**, not proprietary commands limited to Flow/Kling/Wan. This project maps them to implementation plans based on target tool and available footage.

## Supported planning targets
- **CapCut**: keyframes, crop/scale, speed, transitions, masking where available.
- **Canva**: supported animation, crop/scale and timeline effects; feature availability varies by editor/account/version.
- **Premiere / DaVinci**: motion transforms, keyframes, masks, speed and color.
- **FFmpeg**: automate supported 2D transforms and compositing, not arbitrary physical camera movement.
- **Flow / Kling / Wan / Runway / generic AI**: text prompt vocabulary, subject to model-specific support.

## Critical distinction
A digital zoom/pan is not a true dolly/parallax move; a 360-degree orbit cannot be faithfully derived from one flat image without generating new scene geometry. AI-EDIT must not claim full fidelity from an approximation.

Use `runtime/tool_adapters.py:adapt_shot` to obtain a tool-specific **plan**, not a verified action or finished MP4. A tool integration becomes VERIFIED only after actual execution and output review.

For aesthetic medicine, preserve facial anatomy and truthful outcomes; never imply synthetic imagery is genuine patient footage. Canonical CORE and video-master are unchanged.

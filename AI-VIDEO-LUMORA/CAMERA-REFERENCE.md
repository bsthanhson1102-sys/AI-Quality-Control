# NBOX AI camera-motion reference — AI-EDIT integration

Source (16 slides): https://docs.google.com/presentation/d/1HbZA208TCIW721A6NL0w3N2qdqA-VBnf/htmlpresent

The user's supplied deck is titled **Google_Flow_120_hieu_ung_camera.pptx**, with 120 numbered English camera/effect keywords grouped A–K (11 groups), plus five suggested combinations. It is a prompt vocabulary for Google Flow/Kling/Wan, **not a collection of actual executable skills, camera APIs or a rendering engine**.

## Source-derived usage
1. Describe the shot in natural language, then append camera keyword(s) in English.
2. Prefer **one or two** camera/effect keywords per shot, per slide 2.
3. Optionally add pacing/light cues; verify supported syntax per model, not assumed universal.
4. Test several generations, as outputs vary with source images and model versions.

## Groups and counts
A Orbit 12; B Drone 12; C Dolly/track 14; D Pan/tilt 12; E Crane 8; F Zoom/lens 14; G Focus 8; H Time/speed 10; I Handheld 8; J Composition 12; K Special 10. All 120 terms are preserved in `runtime/camera_catalog.py` in the source order.

## Source's five suggested combinations
- slow push in + shallow depth of field (emotional)
- drone reveal + golden hour (opening)
- orbit 360 + slow motion (product/person)
- time lapse + crane up (city/building)
- FPV dive + motion blur (action)

## AI-EDIT application
Use `build_camera_prompt(scene, movements, style, medical=True)` for planning individual shots. For Lumora, prioritize restrained movement, clear facial anatomy, natural proportions, stable lighting, truthful treatment depiction and consent. **No automatic inference of medical efficacy from a cinematic effect.** Synthetic scenes must not be presented as authentic patient outcomes. Avoid distorted face/skin anatomy, deceptive before-after edits or unapproved likenesses.

This integration is a **project-scoped camera vocabulary adapter**, not a change to canonical `SKILLS/video-master/SKILL.md`, `REGISTRY` or `CORE`. It has no production capability, model credentials, subscription, license grant or external publication. Tests must be executed before claiming verified runtime integration.

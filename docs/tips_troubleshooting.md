# Tips and troubleshooting

---

## 🎨 Using with Materialize

[**Materialize**](http://boundingboxsoftware.com/materialize/) is a powerful tool for generating textures like AO, Metallic, and others. Here's how I personally use it to quickly generate masks for Unity's HDRP:

1. Start with a base map texture.
2. Use Materialize to generate your new textures (Metallic, AO, Smoothness).
3. Drag and drop the generated textures into the Mask Map Wizard (from unity).

---

## Empty channels?

If you don’t have a texture for one of the channels (Metallic, AO, etc.), leave it empty:  

> The tool will fill it with pure black (0) by default.

This way, Unity interprets it as “no effect” for that channel, keeping your material safe.

---

## Using Roughness instead of Smoothness?

**No worries!**
You can drop a **Roughness** map in the Smoothness field — the app will ask if you want to **invert** it to Smoothness.  
This ensures compatibility with Unity HDRP’s alpha channel convention (Smoothness = bright / glossy).

---

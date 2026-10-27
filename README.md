# Silent Sounds

An open-source digital music library, preserving the sounds of those which are perishing.

An early, runnable listening-archive prototype for India's musical heritage.

## Run locally

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit, usually `http://localhost:8501`.

To see detailed logs, start it with:

```powershell
python -m streamlit run app.py --logger.level=debug
```

The logs appear in the terminal running Streamlit. Stop the server with `Ctrl+C`.

## Current scope

- All 28 states and 8 Union Territories are clickable on a Wikimedia Commons state-boundary map; a keyboard-accessible state selector is also available.
- The catalog currently includes 27 source-linked starter instruments; eight have locally bundled image assets.
- Filter entries by region, instrument family, status, and era.
- Instrument pages open as an immersive stage with a scroll-triggered curtain reveal, licensed recording playback where available, and interactive synthesized previews. Synthesis is not presented as an authentic recording or historical reconstruction.
- Optional ElevenLabs Music API support can generate short AI musical sketches. Generated audio is labeled as synthetic, not an instrument recording.
- The included Gauhar Jaan vocal recording is kept separate from instrument sound studies.
- Image and recording credits are listed in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

This prototype currently runs on Streamlit because Node.js/npm is not installed in the workspace. Community notes, realtime rooms, a reviewed archival catalog, and the Next.js migration are not implemented yet.

## Optional ElevenLabs music sketches

Create an API key in ElevenLabs with Music API access. Keep it private; do not paste it into source files, the browser, or chat. In the PowerShell terminal that will run Streamlit, set it for that terminal session:

```powershell
$env:ELEVENLABS_API_KEY = "your-key"
python -m streamlit run app.py
```

Open an instrument, expand **Optional · AI-generated musical sketch**, and compose a short instrumental. The key is read by Python only and is never sent to the browser. The generated clip appears as a separate AI-labeled stage control. Usage may consume ElevenLabs credits. See the [official Music API](https://elevenlabs.io/docs/api-reference/music/compose) and [authentication guide](https://elevenlabs.io/docs/api-reference/authentication).
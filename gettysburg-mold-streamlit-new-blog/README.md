# Gettysburg Bathroom Ceiling Moisture Guide — Streamlit

This folder is a **single-page Streamlit app**, designed to be deployed from a GitHub repository. The article is **new and independent** of the earlier Vercel, Netlify, Cloudflare, Firebase and Render articles.

## What stays unchanged

- Exact anchor (second paragraph): **Bathroom & Kitchen Mold Removal Gettysburg, PA**
- Destination: https://gettysburgmoldremediationpros.com/bathroom-kitchen-mold-removal-gettysburg-pa/
- Google Map: 129 Chambersburg St, Gettysburg, PA 17325
- Nine supplied profiles: Houzz, Manta, Yelp, Facebook, YouTube, X, Pinterest, TikTok, Quora
- Simple, text-first layout: no photos, custom header, navbar, footer, or sidebar

## Files

- `app.py` — Streamlit entrypoint
- `article.html` — complete single-page blog, map embed, and social icons
- `requirements.txt` — Streamlit dependency
- `.streamlit/config.toml` — appearance preferences

## Deploy from GitHub (no local coding required)

1. Create a **new GitHub repository**.
2. Upload `app.py`, `article.html`, `requirements.txt`, and the `.streamlit` folder **to the repository root**. Do not upload just the ZIP or place everything within an extra subfolder.
3. Open https://share.streamlit.io and sign in with GitHub.
4. Choose **Create app** > **Yup, I have an app**.
5. Select the repo and `main` branch. Set **Main file path** to `app.py`.
6. Click **Deploy**. The app will receive a `*.streamlit.app` URL.

### Caveat

Unlike HTML-first hosting, Streamlit renders content as a Python web app, including an embedded document. Its pages are **not dependable SEO landing pages**: do not assume Google will index the complete article or count its link. Hosting on a different subdomain does not automatically transfer backlink authority.

If `st.iframe` is not available, confirm Streamlit 1.66+ installed from `requirements.txt`. The Google Map needs a network connection and may be blocked by browser privacy settings.

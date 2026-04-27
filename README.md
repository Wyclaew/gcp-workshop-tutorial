# GCP Cloud Run Workshop Tutorial (v2.5 - Gemini Flash)

Bu proje, Google'in en yeni **Gemini 2.5 Flash** AI modelini kullanarak YouTube videolarini akilli bir sekilde ozetleyen bir web uygulamasi olusturmayi ve Google Cloud Run'a deploy etmeyi ogretir.

## Baslatmak icin:

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/open?git_repo=https://github.com/GDGonCampusPAU/gcp-workshop-tutorial&tutorial=tutorial.md&cloudshell_git_branch=summarizer-v2.5)

### Kurulum Adimlari:

Cloud Shell terminalinde su komutu calistirarak workshop'u baslatabilirsiniz:

```bash
rm -rf ~/gcp-workshop-tutorial && git clone -b summarizer-v2.5 https://github.com/GDGonCampusPAU/gcp-workshop-tutorial.git && cloudshell launch-tutorial ~/gcp-workshop-tutorial/tutorial.md
```

## Yeni Ozellikler (v2.5)

- **Gemini 2.5 Flash Entegrasyonu:** En yeni ve en hizli AI modeli.
- **Transcript (Altyazi) Analizi:** Videoda konusulanlari cekip gercek verilerle ozetleme.
- **Video Metadata:** Baslik ve aciklama bilgilerini kullanarak uydurma (hallucination) riskini azaltma.
- **Gelistirilmis IAM Scripti:** Tum izinleri tek seferde kuran otomatik yapılandırma.

## Ne Ogreneceksiniz?

- Vertex AI (Gemini 2.5 Flash) Kullanımı
- Python Flask & REST API
- YouTube Transcript & Metadata API Entegrasyonu
- Google Cloud Run'a Serverless Deployment
- IAM ve GCP Kredi Yonetimi

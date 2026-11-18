html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<title>Dhikr Tracker by hafizh.arz</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Poppins:wght@300;400;500;600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{overflow:hidden;background:#070d1f;font-family:'Poppins',sans-serif;touch-action:manipulation;user-select:none;-webkit-tap-highlight-color:transparent}

/* ── LANDING ── */
#landing{
  position:fixed;inset:0;z-index:200;
  display:flex;align-items:center;justify-content:center;
  opacity:1;
  transition:opacity 0.9s ease;
  overflow-y:auto;
}
#landing.hide{opacity:0;pointer-events:none}
#lc{position:fixed;inset:0;z-index:0}
.lbox{position:relative;z-index:1;text-align:center;padding:24px 20px;display:flex;flex-direction:column;align-items:center;gap:10px;max-width:410px;width:100%;margin:auto}
.moon-wrap{font-size:60px;line-height:1;animation:moonFloat 4s ease-in-out infinite;filter:drop-shadow(0 0 22px rgba(240,201,122,.75))}
@keyframes moonFloat{0%,100%{transform:translateY(0) rotate(-5deg)}50%{transform:translateY(-9px) rotate(5deg)}}
.bism-ar{font-family:'Amiri',serif;font-size:26px;color:#f0c97a;text-shadow:0 0 22px rgba(240,201,122,.5);line-height:1.35}
.bism-lat{font-size:9px;color:rgba(255,255,255,.38);letter-spacing:2px;margin-top:-4px}

.land-title{
  font-size:clamp(26px,6vw,34px);font-weight:700;color:#fff;
  text-shadow:0 0 36px rgba(255,255,255,.18);line-height:1.15;
  display:flex;flex-direction:column;align-items:center;gap:2px;
}
.land-author{
  font-size:11px;font-weight:400;letter-spacing:1.4px;
  color:rgba(240,201,122,.82);text-transform:lowercase;
}

.verse-card{
  background:rgba(255,255,255,.04);
  border:1px solid rgba(240,201,122,.22);
  border-radius:16px;padding:12px 16px;
  max-width:340px;width:100%;
  backdrop-filter:blur(8px);
}
.verse-ar{
  font-family:'Amiri',serif;font-size:20px;color:#f0c97a;
  line-height:1.6;margin-bottom:4px;
}
.land-sub{font-size:11.5px;color:rgba(255,255,255,.78);line-height:1.65;font-style:italic}
.verse-ref{font-size:10px;color:rgba(240,201,122,.75);margin-top:4px;font-weight:600;letter-spacing:.5px}

.daily-pill{
  margin-top:1px;padding:5px 15px;border-radius:30px;
  background:rgba(240,201,122,.12);border:1px solid rgba(240,201,122,.35);
  color:#f0c97a;font-size:11px;font-weight:600;letter-spacing:.3px;
}

.start-btn{margin-top:4px;padding:14px 36px;border:none;border-radius:50px;background:linear-gradient(135deg,#9c7230,#f0c97a,#9c7230);background-size:200%;color:#0a1628;font-size:14.5px;font-weight:700;cursor:pointer;font-family:inherit;box-shadow:0 0 32px rgba(240,201,122,.4),0 4px 20px rgba(0,0,0,.5);animation:shimmer 3s linear infinite,btnPulse 2.5s ease-in-out infinite;transition:transform .2s}
.start-btn:active{transform:scale(.95)}
@keyframes shimmer{0%{background-position:200%}100%{background-position:-200%}}
@keyframes btnPulse{0%,100%{box-shadow:0 0 28px rgba(240,201,122,.35),0 4px 20px rgba(0,0,0,.5)}50%{box-shadow:0 0 52px rgba(240,201,122,.65),0 4px 20px rgba(0,0,0,.5)}}

/* ── LANGUAGE SELECTOR BOX ── */
.lang-box{
  width:100%;max-width:340px;margin-top:4px;
  background:rgba(10,18,38,.72);
  border:1px solid rgba(240,201,122,.28);
  border-radius:16px;padding:10px 12px;
  backdrop-filter:blur(12px);
}
.lang-box-head{
  display:flex;align-items:center;justify-content:space-between;
  margin-bottom:8px;padding:0 2px;
}
.lang-box-lbl{
  font-size:10px;font-weight:600;color:rgba(240,201,122,.85);
  text-transform:uppercase;letter-spacing:1.1px;
  display:flex;align-items:center;gap:5px;
}
.lang-select{
  background:rgba(255,255,255,.08);
  border:1px solid rgba(240,201,122,.38);
  border-radius:10px;padding:4px 10px;
  color:#f0c97a;font-size:11px;font-weight:600;
  font-family:inherit;cursor:pointer;outline:none;
}
.lang-select option{background:#0d1830;color:#fff}
.lang-grid{
  display:grid;grid-template-columns:repeat(5,1fr);gap:5px;
}
.lbtn{
  padding:5px 4px;border-radius:10px;
  border:1px solid rgba(255,255,255,.14);
  background:rgba(255,255,255,.05);
  color:rgba(255,255,255,.68);
  font-size:10px;cursor:pointer;transition:all .25s;font-family:inherit;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
.lbtn:hover{border-color:rgba(240,201,122,.45);color:#fff}
.lbtn.on{background:rgba(240,201,122,.22);border-color:#f0c97a;color:#f0c97a;font-weight:600}

/* ── APP ── */
#app{
  position:fixed;inset:0;z-index:1;
  opacity:0;pointer-events:none;
  transition:opacity 0.7s ease;
}
#app.show{opacity:1;pointer-events:all}
#c{position:absolute;inset:0;cursor:pointer;z-index:0}
#ui{position:absolute;inset:0;z-index:10;pointer-events:none;display:flex;flex-direction:column;align-items:center;justify-content:space-between}

.top-band{pointer-events:none;text-align:center;padding:20px 20px 14px;width:100%;background:linear-gradient(to bottom,rgba(0,0,0,.62) 55%,transparent)}
.d-ar{font-family:'Amiri',serif;font-size:48px;color:#f0c97a;text-shadow:0 0 26px rgba(240,201,122,.55),0 2px 6px rgba(0,0,0,.8);line-height:1.1}
.d-lat{font-size:15px;color:rgba(255,255,255,.92);margin-top:2px;letter-spacing:.5px;text-shadow:0 1px 4px rgba(0,0,0,.6)}
.d-mean{font-size:11px;color:rgba(255,255,255,.72);margin-top:2px;font-style:italic;text-shadow:0 1px 4px rgba(0,0,0,.6)}

.top-controls{
  pointer-events:all;display:flex;align-items:center;justify-content:space-between;
  padding:0 14px;width:100%;margin-top:4px;gap:8px;
}
.daily-badge{
  pointer-events:all;cursor:pointer;
  display:flex;align-items:center;gap:6px;
  height:36px;padding:0 14px;border-radius:18px;
  background:rgba(12,20,40,.58);backdrop-filter:blur(12px);
  border:1px solid rgba(240,201,122,.35);
  color:#f0c97a;font-size:11px;font-weight:600;
  box-shadow:0 4px 14px rgba(0,0,0,.3);
  transition:all .25s;
}
.daily-badge:active{transform:scale(.95)}
.daily-badge span.num{color:#fff;font-weight:700}

/* ── UNIFIED AESTHETIC CONTROL PILL (Getar, Suara, Bahasa, Home) ── */
.ctrl-pill{
  pointer-events:all;display:flex;align-items:center;gap:4px;
  padding:3px;border-radius:22px;
  background:rgba(12,20,40,.58);backdrop-filter:blur(12px);
  border:1px solid rgba(240,201,122,.32);
  box-shadow:0 4px 14px rgba(0,0,0,.32);
}
.ibtn{
  width:32px;height:32px;border-radius:50%;
  border:1px solid transparent;
  background:transparent;
  color:rgba(255,255,255,.55);
  cursor:pointer;display:flex;align-items:center;justify-content:center;
  transition:all .25s ease;pointer-events:all;flex-shrink:0;
}
.ibtn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.ibtn:hover{color:#fff;background:rgba(255,255,255,.08)}
.ibtn.on{
  background:linear-gradient(135deg,rgba(156,114,48,.38),rgba(240,201,122,.28));
  border-color:rgba(240,201,122,.65);
  color:#f0c97a;
  box-shadow:0 0 12px rgba(240,201,122,.22);
}
.ibtn:active{transform:scale(.92)}

.chud{pointer-events:none;display:flex;flex-direction:column;align-items:center;gap:8px;transition:opacity .4s}
.cw{position:relative;width:170px;height:170px;border-radius:50%;background:radial-gradient(circle,rgba(0,0,0,.28) 0%,rgba(0,0,0,.05) 70%,transparent 100%)}
.csv{width:100%;height:100%;transform:rotate(-90deg)}
.rbg{fill:none;stroke:rgba(255,255,255,.2);stroke-width:5}
.rfg{fill:none;stroke:url(#rg);stroke-width:5;stroke-linecap:round;transition:stroke-dashoffset .45s cubic-bezier(.4,0,.2,1);filter:drop-shadow(0 0 7px rgba(240,201,122,.6))}
.cnum{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.cbig{font-size:62px;font-weight:700;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.55),0 0 22px rgba(255,255,255,.35);line-height:1}
.csml{font-size:11px;color:rgba(255,255,255,.75);letter-spacing:2px;margin-top:-3px;text-shadow:0 1px 4px rgba(0,0,0,.6)}
.thint{font-size:10px;color:rgba(255,255,255,.82);letter-spacing:3px;text-transform:uppercase;text-shadow:0 1px 6px rgba(0,0,0,.65);animation:blink 2.4s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:.45}50%{opacity:.95}}

.bot{pointer-events:all;width:100%;background:linear-gradient(to top,rgba(0,0,0,.78) 55%,transparent);padding:10px 16px 28px;display:flex;flex-direction:column;align-items:center;gap:9px}
.pb{width:min(260px,76%);height:3px;background:rgba(255,255,255,.18);border-radius:2px;overflow:hidden}
.pf{height:100%;background:linear-gradient(to right,#9c7230,#f0c97a);border-radius:2px;transition:width .45s ease}
.slbl{font-size:10px;color:rgba(255,255,255,.84);letter-spacing:1.1px;text-align:center;text-shadow:0 1px 4px rgba(0,0,0,.75)}
.tabs{display:flex;gap:5px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.14);border-radius:30px;padding:4px;backdrop-filter:blur(14px)}
.tab{padding:7px 13px;border-radius:25px;border:none;background:transparent;color:rgba(255,255,255,.65);font-size:11px;font-weight:500;cursor:pointer;transition:all .3s;font-family:inherit}
.tab.on{background:rgba(255,255,255,.94);color:#1a1a2e;font-weight:700}
.trgs{display:flex;gap:7px}
.tbtn{padding:6px 18px;border-radius:20px;border:1px solid rgba(255,255,255,.22);background:rgba(0,0,0,.35);color:rgba(255,255,255,.75);font-size:12px;cursor:pointer;transition:all .3s;font-family:inherit}
.tbtn.on{background:rgba(240,201,122,.24);border-color:#f0c97a;color:#f0c97a;font-weight:600}

#toast{position:fixed;top:66px;left:50%;transform:translateX(-50%) translateY(-70px);background:linear-gradient(135deg,#9c7230,#f0c97a);color:#0a1628;border-radius:30px;padding:9px 22px;font-weight:700;font-size:12px;z-index:300;pointer-events:none;white-space:nowrap;transition:transform .4s cubic-bezier(.34,1.56,.64,1),opacity .4s;opacity:0}
#toast.show{transform:translateX(-50%) translateY(0);opacity:1}

/* ── SUMMARY MODAL ── */
#summary{position:fixed;inset:0;z-index:100;background:rgba(5,10,22,.95);backdrop-filter:blur(18px);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .5s;padding:18px;overflow-y:auto}
#summary.show{opacity:1;pointer-events:all}
.sum-inner{width:100%;max-width:460px;display:flex;flex-direction:column;align-items:center;margin:auto}
.stitle{font-family:'Amiri',serif;font-size:32px;color:#f0c97a;text-align:center;margin-bottom:2px;line-height:1.1}
.sdate{font-size:10.5px;color:rgba(240,201,122,.75);letter-spacing:1.2px;text-transform:uppercase;margin-bottom:5px}
.ssub{font-size:11.5px;color:rgba(255,255,255,.65);text-align:center;margin-bottom:13px;line-height:1.55;max-width:330px}

.grand-total-box{
  width:100%;margin-bottom:12px;
  padding:12px 16px;border-radius:16px;
  background:linear-gradient(135deg,rgba(156,114,48,.24),rgba(240,201,122,.14));
  border:1px solid rgba(240,201,122,.45);
  display:flex;align-items:center;justify-content:space-between;gap:12px;
  box-shadow:0 6px 24px rgba(0,0,0,.35);
}
.gt-left{text-align:left}
.gt-label{font-size:10.5px;font-weight:600;color:#f0c97a;text-transform:uppercase;letter-spacing:1px}
.gt-sub{font-size:9.5px;color:rgba(255,255,255,.55);margin-top:2px}
.gt-num{font-size:34px;font-weight:700;color:#fff;text-shadow:0 0 18px rgba(240,201,122,.5);line-height:1}

.igrid{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;width:100%}
.icard{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:12px 10px;text-align:center;flex:1;min-width:118px;max-width:148px}
.iemoji{font-size:28px;display:block;margin-bottom:3px}
.iname{font-size:10.5px;font-weight:600;color:#f0c97a;margin-bottom:2px}
.inum{font-size:26px;font-weight:700;color:#fff;display:block;line-height:1.1}
.isess{font-size:9.5px;color:rgba(240,201,122,.82);margin-top:2px;font-weight:500}
.idesc{font-size:8.5px;color:rgba(255,255,255,.48);margin-top:4px;line-height:1.45}

/* ── SHARE DA'WAH CARD (WhatsApp Story & Link) ── */
.share-card{
  width:100%;margin-top:12px;padding:13px 15px;
  border-radius:16px;
  background:rgba(37,211,102,.09);
  border:1px solid rgba(37,211,102,.32);
  text-align:center;
}
.share-title{font-size:11.5px;font-weight:600;color:#a7f3d0;line-height:1.5;margin-bottom:9px}
.share-btns{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.wa-story-btn{
  padding:10px 18px;border:none;border-radius:24px;
  background:linear-gradient(135deg,#1ebe5d,#25D366);
  color:#051b0e;font-size:12px;font-weight:700;
  cursor:pointer;font-family:inherit;
  display:inline-flex;align-items:center;gap:7px;
  box-shadow:0 4px 16px rgba(37,211,102,.3);
  transition:transform .2s;
}
.wa-story-btn:active{transform:scale(.95)}
.copy-link-btn{
  padding:10px 15px;border-radius:24px;
  background:rgba(255,255,255,.08);
  border:1px solid rgba(255,255,255,.22);
  color:#fff;font-size:11.5px;font-weight:600;
  cursor:pointer;font-family:inherit;
  display:inline-flex;align-items:center;gap:6px;
  transition:transform .2s;
}
.copy-link-btn:active{transform:scale(.95)}

.sum-actions{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap;justify-content:center}
.sbtn{padding:12px 32px;background:linear-gradient(135deg,#9c7230,#f0c97a);border:none;border-radius:30px;color:#0a1628;font-size:13.5px;font-weight:700;cursor:pointer;font-family:inherit}
.sbtn:active{transform:scale(.96)}
.sbtn-sec{padding:12px 18px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);border-radius:30px;color:rgba(255,255,255,.78);font-size:11.5px;font-weight:600;cursor:pointer;font-family:inherit}
.sbtn-sec:active{transform:scale(.96)}
</style>
</head>
<body>

<div id="toast"></div>

<!-- ══ LANDING ══ -->
<div id="landing">
  <canvas id="lc"></canvas>
  <div class="lbox">
    <div class="moon-wrap">🌙</div>
    <div class="bism-ar">بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ</div>
    <div class="bism-lat">BISMILLAHIRRAHMANIRRAHIM</div>

    <h1 class="land-title">
      <span id="lt">Dhikr Tracker</span>
      <span class="land-author">by hafizh.arz</span>
    </h1>

    <div class="verse-card">
      <div class="verse-ar">أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ</div>
      <p class="land-sub" id="ls">"Ingatlah, hanya dengan mengingat Allah hati menjadi tenteram."</p>
      <div class="verse-ref" id="vRef">— QS. Ar-Ra'd: 28</div>
    </div>

    <div class="daily-pill" id="landDailyPill">📿 Zikir Hari Ini: 0×</div>
    <button class="start-btn" id="startBtn">✨ Bismillah, Mari Berzikir</button>

    <!-- Kolom Opsi Bahasa -->
    <div class="lang-box">
      <div class="lang-box-head">
        <span class="lang-box-lbl" id="langBoxLbl">🌐 Pilih Bahasa</span>
        <select class="lang-select" id="langSelect" aria-label="Pilih Bahasa">
          <option value="id">🇮🇩 Indonesia</option>
          <option value="en">🇬🇧 English</option>
          <option value="ar">🇸🇦 العربية (Arab)</option>
          <option value="zh">🇨🇳 中文 (Mandarin)</option>
          <option value="ko">🇰🇷 한국어 (Korea)</option>
          <option value="ja">🇯🇵 日本語 (Jepang)</option>
          <option value="jv">🇮🇩 Basa Jawa</option>
          <option value="tr">🇹🇷 Türkçe (Turki)</option>
          <option value="ms">🇲🇾 Bahasa Melayu</option>
          <option value="es">🇪🇸 Español (Spanyol)</option>
        </select>
      </div>
      <div class="lang-grid" id="langGrid">
        <button class="lbtn on" data-lang="id">🇮🇩 ID</button>
        <button class="lbtn"    data-lang="en">🇬🇧 EN</button>
        <button class="lbtn"    data-lang="ar">🇸🇦 عربي</button>
        <button class="lbtn"    data-lang="zh">🇨🇳 中文</button>
        <button class="lbtn"    data-lang="ko">🇰🇷 한국</button>
        <button class="lbtn"    data-lang="ja">🇯🇵 日本</button>
        <button class="lbtn"    data-lang="jv">🌿 Jawa</button>
        <button class="lbtn"    data-lang="tr">🇹🇷 TR</button>
        <button class="lbtn"    data-lang="ms">🇲🇾 MY</button>
        <button class="lbtn"    data-lang="es">🇪🇸 ES</button>
      </div>
    </div>
  </div>
</div>

<!-- ══ APP ══ -->
<div id="app">
  <canvas id="c"></canvas>
  <div id="ui">
    <div style="width:100%;display:flex;flex-direction:column;align-items:center">
      <div class="top-band">
        <div class="d-ar"   id="dAr">الحمد لله</div>
        <div class="d-lat"  id="dLat">Alhamdulillah</div>
        <div class="d-mean" id="dMean">"Segala puji bagi Allah"</div>
      </div>
      <div class="top-controls">
        <button class="daily-badge" id="btnStats" title="Rekap Zikir Hari Ini">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/>
          </svg>
          <span id="dailyLabel">Hari Ini:</span>
          <span class="num" id="dailyTotalBadge">0×</span>
        </button>

        <!-- Kontrol Seragam & Estetik: Getar, Suara, Bahasa, Beranda -->
        <div class="ctrl-pill">
          <button class="ibtn on" id="btnVib" title="Getaran" aria-label="Getaran">
            <svg viewBox="0 0 24 24">
              <rect x="7" y="4" width="10" height="16" rx="2"/>
              <path d="M3 8v8"/><path d="M21 8v8"/>
            </svg>
          </button>
          <button class="ibtn on" id="btnSnd" title="Suara" aria-label="Suara">
            <svg id="iconSndOn" viewBox="0 0 24 24">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
              <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
              <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
            </svg>
            <svg id="iconSndOff" viewBox="0 0 24 24" style="display:none">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
              <line x1="23" y1="9" x2="17" y2="15"/>
              <line x1="17" y1="9" x2="23" y2="15"/>
            </svg>
          </button>
          <button class="ibtn" id="btnLang" title="Ganti Bahasa" aria-label="Ganti Bahasa">
            <svg viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="9"/>
              <line x1="3" y1="12" x2="21" y2="12"/>
              <path d="M12 3a14.5 14.5 0 0 1 0 18 14.5 14.5 0 0 1 0-18"/>
            </svg>
          </button>
          <button class="ibtn" id="btnHome" title="Beranda" aria-label="Beranda">
            <svg viewBox="0 0 24 24">
              <path d="M3 10.5L12 3l9 7.5"/>
              <path d="M5 9.5V19a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9.5"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <div class="chud">
      <div class="cw">
        <svg class="csv" viewBox="0 0 170 170">
          <defs>
            <linearGradient id="rg" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%"   stop-color="#9c7230"/>
              <stop offset="100%" stop-color="#f0c97a"/>
            </linearGradient>
          </defs>
          <circle class="rbg" cx="85" cy="85" r="75"/>
          <circle class="rfg" cx="85" cy="85" r="75"
                  id="rfg" stroke-dasharray="471.24" stroke-dashoffset="471.24"/>
        </svg>
        <div class="cnum">
          <div class="cbig" id="cNum">0</div>
          <div class="csml" id="cOf">/ 33</div>
        </div>
      </div>
      <div class="thint" id="tapHint">KETUK LAYAR</div>
    </div>

    <div class="bot">
      <div class="slbl" id="sLbl">🦋 Alhamdulillah — Pagi cerah & makhluk bermain penuh syukur</div>
      <div class="pb"><div class="pf" id="pFill" style="width:0%"></div></div>
      <div class="tabs">
        <button class="tab on" id="tab0">Alhamdulillah</button>
        <button class="tab"    id="tab1">Subhanallah</button>
        <button class="tab"    id="tab2">Astagfirullah</button>
      </div>
      <div class="trgs">
        <button class="tbtn on" id="trg33">33×</button>
        <button class="tbtn"    id="trg99">99×</button>
      </div>
    </div>
  </div>
</div>

<!-- ══ SUMMARY ══ -->
<div id="summary">
  <div class="sum-inner">
    <div class="stitle" id="sumTitle">MasyaAllah!</div>
    <div class="sdate"  id="sumDate"></div>
    <div class="ssub"   id="sumSub">Zikirmu telah mengubah dunia. Semoga Allah menerima amalanmu. Aamiin 🤲</div>

    <div class="grand-total-box">
      <div class="gt-left">
        <div class="gt-label" id="gtLabel">Total Seluruh Zikir Hari Ini</div>
        <div class="gt-sub"   id="gtSub">Tersimpan otomatis • Direset setiap pergantian hari</div>
      </div>
      <div class="gt-num" id="gtNum">0×</div>
    </div>

    <div class="igrid" id="iGrid"></div>

    <!-- Ajakan Sebar Kebaikan & Share Story WhatsApp -->
    <div class="share-card">
      <div class="share-title" id="shareTitle">✨ Yuk sebarkan link zikir ini ke temanmu, agar kebaikan terus menyebar!</div>
      <div class="share-btns">
        <button class="wa-story-btn" id="btnShareWaStory">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.52 3.48A11.86 11.86 0 0 0 12.06 0C5.5 0 .16 5.34.16 11.9c0 2.1.55 4.15 1.6 5.96L0 24l6.33-1.66a11.86 11.86 0 0 0 5.73 1.46h.01c6.56 0 11.9-5.34 11.9-11.9 0-3.18-1.24-6.17-3.45-8.42zM12.07 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.76.99 1-3.66-.24-.38a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.89 9.9-9.89 2.64 0 5.13 1.03 7 2.9a9.83 9.83 0 0 1 2.9 7c0 5.46-4.44 9.89-9.89 9.89zm5.43-7.41c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35z"/>
          </svg>
          <span id="waStoryLbl">Share ke Story WhatsApp</span>
        </button>
        <button class="copy-link-btn" id="btnCopyLink">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
          </svg>
          <span id="copyLinkLbl">Salin Link</span>
        </button>
      </div>
    </div>

    <div class="sum-actions">
      <button class="sbtn"     id="sumBtn">Lanjut Berzikir ➜</button>
      <button class="sbtn-sec" id="resetTodayBtn">Reset Hari Ini</button>
    </div>
  </div>
</div>

<script>
"use strict";
// ══════════════════════════════════════════
// DAILY STORAGE SYSTEM
// ══════════════════════════════════════════
const STORAGE_KEY = 'zikir_daily_tracker_v2';

function getTodayKey(){
  const now = new Date();
  const y = now.getFullYear();
  const m = String(now.getMonth() + 1).padStart(2, '0');
  const d = String(now.getDate()).padStart(2, '0');
  return `${y}-${m}-${d}`;
}

const LOCALE_MAP = {
  id:'id-ID', en:'en-US', ar:'ar-SA', zh:'zh-CN', ko:'ko-KR',
  ja:'ja-JP', jv:'id-ID', tr:'tr-TR', ms:'ms-MY', es:'es-ES'
};

function getFormattedDate(l){
  const now = new Date();
  try{
    return now.toLocaleDateString(LOCALE_MAP[l] || 'id-ID', {
      weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
    });
  }catch(e){
    return now.toDateString();
  }
}

// ══════════════════════════════════════════
// STATE
// ══════════════════════════════════════════
const DHIKRS = [
  {arabic:'الحمد لله',           latin:'Alhamdulillah',   count:0, dailyTotal:0, target:33, sessions:0},
  {arabic:'سبحان الله',          latin:'Subhanallah',     count:0, dailyTotal:0, target:33, sessions:0},
  {arabic:'أَسْتَغْفِرُ اللَّهَ', latin:'Astagfirullah', count:0, dailyTotal:0, target:33, sessions:0},
];
let savedDate = getTodayKey();
let cur = 0;
let TM = 0;
let appRunning = false;
let W = 0, H = 0;
let soundOn = true, vibOn = true;
let audioCtx = null;
let lang = 'id';
let summaryTriggeredByCompletion = false;

let subhanFinaleActive = false;
let subhanDroneProgress = 0;

const LANG_ORDER = ['id','en','ar','zh','ko','ja','jv','tr','ms','es'];

// ══════════════════════════════════════════
// MULTI-LANGUAGE DATA (10 Languages)
// ══════════════════════════════════════════
const TXT = {
  id:{
    lang_label:'🌐 Pilih Bahasa',
    land_verse:'"Ingatlah, hanya dengan mengingat Allah hati menjadi tenteram."',
    verse_ref:"— QS. Ar-Ra'd: 28",
    start_btn:'✨ Bismillah, Mari Berzikir',
    tap_hint:'KETUK LAYAR',
    vib_on:'Getaran Aktif', vib_off:'Getaran Nonaktif',
    snd_on:'Suara Aktif',   snd_off:'Suara Nonaktif',
    daily_label:'Hari Ini:',
    land_pill:(n)=>`📿 Zikir Hari Ini: ${n.toLocaleString('id-ID')}×`,
    gt_label:'Total Seluruh Zikir Hari Ini',
    gt_sub:'Tersimpan otomatis • Direset setiap pergantian hari',
    sess_lbl:(s)=>`${s} putaran selesai`,
    sum_title:'MasyaAllah!',
    sum_title_recap:'Catatan Zikir Harian',
    sum_sub:'Zikirmu telah mengubah dunia. Semoga Allah menerima amalanmu. Aamiin 🤲',
    share_title:'✨ Yuk sebarkan link zikir ke temanmu, agar kebaikan terus menyebar!',
    wa_story_btn:'Share ke Story WhatsApp',
    copy_btn:'Salin Link',
    copied_toast:'Link zikir berhasil disalin! 📋',
    sum_btn:'Lanjut Berzikir ➜',
    sum_close:'Tutup',
    reset_btn:'Reset Hari Ini',
    reset_done:'Catatan zikir hari ini direset 🔄',
    scenes:[
      '🦋 Alhamdulillah — Pagi cerah & makhluk bermain penuh syukur',
      '🌌 Subhanallah — Aurora, fajar terbit, hingga semesta raya bertasbih',
      '🔥 Astagfirullah — Tiap istighfar memadamkan api',
    ],
    meanings:['"Segala puji bagi Allah"','"Maha Suci Allah"','"Aku memohon ampun kepada Allah"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah',  desc:'Total zikir syukur hari ini yang menyinari pagi & membahagiakan makhluk.'},
      {emoji:'🌌',name:'Subhanallah',    desc:'Total tasbih hari ini dari aurora, matahari terbit, hingga luasnya alam semesta.'},
      {emoji:'🌧️',name:'Astagfirullah',  desc:'Total istighfar hari ini memohon ampunan & rahmat Allah.'},
    ],
  },
  en:{
    lang_label:'🌐 Select Language',
    land_verse:'"Unquestionably, by the remembrance of Allah hearts are assured."',
    verse_ref:"— Surah Ar-Ra'd: 28",
    start_btn:"✨ Bismillah, Let's Begin",
    tap_hint:'TAP SCREEN',
    vib_on:'Vibration On', vib_off:'Vibration Off',
    snd_on:'Sound On',     snd_off:'Sound Off',
    daily_label:'Today:',
    land_pill:(n)=>`📿 Today's Dhikr: ${n.toLocaleString('en-US')}×`,
    gt_label:"Today's Total Dhikr",
    gt_sub:'Auto-saved • Resets automatically each new day',
    sess_lbl:(s)=>`${s} round${s===1?'':'s'} completed`,
    sum_title:'MasyaAllah!',
    sum_title_recap:'Daily Dhikr Record',
    sum_sub:'Your dhikr transformed the world. May Allah accept your deeds. Ameen 🤲',
    share_title:'✨ Share this dhikr link with your friends so goodness keeps spreading!',
    wa_story_btn:'Share to WhatsApp Story',
    copy_btn:'Copy Link',
    copied_toast:'Dhikr link copied! 📋',
    sum_btn:'Continue Dhikr ➜',
    sum_close:'Close',
    reset_btn:'Reset Today',
    reset_done:"Today's dhikr count has been reset 🔄",
    scenes:[
      "🦋 Alhamdulillah — Bright morning filled with joyful creatures",
      "🌌 Subhanallah — Aurora, sunrise, and the cosmos glorifying Allah",
      '🔥 Astagfirullah — Each istighfar extinguishes fire',
    ],
    meanings:['"All praise is due to Allah"','"Glory be to Allah"','"I seek forgiveness from Allah"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah',  desc:"Total gratitude dhikr today brightening the morning & creatures."},
      {emoji:'🌌',name:'Subhanallah',    desc:"Total glorification today from aurora and sunrise to the vast universe."},
      {emoji:'🌧️',name:'Astagfirullah',  desc:"Total istighfar today seeking Allah's forgiveness & mercy."},
    ],
  },
  ar:{
    lang_label:'🌐 اختر اللغة',
    land_verse:'«أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ» — فاذكروا الله يذكركم.',
    verse_ref:'— سورة الرعد: ٢٨',
    start_btn:'✨ بسم الله، لنبدأ الذكر',
    tap_hint:'المس الشاشة',
    vib_on:'الاهتزاز مفعل', vib_off:'الاهتزاز متوقف',
    snd_on:'الصوت مفعل',    snd_off:'الصوت متوقف',
    daily_label:'اليوم:',
    land_pill:(n)=>`📿 أذكار اليوم: ${n.toLocaleString('ar-SA')}×`,
    gt_label:'إجمالي أذكار اليوم',
    gt_sub:'يُحفظ تلقائياً • يتجدد كل يوم',
    sess_lbl:(s)=>`تمت ${s} دورة`,
    sum_title:'ما شاء الله!',
    sum_title_recap:'سجل الأذكار اليومي',
    sum_sub:'تقبل الله طاعتكم وبارك في أوقاتكم. آمين 🤲',
    share_title:'✨ شارك رابط الذكر مع أصدقائك لينتشر الخير والأجر!',
    wa_story_btn:'مشاركة في حالة واتساب',
    copy_btn:'نسخ الرابط',
    copied_toast:'تم نسخ رابط الذكر! 📋',
    sum_btn:'متابعة الذكر ➜',
    sum_close:'إغلاق',
    reset_btn:'إعادة ضبط اليوم',
    reset_done:'تمت إعادة ضبط عداد اليوم 🔄',
    scenes:[
      '🦋 الحمد لله — صباح مشرق ومخلوقات تسبح بحمد الله',
      '🌌 سبحان الله — الشفق والشروق وعظمة الكون الفسيح',
      '🔥 أستغفر الله — كل استغفار يطفئ نار الذنوب',
    ],
    meanings:['"الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"','"سُبْحَانَ اللَّهِ وَبِحَمْدِهِ"','"أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ"'],
    impacts:[
      {emoji:'🦋',name:'الحمد لله',   desc:'مجموع التحميد والشكر لله في هذا اليوم.'},
      {emoji:'🌌',name:'سبحان الله',  desc:'مجموع التسبيح وتنزيه الله في هذا اليوم.'},
      {emoji:'🌧️',name:'أستغفر الله', desc:'مجموع الاستغفار وطلب المغفرة في هذا اليوم.'},
    ],
  },
  zh:{
    lang_label:'🌐 选择语言',
    land_verse:'“真的，一切心境因记忆真主而安宁。”',
    verse_ref:'— 《古兰经》雷霆章 13:28',
    start_btn:'✨ 奉真主之名，开始记念',
    tap_hint:'点击屏幕',
    vib_on:'震动开启', vib_off:'震动关闭',
    snd_on:'音效开启', snd_off:'音效关闭',
    daily_label:'今日:',
    land_pill:(n)=>`📿 今日记主: ${n.toLocaleString('zh-CN')}×`,
    gt_label:'今日记主总次数',
    gt_sub:'自动保存 • 每日自动重置',
    sess_lbl:(s)=>`已完成 ${s} 轮`,
    sum_title:'真主意欲！',
    sum_title_recap:'每日记主记录',
    sum_sub:'愿真主接纳你的善功与记念。阿米乃 🤲',
    share_title:'✨ 将记主链接分享给朋友，让善意不断传递！',
    wa_story_btn:'分享到 WhatsApp 动态',
    copy_btn:'复制链接',
    copied_toast:'链接已复制！📋',
    sum_btn:'继续记主 ➜',
    sum_close:'关闭',
    reset_btn:'重置今日',
    reset_done:'今日记录已重置 🔄',
    scenes:[
      '🦋 Alhamdulillah — 明媚清晨，万物感恩',
      '🌌 Subhanallah — 极光、日出与浩瀚宇宙赞颂真主',
      '🔥 Astagfirullah — 每一声求饶熄灭火焰',
    ],
    meanings:['“一切赞颂全归真主”','“赞颂真主超绝万物”','“我向真主求饶”'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'今日感恩赞颂总次数。'},
      {emoji:'🌌',name:'Subhanallah',   desc:'今日赞主超绝总次数。'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'今日向主求饶总次数。'},
    ],
  },
  ko:{
    lang_label:'🌐 언어 선택',
    land_verse:'"실로 하나님을 기억함으로써 마음이 평온해지느니라."',
    verse_ref:'— 꾸란 13장 28절',
    start_btn:'✨ 비스밀라, 디크르 시작하기',
    tap_hint:'화면을 탭하세요',
    vib_on:'진동 켜짐', vib_off:'진동 꺼짐',
    snd_on:'소리 켜짐', snd_off:'소리 꺼짐',
    daily_label:'오늘:',
    land_pill:(n)=>`📿 오늘의 디크르: ${n.toLocaleString('ko-KR')}×`,
    gt_label:'오늘 총 디크르 횟수',
    gt_sub:'자동 저장 • 매일 자정 자동 초기화',
    sess_lbl:(s)=>`${s}회 완료`,
    sum_title:'마샤알라!',
    sum_title_recap:'오늘의 디크르 기록',
    sum_sub:'당신의 디크르가 세상을 밝힙니다. 하나님께서 받아주시길 바랍니다. 아민 🤲',
    share_title:'✨ 친구들에게 디크르 링크를 공유해 선행을 널리 퍼뜨려 보세요!',
    wa_story_btn:'WhatsApp 스토리에 공유',
    copy_btn:'링크 복사',
    copied_toast:'링크가 복사되었습니다! 📋',
    sum_btn:'계속하기 ➜',
    sum_close:'닫기',
    reset_btn:'오늘 초기화',
    reset_done:'오늘의 기록이 초기화되었습니다 🔄',
    scenes:[
      '🦋 Alhamdulillah — 감사로 가득한 화창한 아침',
      '🌌 Subhanallah — 오로라와 일출, 광활한 우주의 찬미',
      '🔥 Astagfirullah — 용서를 구할 때마다 불길이 꺼집니다',
    ],
    meanings:['"모든 찬미는 하나님께"','"하나님께 영광을"','"하나님께 용서를 구합니다"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'오늘 바친 감사의 디크르 합계입니다.'},
      {emoji:'🌌',name:'Subhanallah',   desc:'오늘 바친 찬미의 디크르 합계입니다.'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'오늘 바친 용서의 디크르 합계입니다.'},
    ],
  },
  ja:{
    lang_label:'🌐 言語を選択',
    land_verse:'「実にアッラーを念ずることによってこそ、心は安らぎを得る。」',
    verse_ref:'— クルアーン 雷電章 13:28',
    start_btn:'✨ ビスミッラー、ズィクルを始める',
    tap_hint:'画面をタップ',
    vib_on:'バイブ ON', vib_off:'バイブ OFF',
    snd_on:'サウンド ON', snd_off:'サウンド OFF',
    daily_label:'今日:',
    land_pill:(n)=>`📿 今日のズィクル: ${n.toLocaleString('ja-JP')}×`,
    gt_label:'今日の合計ズィクル数',
    gt_sub:'自動保存 • 毎日自動でリセット',
    sess_lbl:(s)=>`${s} ラウンド完了`,
    sum_title:'マーシャアッラー！',
    sum_title_recap:'毎日のズィクル記録',
    sum_sub:'あなたのズィクルが世界を照らします。アッラーが受け入れてくださいますように。アーミーン 🤲',
    share_title:'✨ 友達にズィクルのリンクをシェアして、善行の輪を広げよう！',
    wa_story_btn:'WhatsAppストーリーで共有',
    copy_btn:'リンクをコピー',
    copied_toast:'リンクをコピーしました！📋',
    sum_btn:'ズィクルを続ける ➜',
    sum_close:'閉じる',
    reset_btn:'今日をリセット',
    reset_done:'今日の記録をリセットしました 🔄',
    scenes:[
      '🦋 Alhamdulillah — 感謝に満ちた爽やかな朝',
      '🌌 Subhanallah — オーロラと日の出、広大な宇宙の賛美',
      '🔥 Astagfirullah — 赦しを請うたびに炎が消える',
    ],
    meanings:['「すべての賛美はアッラーに属す」','「アッラーに栄光あれ」','「アッラーにお赦しを請います」'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'今日の感謝のズィクル合計回数。'},
      {emoji:'🌌',name:'Subhanallah',   desc:'今日の賛美のズィクル合計回数。'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'今日の赦しを請うズィクル合計回数。'},
    ],
  },
  jv:{
    lang_label:'🌐 Pilih Basa',
    land_verse:'"Elinga, mung kanthi eling marang Gusti Allah ati dadi ayem tentrem."',
    verse_ref:"— QS. Ar-Ra'd: 28",
    start_btn:'✨ Bismillah, Ayo Dzikir',
    tap_hint:'TUTUK LAYAR',
    vib_on:'Geter Urip', vib_off:'Geter Mati',
    snd_on:'Swara Urip', snd_off:'Swara Mati',
    daily_label:'Dina Iki:',
    land_pill:(n)=>`📿 Dzikir Dina Iki: ${n.toLocaleString('id-ID')}×`,
    gt_label:'Gunggung Dzikir Dina Iki',
    gt_sub:'Kasimpen otomatis • Direset saben ganti dina',
    sess_lbl:(s)=>`${s} ubengan rampung`,
    sum_title:'MasyaAllah!',
    sum_title_recap:'Cathetan Dzikir Saben Dina',
    sum_sub:'Dzikirmu wis madhangi donya. Muga-muga Gusti Allah nampa amalmu. Aamiin 🤲',
    share_title:'✨ Ayo sebarake link dzikir iki marang kancamu, supaya kabecikan terus sumebar!',
    wa_story_btn:'Share menyang Story WhatsApp',
    copy_btn:'Salin Link',
    copied_toast:'Link dzikir wis disalin! 📋',
    sum_btn:'Terusake Dzikir ➜',
    sum_close:'Tutup',
    reset_btn:'Reset Dina Iki',
    reset_done:'Cathetan dzikir dina iki direset 🔄',
    scenes:[
      '🦋 Alhamdulillah — Esuk padhang & kewan dolanan kebak rasa syukur',
      '🌌 Subhanallah — Aurora, srengenge mlethek, nganti jagad raya tasbih',
      '🔥 Astagfirullah — Saben istighfar nyirepake geni',
    ],
    meanings:['"Kabeh puji kagunganipun Gusti Allah"','"Maha Suci Gusti Allah"','"Kula nyuwun pangapura dhumateng Gusti Allah"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'Gunggung dzikir syukur dina iki sing madhangi esuk.'},
      {emoji:'🌌',name:'Subhanallah',   desc:'Gunggung tasbih dina iki muji kaendahan jagad raya.'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'Gunggung istighfar dina iki nyuwun pangapura Allah.'},
    ],
  },
  tr:{
    lang_label:'🌐 Dil Seçin',
    land_verse:'"Bilesiniz ki, kalpler ancak Allah’ı anmakla huzur bulur."',
    verse_ref:"— Ra'd Suresi: 28",
    start_btn:'✨ Bismillah, Zikre Başla',
    tap_hint:'EKRANA DOKUN',
    vib_on:'Titreşim Açık', vib_off:'Titreşim Kapalı',
    snd_on:'Ses Açık',       snd_off:'Ses Kapalı',
    daily_label:'Bugün:',
    land_pill:(n)=>`📿 Bugünkü Zikir: ${n.toLocaleString('tr-TR')}×`,
    gt_label:'Bugünkü Toplam Zikir',
    gt_sub:'Otomatik kaydedilir • Her yeni günde sıfırlanır',
    sess_lbl:(s)=>`${s} tur tamamlandı`,
    sum_title:'Maşallah!',
    sum_title_recap:'Günlük Zikir Kaydı',
    sum_sub:'Zikrin dünyayı güzelleştirdi. Allah ibadetlerini kabul etsin. Amin 🤲',
    share_title:'✨ İyiliğin yayılması için bu zikir bağlantısını arkadaşlarınla paylaş!',
    wa_story_btn:"WhatsApp Hikayesi'nde Paylaş",
    copy_btn:'Bağlantıyı Kopyala',
    copied_toast:'Zikir bağlantısı kopyalandı! 📋',
    sum_btn:'Zikre Devam Et ➜',
    sum_close:'Kapat',
    reset_btn:'Bugünü Sıfırla',
    reset_done:'Bugünkü zikir sayacı sıfırlandı 🔄',
    scenes:[
      '🦋 Alhamdulillah — Şükür dolu aydınlık bir sabah',
      '🌌 Subhanallah — Aurora, gün doğumu ve evrenin tesbihi',
      '🔥 Astagfirullah — Her istiğfar ateşi söndürür',
    ],
    meanings:['"Hamd Allah’a mahsustur"','"Allah her türlü eksiklikten uzaktır"','"Allah’tan bağışlanma dilerim"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'Bugün çekilen toplam şükür zikri.'},
      {emoji:'🌌',name:'Subhanallah',   desc:'Bugün çekilen toplam tesbih zikri.'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'Bugün çekilen toplam istiğfar zikri.'},
    ],
  },
  ms:{
    lang_label:'🌐 Pilih Bahasa',
    land_verse:'"Ketahuilah dengan mengingati Allah itu, tenang tenteramlah hati manusia."',
    verse_ref:"— Surah Ar-Ra'd: 28",
    start_btn:'✨ Bismillah, Mari Berzikir',
    tap_hint:'KETIK SKRIN',
    vib_on:'Getaran Aktif', vib_off:'Getaran Nyahaktif',
    snd_on:'Bunyi Aktif',   snd_off:'Bunyi Nyahaktif',
    daily_label:'Hari Ini:',
    land_pill:(n)=>`📿 Zikir Hari Ini: ${n.toLocaleString('ms-MY')}×`,
    gt_label:'Jumlah Zikir Hari Ini',
    gt_sub:'Disimpan automatik • Ditetapkan semula setiap hari',
    sess_lbl:(s)=>`${s} pusingan selesai`,
    sum_title:'MasyaAllah!',
    sum_title_recap:'Rekod Zikir Harian',
    sum_sub:'Zikirmu menyinari dunia. Semoga Allah menerima amalanmu. Aamiin 🤲',
    share_title:'✨ Jom kongsikan pautan zikir ini kepada rakanmu agar kebaikan terus tersebar!',
    wa_story_btn:'Kongsi ke Story WhatsApp',
    copy_btn:'Salin Pautan',
    copied_toast:'Pautan zikir berjaya disalin! 📋',
    sum_btn:'Teruskan Berzikir ➜',
    sum_close:'Tutup',
    reset_btn:'Set Semula Hari Ini',
    reset_done:'Rekod zikir hari ini telah ditetapkan semula 🔄',
    scenes:[
      '🦋 Alhamdulillah — Pagi cerah & makhluk bermain penuh syukur',
      '🌌 Subhanallah — Aurora, fajar terbit hingga alam semesta bertasbih',
      '🔥 Astagfirullah — Setiap istighfar memadamkan api',
    ],
    meanings:['"Segala puji bagi Allah"','"Maha Suci Allah"','"Aku memohon keampunan kepada Allah"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'Jumlah zikir syukur hari ini.'},
      {emoji:'🌌',name:'Subhanallah',   desc:'Jumlah tasbih hari ini memuji kebesaran Allah.'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'Jumlah istighfar hari ini memohon keampunan Allah.'},
    ],
  },
  es:{
    lang_label:'🌐 Elegir Idioma',
    land_verse:'"¿Acaso no es con el recuerdo de Alá con lo que se tranquilizan los corazones?"',
    verse_ref:"— Corán, Sura Ar-Ra'd: 28",
    start_btn:'✨ Bismillah, Comenzar Dhikr',
    tap_hint:'TOCA LA PANTALLA',
    vib_on:'Vibración Activada', vib_off:'Vibración Desactivada',
    snd_on:'Sonido Activado',    snd_off:'Sonido Desactivado',
    daily_label:'Hoy:',
    land_pill:(n)=>`📿 Dhikr de Hoy: ${n.toLocaleString('es-ES')}×`,
    gt_label:'Total de Dhikr Hoy',
    gt_sub:'Guardado automático • Se reinicia cada nuevo día',
    sess_lbl:(s)=>`${s} ronda${s===1?'':'s'} completada${s===1?'':'s'}`,
    sum_title:'¡MashaAllah!',
    sum_title_recap:'Registro Diario de Dhikr',
    sum_sub:'Tu dhikr ilumina el mundo. Que Alá acepte tus buenas obras. Amén 🤲',
    share_title:'✨ ¡Comparte este enlace de dhikr con tus amigos para que el bien se siga difundiendo!',
    wa_story_btn:'Compartir en Historia de WhatsApp',
    copy_btn:'Copiar Enlace',
    copied_toast:'¡Enlace de dhikr copiado! 📋',
    sum_btn:'Continuar Dhikr ➜',
    sum_close:'Cerrar',
    reset_btn:'Reiniciar Hoy',
    reset_done:'El contador de hoy se ha reiniciado 🔄',
    scenes:[
      '🦋 Alhamdulillah — Mañana radiante llena de gratitud',
      '🌌 Subhanallah — Aurora, amanecer y el universo glorificando a Alá',
      '🔥 Astagfirullah — Cada istighfar apaga el fuego',
    ],
    meanings:['"Toda alabanza pertenece a Alá"','"Gloria a Alá"','"Pido perdón a Alá"'],
    impacts:[
      {emoji:'🦋',name:'Alhamdulillah', desc:'Total de dhikr de gratitud realizado hoy.'},
      {emoji:'🌌',name:'Subhanallah',   desc:'Total de glorificación realizado hoy.'},
      {emoji:'🌧️',name:'Astagfirullah', desc:'Total de súplicas de perdón realizadas hoy.'},
    ],
  }
};

function loadDailyData(){
  try{
    const raw = localStorage.getItem(STORAGE_KEY);
    const today = getTodayKey();
    if(!raw){
      savedDate = today;
      saveDailyData();
      return;
    }
    const data = JSON.parse(raw);
    if(data.date !== today){
      savedDate = today;
      DHIKRS.forEach(d => { d.count = 0; d.dailyTotal = 0; d.sessions = 0; });
      if(data.lang && TXT[data.lang]) lang = data.lang;
      if(typeof data.soundOn === 'boolean') soundOn = data.soundOn;
      if(typeof data.vibOn === 'boolean') vibOn = data.vibOn;
      if(data.target) DHIKRS.forEach(d => d.target = data.target);
      saveDailyData();
    } else {
      savedDate = today;
      if(Array.isArray(data.items)){
        data.items.forEach((item, idx) => {
          if(DHIKRS[idx]){
            DHIKRS[idx].count = Number(item.count) || 0;
            DHIKRS[idx].dailyTotal = Number(item.dailyTotal) || 0;
            DHIKRS[idx].sessions = Number(item.sessions) || 0;
            DHIKRS[idx].target = Number(item.target) || 33;
          }
        });
      }
      if(typeof data.cur === 'number' && DHIKRS[data.cur]) cur = data.cur;
      if(data.lang && TXT[data.lang]) lang = data.lang;
      if(typeof data.soundOn === 'boolean') soundOn = data.soundOn;
      if(typeof data.vibOn === 'boolean') vibOn = data.vibOn;
    }
  }catch(e){}
}

function saveDailyData(){
  try{
    const today = getTodayKey();
    if(savedDate !== today){
      savedDate = today;
      DHIKRS.forEach(d => { d.count = 0; d.dailyTotal = 0; d.sessions = 0; });
    }
    const payload = {
      date: savedDate,
      cur,
      lang,
      soundOn,
      vibOn,
      target: DHIKRS[0].target,
      items: DHIKRS.map(d => ({
        count: d.count,
        dailyTotal: d.dailyTotal,
        sessions: d.sessions,
        target: d.target
      }))
    };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
  }catch(e){}
}

function checkDayRollover(){
  const today = getTodayKey();
  if(savedDate !== today){
    savedDate = today;
    DHIKRS.forEach(d => { d.count = 0; d.dailyTotal = 0; d.sessions = 0; });
    saveDailyData();
    resetSceneEntities();
    updateUI();
  }
}

function getGrandDailyTotal(){
  return DHIKRS.reduce((sum, d) => sum + d.dailyTotal, 0);
}

// ══════════════════════════════════════════
// HELPERS
// ══════════════════════════════════════════
const lerp  = (a,b,t) => a + (b-a)*Math.min(1,Math.max(0,t));
const clamp = (v,lo,hi) => Math.min(hi,Math.max(lo,v));
const rand  = (a,b) => a + Math.random()*(b-a);
const smoothstep = (e0,e1,x) => {
  const t = clamp((x - e0) / (e1 - e0), 0, 1);
  return t * t * (3 - 2 * t);
};

// ══════════════════════════════════════════
// LANGUAGE FUNCTIONS
// ══════════════════════════════════════════
function applyDhikrTexts(){
  const d = DHIKRS[cur];
  const tx = TXT[lang] || TXT.id;
  document.getElementById('dAr').textContent   = d.arabic;
  document.getElementById('dLat').textContent  = d.latin;
  document.getElementById('dMean').textContent = tx.meanings[cur];
  document.getElementById('tapHint').textContent = tx.tap_hint;
  document.getElementById('sLbl').textContent  = tx.scenes[cur];
}

function applyLang(){
  const tx = TXT[lang] || TXT.id;
  document.getElementById('langBoxLbl').textContent  = tx.lang_label;
  document.getElementById('ls').textContent          = tx.land_verse;
  document.getElementById('vRef').textContent        = tx.verse_ref;
  document.getElementById('startBtn').textContent    = tx.start_btn;
  document.getElementById('dailyLabel').textContent  = tx.daily_label;
  document.getElementById('gtLabel').textContent     = tx.gt_label;
  document.getElementById('gtSub').textContent       = tx.gt_sub;
  document.getElementById('sumSub').textContent      = tx.sum_sub;
  document.getElementById('shareTitle').textContent  = tx.share_title;
  document.getElementById('waStoryLbl').textContent  = tx.wa_story_btn;
  document.getElementById('copyLinkLbl').textContent = tx.copy_btn;
  document.getElementById('resetTodayBtn').textContent = tx.reset_btn;

  document.getElementById('langSelect').value = lang;
  document.querySelectorAll('#langGrid .lbtn').forEach(btn => {
    btn.classList.toggle('on', btn.dataset.lang === lang);
  });

  applyDhikrTexts();
  updateDailyCountersUI();
}

function setLang(l){
  if(!TXT[l]) return;
  lang = l;
  saveDailyData();
  applyLang();
}

function toggleLang(){
  const idx = LANG_ORDER.indexOf(lang);
  const next = LANG_ORDER[(idx + 1) % LANG_ORDER.length];
  setLang(next);
  const opt = document.querySelector(`#langSelect option[value="${next}"]`);
  if(opt) showToast(opt.textContent);
}

// ══════════════════════════════════════════
// SHARE TO WHATSAPP STORY & COPY LINK
// ══════════════════════════════════════════
function getShareMessage(){
  const total = getGrandDailyTotal();
  const locale = LOCALE_MAP[lang] || 'id-ID';
  const pageUrl = window.location.href.startsWith('http') ? window.location.href : 'https://dhikr-tracker.app';
  if(lang === 'en'){
    return `✨ Alhamdulillah! Today I completed ${total.toLocaleString(locale)}× dhikr on *Dhikr Tracker by hafizh.arz* 🌙\n\n"Unquestionably, by the remembrance of Allah hearts are assured." (QS. Ar-Ra'd: 28)\n\nLet's remember Allah together:\n${pageUrl}`;
  }
  return `✨ Alhamdulillah! Hari ini aku sudah berzikir sebanyak *${total.toLocaleString(locale)}×* di *Dhikr Tracker by hafizh.arz* 🌙\n\n"Ingatlah, hanya dengan mengingat Allah hati menjadi tenteram." (QS. Ar-Ra'd: 28)\n\nYuk ikut berzikir bersama & sebarkan kebaikan:\n${pageUrl}`;
}

function shareToWhatsAppStory(){
  const text = encodeURIComponent(getShareMessage());
  const waUrl = `https://api.whatsapp.com/send?text=${text}`;
  window.open(waUrl, '_blank', 'noopener,noreferrer');
}

function copyShareLink(){
  const msg = getShareMessage();
  if(navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(msg).then(()=>{
      showToast((TXT[lang] || TXT.id).copied_toast);
    }).catch(()=>{
      fallbackCopy(msg);
    });
  } else {
    fallbackCopy(msg);
  }
}

function fallbackCopy(text){
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.select();
  try{ document.execCommand('copy'); }catch(e){}
  document.body.removeChild(ta);
  showToast((TXT[lang] || TXT.id).copied_toast);
}

// ══════════════════════════════════════════
// AUDIO
// ══════════════════════════════════════════
function getActx(){
  if(!audioCtx) audioCtx = new (window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==='suspended') audioCtx.resume();
  return audioCtx;
}
function playTone(freq, type, dur, vol, freqEnd){
  if(!soundOn) return;
  try{
    const ac=getActx(), osc=ac.createOscillator(), gain=ac.createGain(), now=ac.currentTime;
    osc.connect(gain); gain.connect(ac.destination);
    osc.type=type; osc.frequency.setValueAtTime(freq,now);
    if(freqEnd) osc.frequency.exponentialRampToValueAtTime(freqEnd,now+dur*.7);
    gain.gain.setValueAtTime(0,now);
    gain.gain.linearRampToValueAtTime(vol||.18,now+.04);
    gain.gain.exponentialRampToValueAtTime(.0001,now+dur);
    osc.start(now); osc.stop(now+dur+.05);
  }catch(e){}
}
function playChord(freqs,type,dur,vol){ freqs.forEach(f=>playTone(f,type,dur,vol)); }
function playSound(idx){
  if(!soundOn) return;
  if(idx===0){ playTone(528,'sine',1.4,.18); setTimeout(()=>playTone(660,'sine',1.0,.10),100); setTimeout(()=>playTone(396,'sine',1.8,.08),200); }
  else if(idx===1){ playChord([432,648,864],'sine',2.5,.10); setTimeout(()=>playChord([396,528],'sine',2.0,.07),300); }
  else{ playTone(900,'sine',.18,.20,200); setTimeout(()=>playTone(500,'sine',.6,.12,150),160); setTimeout(()=>playTone(300,'sine',.9,.08,180),300); }
}

function syncControlButtons(){
  const bs = document.getElementById('btnSnd');
  bs.classList.toggle('on', soundOn);
  document.getElementById('iconSndOn').style.display  = soundOn ? 'block' : 'none';
  document.getElementById('iconSndOff').style.display = soundOn ? 'none'  : 'block';

  const bv = document.getElementById('btnVib');
  bv.classList.toggle('on', vibOn);

  const t = DHIKRS[0].target;
  document.getElementById('trg33').classList.toggle('on', t===33);
  document.getElementById('trg99').classList.toggle('on', t===99);
  document.querySelectorAll('.tab').forEach((tabEl, i) => tabEl.classList.toggle('on', i===cur));
}

function toggleSnd(){
  soundOn = !soundOn;
  syncControlButtons();
  saveDailyData();
  const tx = TXT[lang] || TXT.id;
  showToast(tx[soundOn?'snd_on':'snd_off']);
}

// ══════════════════════════════════════════
// VIBRATION
// ══════════════════════════════════════════
function vib(p){ if(vibOn && navigator.vibrate) navigator.vibrate(p); }
function toggleVib(){
  vibOn = !vibOn;
  syncControlButtons();
  saveDailyData();
  const tx = TXT[lang] || TXT.id;
  showToast(tx[vibOn?'vib_on':'vib_off']);
  if(vibOn) vib([20,30,20]);
}

// ══════════════════════════════════════════
// LANDING CANVAS
// ══════════════════════════════════════════
(function initLanding(){
  const lc = document.getElementById('lc');
  const lx = lc.getContext('2d');
  let lw, lh, lstars = [], lparts = [];
  function lresize(){
    lw = lc.width  = window.innerWidth;
    lh = lc.height = window.innerHeight;
    lstars = Array.from({length:150}, ()=>({
      x:rand(0,lw), y:rand(0,lh), r:rand(.3,1.6),
      a:rand(0,Math.PI*2), sp:rand(.003,.01)
    }));
  }
  window.addEventListener('resize', lresize);
  lresize();
  let lt = 0;
  function ldraw(){
    const landing = document.getElementById('landing');
    if(!landing.classList.contains('hide')){
      lt += .014;
      lx.clearRect(0,0,lw,lh);
      const bg = lx.createLinearGradient(0,0,0,lh);
      bg.addColorStop(0,'#070d1f');
      bg.addColorStop(.5,'#0d1830');
      bg.addColorStop(1,'#070d1f');
      lx.fillStyle = bg; lx.fillRect(0,0,lw,lh);
      lstars.forEach(s=>{
        s.a += s.sp;
        const al = (Math.sin(s.a)+1)/2*.8+.1;
        lx.beginPath(); lx.arc(s.x,s.y,s.r,0,Math.PI*2);
        lx.fillStyle = `rgba(212,168,83,${al})`; lx.fill();
      });
      if(Math.random()<.12) lparts.push({x:rand(lw*.1,lw*.9),y:lh+10,vx:rand(-.3,.3),vy:rand(-1.2,-.5),r:rand(1.5,3.5),a:0,hue:rand(30,60)});
      lparts = lparts.filter(p=>{
        p.x += p.vx; p.y += p.vy; p.a = Math.min(1,p.a+.04);
        lx.globalAlpha = p.a; lx.fillStyle = `hsl(${p.hue},80%,65%)`;
        lx.beginPath(); lx.arc(p.x,p.y,p.r,0,Math.PI*2); lx.fill();
        lx.globalAlpha = 1; return p.y > -10;
      });
      const cg = lx.createRadialGradient(lw/2,lh/2,0,lw/2,lh/2,lw*.35);
      cg.addColorStop(0,`rgba(240,201,122,${.06+Math.sin(lt*.5)*.02})`);
      cg.addColorStop(1,'rgba(0,0,0,0)');
      lx.fillStyle = cg; lx.fillRect(0,0,lw,lh);
    }
    requestAnimationFrame(ldraw);
  }
  ldraw();
})();

// ══════════════════════════════════════════
// TRANSITION
// ══════════════════════════════════════════
function startApp(){
  checkDayRollover();
  try{ getActx(); }catch(e){}
  const ld = document.getElementById('landing');
  const ap = document.getElementById('app');
  ld.classList.add('hide');
  requestAnimationFrame(()=>{
    requestAnimationFrame(()=>{
      ap.classList.add('show');
    });
  });
  appRunning = true;
}

function goHome(){
  updateDailyCountersUI();
  const ld = document.getElementById('landing');
  const ap = document.getElementById('app');
  ap.classList.remove('show');
  appRunning = false;
  setTimeout(()=>{
    ld.classList.remove('hide');
  }, 400);
}

// ══════════════════════════════════════════
// MAIN CANVAS
// ══════════════════════════════════════════
const canvas = document.getElementById('c');
const ctx    = canvas.getContext('2d');
function resize(){
  W = canvas.width  = window.innerWidth;
  H = canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

// ══════════════════════════════════════════
// SCENE 0 — ALHAMDULILLAH: Bright Grateful Morning
// ══════════════════════════════════════════
let animals=[], butterflies=[], foodPellets=[], sceneFlowers=[];

function spawnAnimal(forceType){
  const types = ['bird','bird','rabbit','rabbit','kancil','kancil'];
  const type  = forceType || types[Math.floor(rand(0,types.length))];
  animals.push({
    type,
    x: rand(W*.06,W*.94),
    dir: Math.random()<.5 ? 1 : -1,
    size: type==='kancil' ? rand(.85,1.25) : rand(.85,1.3),
    munch: 0,
    munchTimer: rand(.5,3),
    hue: type==='bird' ? rand(180,360) : rand(24,42),
    wingPhase: rand(0,Math.PI*2),
    flyH: type==='bird' ? rand(H*.18,H*.52) : 0,
    flyAmp: rand(8,18),
    flySpd: rand(.6,1.1),
    hopTimer: rand(.8,3.2),
    hopPhase: 0,
    isHopping: false,
    walkTimer: rand(1.5,4.5),
    isWalking: Math.random()<.6,
  });
}

function spawnButterfly(){
  const palettes = [340, 42, 195, 285, 22, 52];
  butterflies.push({
    x: rand(W*.05, W*.95),
    y: rand(H*.36, H*.71),
    baseY: rand(H*.38, H*.70),
    dir: Math.random()<.5 ? 1 : -1,
    vx: rand(.35, .85),
    wingPhase: rand(0, Math.PI*2),
    wingSpeed: rand(.16, .24),
    floatPhase: rand(0, Math.PI*2),
    size: rand(.75, 1.25),
    hue: palettes[Math.floor(rand(0, palettes.length))],
  });
}

function spawnFood(x,y){
  for(let i=0;i<6;i++)
    foodPellets.push({x:x+rand(-60,60),y:rand(-20,0),vy:rand(2,5),vx:rand(-1,1),a:1,r:rand(2,4),hue:rand(32,55)});
}

function spawnFlower0(){
  const gy = H*.73;
  sceneFlowers.push({x:rand(W*.02,W*.98),y:gy+rand(-4,18),hue:Math.round(rand(0,360)),size:rand(.65,1.35),stemH:0,maxH:rand(18,46),bloom:0,phase:rand(0,Math.PI*2)});
}

function drawScene0(p){
  const gy = H*.73;

  const sky = ctx.createLinearGradient(0,0,0,gy);
  if(p < 0.45){
    const q = p / 0.45;
    sky.addColorStop(0,   `hsl(${lerp(235,212,q)|0}, ${lerp(42,68,q)|0}%, ${lerp(11,34,q)|0}%)`);
    sky.addColorStop(0.55,`hsl(${lerp(225,32,q)|0},  ${lerp(35,78,q)|0}%, ${lerp(15,48,q)|0}%)`);
    sky.addColorStop(1,   `hsl(${lerp(215,38,q)|0},  ${lerp(28,88,q)|0}%, ${lerp(20,62,q)|0}%)`);
  } else {
    const q = (p - 0.45) / 0.55;
    sky.addColorStop(0,   `hsl(${lerp(212,202,q)|0}, ${lerp(68,86,q)|0}%, ${lerp(34,56,q)|0}%)`);
    sky.addColorStop(0.58,`hsl(${lerp(32,197,q)|0},  ${lerp(78,84,q)|0}%, ${lerp(48,74,q)|0}%)`);
    sky.addColorStop(1,   `hsl(${lerp(38,52,q)|0},   ${lerp(88,92,q)|0}%, ${lerp(62,86,q)|0}%)`);
  }
  ctx.fillStyle = sky;
  ctx.fillRect(0,0,W,H);

  if(p > .02){
    const sa = Math.min(1, p * 2.2);
    const sx = W * .78;
    const sy = lerp(H * .24, H * .14, p);
    const sunR = lerp(20, 32, p);

    ctx.save();
    const halo = ctx.createRadialGradient(sx,sy,sunR*.4,sx,sy,sunR*5.5);
    halo.addColorStop(0, `rgba(255,248,195,${.48*sa*p})`);
    halo.addColorStop(0.45, `rgba(255,220,115,${.22*sa*p})`);
    halo.addColorStop(1, 'rgba(255,220,115,0)');
    ctx.fillStyle = halo;
    ctx.beginPath(); ctx.arc(sx,sy,sunR*5.5,0,Math.PI*2); ctx.fill();

    ctx.globalAlpha = sa * (.45 + .45*p);
    for(let r=0; r<14; r++){
      const a = (r/14)*Math.PI*2 + TM*.18;
      const rIn = sunR + 6;
      const rOut = sunR + lerp(18, 42, p) + Math.sin(TM*2+r)*4;
      ctx.strokeStyle = 'rgba(255,242,150,.55)';
      ctx.lineWidth = 2.2;
      ctx.beginPath();
      ctx.moveTo(sx+Math.cos(a)*rIn, sy+Math.sin(a)*rIn);
      ctx.lineTo(sx+Math.cos(a)*rOut, sy+Math.sin(a)*rOut);
      ctx.stroke();
    }

    ctx.globalAlpha = sa;
    const sg = ctx.createRadialGradient(sx,sy,0,sx,sy,sunR);
    sg.addColorStop(0, 'rgba(255,255,235,1)');
    sg.addColorStop(0.7, 'rgba(255,230,110,.98)');
    sg.addColorStop(1, 'rgba(255,190,45,.88)');
    ctx.fillStyle = sg;
    ctx.beginPath(); ctx.arc(sx,sy,sunR,0,Math.PI*2); ctx.fill();
    ctx.restore();
  }

  if(p > .08){
    const ca = Math.min(.92, (p-.08)/.35);
    const drift1 = Math.sin(TM*.08)*14;
    const drift2 = Math.cos(TM*.06)*18;
    drawCloud(W*.20 + drift1, H*.13, 110, 40, ca, p);
    drawCloud(W*.56 + drift2, H*.09, 132, 46, ca, p);
    if(p > .45){
      const ca2 = Math.min(.85, (p-.45)/.35);
      drawCloud(W*.86 - drift1, H*.22, 92, 34, ca2, p);
    }
  }

  if(p > .15){
    const ha = Math.min(1, (p-.15)/.45);
    ctx.save();
    ctx.globalAlpha = ha;
    ctx.fillStyle = `hsl(118, ${lerp(30,52,p)|0}%, ${lerp(22,42,p)|0}%)`;
    ctx.beginPath();
    ctx.moveTo(0, gy);
    ctx.quadraticCurveTo(W*.25, gy - H*.085, W*.52, gy - H*.02);
    ctx.quadraticCurveTo(W*.78, gy - H*.095, W, gy - H*.015);
    ctx.lineTo(W, gy+4);
    ctx.lineTo(0, gy+4);
    ctx.fill();
    ctx.restore();
  }

  const gg = ctx.createLinearGradient(0,gy,0,H);
  gg.addColorStop(0, `hsl(104, ${lerp(24,68,p)|0}%, ${lerp(16,44,p)|0}%)`);
  gg.addColorStop(0.5, `hsl(98, ${lerp(20,62,p)|0}%, ${lerp(13,34,p)|0}%)`);
  gg.addColorStop(1, `hsl(92, ${lerp(16,52,p)|0}%, ${lerp(10,24,p)|0}%)`);
  ctx.fillStyle = gg;
  ctx.fillRect(0,gy,W,H-gy);

  if(p > .5){
    const sunWash = (p - .5) / .5;
    const wg = ctx.createLinearGradient(W*.8, gy, W*.1, H);
    wg.addColorStop(0, `rgba(255,245,165,${.24*sunWash})`);
    wg.addColorStop(1, 'rgba(255,245,165,0)');
    ctx.fillStyle = wg;
    ctx.fillRect(0, gy, W, H-gy);
  }

  if(p > .18){
    const sa = Math.min(1, (p-.18)/.35);
    ctx.save();
    ctx.globalAlpha = sa * .82;
    const sg = ctx.createLinearGradient(0,gy+6,0,gy+26);
    sg.addColorStop(0, `rgba(${lerp(80,115,p)|0},${lerp(160,210,p)|0},250,.75)`);
    sg.addColorStop(1, `rgba(55,145,220,.55)`);
    ctx.fillStyle = sg;
    ctx.beginPath();
    ctx.moveTo(W*.26, gy+6);
    ctx.bezierCurveTo(W*.40, gy+10, W*.54, gy+4, W*.70, gy+9);
    ctx.lineTo(W*.70, gy+24);
    ctx.bezierCurveTo(W*.54, gy+19, W*.40, gy+25, W*.26, gy+20);
    ctx.fill();
    ctx.strokeStyle = 'rgba(255,255,255,.55)';
    ctx.lineWidth = 1.2;
    for(let ri=0; ri<4; ri++){
      const rx = W*.36 + ri*24 + Math.sin(TM*1.3+ri)*6;
      ctx.beginPath(); ctx.ellipse(rx, gy+14, 9, 2.6, 0, 0, Math.PI*2); ctx.stroke();
    }
    ctx.restore();
  }

  for(let i=0; i<75; i++){
    const gx = (i/75)*W + Math.sin(i*1.1)*12;
    const gh = (10 + Math.sin(i*1.3)*5) * Math.min(1, p*3.5 + .2);
    ctx.strokeStyle = `hsl(${98+(i%22)*2}, 65%, ${lerp(26,42,p)|0}%)`;
    ctx.lineWidth = 1.7;
    ctx.beginPath(); ctx.moveTo(gx,gy);
    ctx.quadraticCurveTo(gx+Math.sin(TM+i*.4)*5, gy-gh*.5, gx+Math.sin(TM*.4+i)*3, gy-gh);
    ctx.stroke();
  }

  sceneFlowers.forEach(f=>{
    f.stemH = Math.min(f.maxH, f.stemH+.45);
    f.bloom = Math.min(1, f.bloom+.016);
    ctx.strokeStyle = `hsl(104, 58%, ${lerp(24,36,p)|0}%)`;
    ctx.lineWidth = 1.8;
    ctx.beginPath(); ctx.moveTo(f.x,f.y);
    ctx.quadraticCurveTo(f.x+Math.sin(TM+f.phase)*3, f.y-f.stemH*.5, f.x, f.y-f.stemH);
    ctx.stroke();
    if(f.bloom > .2){
      const ba = Math.min(1, (f.bloom-.2)/.8);
      for(let p2=0; p2<6; p2++){
        const ang = (p2/6)*Math.PI*2 + Math.sin(TM*.5+f.phase)*.08;
        const pr  = 5.2*f.size*f.bloom;
        ctx.globalAlpha = ba;
        ctx.fillStyle = `hsl(${f.hue}, 82%, 64%)`;
        ctx.beginPath();
        ctx.ellipse(f.x+Math.cos(ang)*pr, f.y-f.stemH+Math.sin(ang)*pr, pr*.78, pr*.42, ang, 0, Math.PI*2);
        ctx.fill();
      }
      ctx.fillStyle = `hsl(${f.hue+55}, 88%, 58%)`;
      ctx.beginPath(); ctx.arc(f.x, f.y-f.stemH, 4*f.size*f.bloom, 0, Math.PI*2); ctx.fill();
      ctx.globalAlpha = 1;
    }
  });

  foodPellets = foodPellets.filter(fp=>{
    fp.x += fp.vx; fp.y += fp.vy; fp.vy += .2; fp.a -= .015;
    if(fp.a <= 0) return false;
    ctx.globalAlpha = fp.a;
    ctx.fillStyle = `hsl(${fp.hue}, 82%, 62%)`;
    ctx.beginPath(); ctx.arc(fp.x, fp.y, fp.r, 0, Math.PI*2); ctx.fill();
    return fp.y < gy+12;
  });
  ctx.globalAlpha = 1;

  animals.forEach(a=>{
    if(a.type === 'bird') drawBird(a, p);
    else if(a.type === 'rabbit') drawRabbit(a, gy);
    else drawKancil(a, gy);
  });

  butterflies.forEach(bf => drawButterfly(bf, gy));

  if(p > .55){
    const sparkleAlpha = (p - .55) / .45;
    ctx.save();
    for(let i=0; i<16; i++){
      const sx = ((i*97 + TM*14*(i%2===0?1:-1)) % W + W) % W;
      const sy = H*.22 + ((i*61 + Math.sin(TM*.8+i)*26) % (H*.52));
      const sr = 1.4 + Math.sin(TM*2.5 + i)*0.9;
      ctx.globalAlpha = sparkleAlpha * (0.35 + 0.45*Math.sin(TM*2 + i*1.3));
      ctx.fillStyle = '#fff9d2';
      ctx.beginPath(); ctx.arc(sx, sy, Math.max(0.5, sr), 0, Math.PI*2); ctx.fill();
    }
    ctx.restore();
  }
}

function drawButterfly(bf, groundY){
  bf.wingPhase += bf.wingSpeed;
  bf.floatPhase += 0.035;
  bf.x += bf.dir * bf.vx;
  if(bf.x > W + 30){ bf.x = -30; bf.baseY = rand(H*.36, groundY - 22); }
  if(bf.x < -30){ bf.x = W + 30; bf.baseY = rand(H*.36, groundY - 22); }
  if(Math.random() < 0.004) bf.dir = -bf.dir;

  const y = bf.baseY + Math.sin(bf.floatPhase) * 16 + Math.cos(bf.floatPhase * 0.6) * 7;
  const flap = Math.abs(Math.sin(bf.wingPhase));
  const wingSpread = 0.25 + flap * 0.85;
  const s = bf.size * 9;

  ctx.save();
  ctx.translate(bf.x, y);
  ctx.rotate(bf.dir * 0.18 + Math.sin(bf.floatPhase)*0.12);

  [-1, 1].forEach(side => {
    ctx.save();
    ctx.scale(side * wingSpread, 1);

    ctx.fillStyle = `hsla(${bf.hue}, 88%, 64%, 0.92)`;
    ctx.beginPath();
    ctx.ellipse(s*0.65, -s*0.35, s*0.75, s*0.48, -0.35, 0, Math.PI*2);
    ctx.fill();

    ctx.fillStyle = `hsla(${(bf.hue+35)%360}, 95%, 82%, 0.75)`;
    ctx.beginPath();
    ctx.ellipse(s*0.72, -s*0.38, s*0.34, s*0.20, -0.35, 0, Math.PI*2);
    ctx.fill();

    ctx.fillStyle = `hsla(${(bf.hue+15)%360}, 84%, 58%, 0.88)`;
    ctx.beginPath();
    ctx.ellipse(s*0.50, s*0.32, s*0.56, s*0.38, 0.35, 0, Math.PI*2);
    ctx.fill();

    ctx.restore();
  });

  ctx.fillStyle = '#3b2818';
  ctx.beginPath();
  ctx.ellipse(0, 0, s*0.11, s*0.55, 0, 0, Math.PI*2);
  ctx.fill();

  ctx.strokeStyle = '#3b2818';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(0, -s*0.48); ctx.quadraticCurveTo(-s*0.22, -s*0.85, -s*0.32, -s*0.88);
  ctx.moveTo(0, -s*0.48); ctx.quadraticCurveTo( s*0.22, -s*0.85,  s*0.32, -s*0.88);
  ctx.stroke();

  ctx.restore();
}

function drawBird(b, p){
  b.wingPhase += .095;
  b.x += b.dir * (0.95 + p * 0.45);
  if(b.x > W+40) b.x = -40;
  if(b.x < -40) b.x = W+40;
  const glideY = b.flyH + Math.sin(TM * b.flySpd + b.wingPhase * 0.25) * b.flyAmp;
  const wy = Math.sin(b.wingPhase) * 4.5;
  const s = b.size;

  ctx.save();
  ctx.strokeStyle = `hsl(${b.hue}, 72%, ${lerp(55,42,p)|0}%)`;
  ctx.lineWidth = 2.4 * s;
  ctx.lineCap = 'round';
  ctx.beginPath();
  ctx.moveTo(b.x - 11*s, glideY - wy*0.4);
  ctx.quadraticCurveTo(b.x - 5*s, glideY - 5*s - wy, b.x, glideY);
  ctx.quadraticCurveTo(b.x + 5*s, glideY - 5*s - wy, b.x + 11*s, glideY - wy*0.4);
  ctx.stroke();

  ctx.fillStyle = `hsl(${b.hue}, 75%, 38%)`;
  ctx.beginPath(); ctx.arc(b.x, glideY, 2.2*s, 0, Math.PI*2); ctx.fill();
  ctx.restore();
}

function drawRabbit(r, groundY){
  r.hopTimer -= .016;
  r.munchTimer -= .016;
  if(r.hopTimer < 0){
    r.isHopping = true;
    r.hopPhase = 0;
    r.hopTimer = rand(1.4, 3.8);
    if(Math.random() < .35) r.dir = -r.dir;
  }
  let ry = groundY + 3;
  if(r.isHopping){
    r.hopPhase += .15;
    r.x += r.dir * 2.1;
    ry -= Math.sin(r.hopPhase) * 14;
    if(r.hopPhase > Math.PI) r.isHopping = false;
    r.x = clamp(r.x, W*.04, W*.96);
  }
  if(r.munchTimer < 0){ r.munch = 1; r.munchTimer = rand(1.8, 3.8); }
  if(r.munch > 0) r.munch -= .04;

  const s = r.size * 16, x = r.x, y = ry - s*.55;
  ctx.save();
  ctx.translate(x, y);
  if(r.dir < 0) ctx.scale(-1, 1);

  ctx.fillStyle = '#ffffff';
  ctx.beginPath(); ctx.arc(-s*.52, s*.06, s*.16, 0, Math.PI*2); ctx.fill();

  ctx.fillStyle = `hsl(${r.hue}, 24%, 86%)`;
  ctx.beginPath(); ctx.ellipse(0, 0, s*.54, s*.44, 0, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.ellipse(s*.32, -s*.28, s*.31, s*.28, .18, 0, Math.PI*2); ctx.fill();

  [[s*.20, -s*.76, -.12], [s*.38, -s*.70, .12]].forEach(([ex, ey, ea])=>{
    ctx.fillStyle = `hsl(${r.hue}, 24%, 86%)`;
    ctx.beginPath(); ctx.ellipse(ex, ey, s*.09, s*.28, ea, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = 'rgba(255,165,175,.65)';
    ctx.beginPath(); ctx.ellipse(ex, ey, s*.045, s*.17, ea, 0, Math.PI*2); ctx.fill();
  });

  ctx.fillStyle = '#1a1a1a';
  ctx.beginPath(); ctx.arc(s*.48, -s*.35, s*.068, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = '#ffffff';
  ctx.beginPath(); ctx.arc(s*.50, -s*.37, s*.024, 0, Math.PI*2); ctx.fill();

  ctx.fillStyle = 'rgba(255,130,145,.45)';
  ctx.beginPath(); ctx.arc(s*.44, -s*.22, s*.07, 0, Math.PI*2); ctx.fill();

  const mo = r.munch > 0 ? Math.sin(TM*16)*1.1 : 0;
  ctx.fillStyle = 'rgba(255,105,120,.9)';
  ctx.beginPath(); ctx.arc(s*.64, -s*.24 + mo, s*.052, 0, Math.PI*2); ctx.fill();
  ctx.restore();
}

function drawKancil(d, groundY){
  d.walkTimer -= .016;
  if(d.walkTimer < 0){
    d.isWalking = !d.isWalking;
    d.walkTimer = rand(1.5, 4.0);
    if(Math.random() < 0.45) d.dir = -d.dir;
  }
  d.hopTimer -= .016;
  if(d.hopTimer < 0){
    d.isHopping = true;
    d.hopPhase = 0;
    d.hopTimer = rand(2.5, 5.5);
  }

  let bounceY = 0;
  let legSwing = 0;
  if(d.isHopping){
    d.hopPhase += .14;
    d.x += d.dir * 1.8;
    bounceY = Math.sin(d.hopPhase) * 11;
    legSwing = Math.sin(d.hopPhase * 2) * 0.35;
    if(d.hopPhase > Math.PI) d.isHopping = false;
  } else if(d.isWalking){
    d.x += d.dir * 0.65;
    bounceY = Math.abs(Math.sin(TM * 7 + d.wingPhase)) * 2.2;
    legSwing = Math.sin(TM * 7 + d.wingPhase) * 0.25;
  }
  d.x = clamp(d.x, W*.05, W*.95);

  const s = d.size * 18;
  ctx.save();
  ctx.translate(d.x, groundY + 3 - bounceY);
  if(d.dir < 0) ctx.scale(-1, 1);

  ctx.strokeStyle = '#6e4219';
  ctx.lineWidth = s * 0.075;
  ctx.lineCap = 'round';
  [[-s*.34, -legSwing], [-s*.18, legSwing], [s*.18, -legSwing], [s*.32, legSwing]].forEach(([lx, ang])=>{
    ctx.save();
    ctx.translate(lx, -s*.36);
    ctx.rotate(ang);
    ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, s*.36); ctx.stroke();
    ctx.restore();
  });

  ctx.fillStyle = '#f5e6d3';
  ctx.beginPath(); ctx.ellipse(-s*.52, -s*.56, s*.10, s*.06, -0.4, 0, Math.PI*2); ctx.fill();

  ctx.fillStyle = '#b56e28';
  ctx.beginPath(); ctx.ellipse(0, -s*.52, s*.48, s*.27, 0, 0, Math.PI*2); ctx.fill();

  ctx.fillStyle = '#f7ebd9';
  ctx.beginPath(); ctx.ellipse(s*.02, -s*.37, s*.34, s*.11, 0, 0, Math.PI); ctx.fill();

  ctx.fillStyle = 'rgba(255, 246, 230, 0.85)';
  [[-s*.22, -s*.58], [-s*.06, -s*.62], [s*.10, -s*.58], [-s*.14, -s*.49], [s*.03, -s*.50]].forEach(([bx, by])=>{
    ctx.beginPath(); ctx.arc(bx, by, s*.032, 0, Math.PI*2); ctx.fill();
  });

  ctx.fillStyle = '#c4792e';
  ctx.beginPath();
  ctx.moveTo(s*.22, -s*.56);
  ctx.lineTo(s*.36, -s*.86);
  ctx.lineTo(s*.48, -s*.72);
  ctx.lineTo(s*.36, -s*.48);
  ctx.fill();

  ctx.beginPath(); ctx.ellipse(s*.46, -s*.86, s*.23, s*.17, 0.15, 0, Math.PI*2); ctx.fill();

  const earTwitch = Math.sin(TM*4 + d.wingPhase) * 0.08;
  ctx.save();
  ctx.translate(s*.34, -s*.98);
  ctx.rotate(-0.25 + earTwitch);
  ctx.fillStyle = '#b56e28';
  ctx.beginPath(); ctx.ellipse(0, -s*.08, s*.07, s*.13, 0, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = '#f2b8a2';
  ctx.beginPath(); ctx.ellipse(0, -s*.08, s*.035, s*.08, 0, 0, Math.PI*2); ctx.fill();
  ctx.restore();

  ctx.fillStyle = '#18120e';
  ctx.beginPath(); ctx.arc(s*.51, -s*.88, s*.048, 0, Math.PI*2); ctx.fill();
  ctx.fillStyle = '#ffffff';
  ctx.beginPath(); ctx.arc(s*.525, -s*.895, s*.018, 0, Math.PI*2); ctx.fill();

  ctx.fillStyle = '#2b1b12';
  ctx.beginPath(); ctx.arc(s*.67, -s*.82, s*.034, 0, Math.PI*2); ctx.fill();

  ctx.restore();
}

// ══════════════════════════════════════════
// SCENE 1 — SUBHANALLAH: Aurora -> Sunrise -> Drone Zoom-Out to Cosmos
// ══════════════════════════════════════════
let hillFlowers=[];
const auroraStars = Array.from({length:240}, ()=>({
  x: rand(0,1), y: rand(0,0.85), r: rand(0.35, 1.9),
  a: rand(0, Math.PI*2), sp: rand(0.004, 0.014),
  tint: Math.random() < 0.25 ? '#ffe7ba' : (Math.random() < 0.5 ? '#c8e6ff' : '#ffffff')
}));

const cosmicNebulae = [
  {x: 0.22, y: 0.24, rx: 0.36, ry: 0.22, rot: -0.35, c1: 'rgba(110, 68, 225, 0.34)', c2: 'rgba(40, 175, 225, 0.14)'},
  {x: 0.78, y: 0.22, rx: 0.34, ry: 0.20, rot:  0.40, c1: 'rgba(225, 95, 165, 0.30)', c2: 'rgba(255, 175, 85, 0.14)'},
  {x: 0.50, y: 0.16, rx: 0.48, ry: 0.25, rot:  0.10, c1: 'rgba(65, 200, 185, 0.26)', c2: 'rgba(130, 90, 235, 0.12)'},
];

const distantGalaxies = [
  {x: 0.16, y: 0.20, r: 26, angle: -0.42, hue: 210},
  {x: 0.84, y: 0.28, r: 22, angle:  0.55, hue: 38},
  {x: 0.74, y: 0.13, r: 16, angle: -0.20, hue: 280},
];

function drawScene1(p){
  const auroraPhase  = clamp(p / 0.55, 0, 1);
  const sunrisePhase = smoothstep(0.42, 0.82, p);
  const baseDrone    = smoothstep(0.76, 1.0, p) * 0.45;
  const droneT       = clamp(baseDrone + subhanDroneProgress * 0.55, 0, 1);

  const spaceBg = ctx.createRadialGradient(W*0.5, H*0.45, 10, W*0.5, H*0.45, Math.max(W, H)*0.85);
  spaceBg.addColorStop(0, '#0a0f29');
  spaceBg.addColorStop(0.55, '#050716');
  spaceBg.addColorStop(1, '#02030a');
  ctx.fillStyle = spaceBg;
  ctx.fillRect(0, 0, W, H);

  if(droneT > 0.02){
    ctx.save();
    cosmicNebulae.forEach(nb => {
      ctx.save();
      ctx.translate(nb.x * W, nb.y * H);
      ctx.rotate(nb.rot);
      ctx.scale(1, nb.ry / nb.rx);
      const rad = nb.rx * W;
      const ng = ctx.createRadialGradient(0, 0, 0, 0, 0, rad);
      ng.addColorStop(0, nb.c1);
      ng.addColorStop(0.55, nb.c2);
      ng.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.globalAlpha = droneT * 0.95;
      ctx.fillStyle = ng;
      ctx.beginPath(); ctx.arc(0, 0, rad, 0, Math.PI*2); ctx.fill();
      ctx.restore();
    });

    ctx.save();
    ctx.translate(W*0.5, H*0.32);
    ctx.rotate(-0.32);
    const mw = ctx.createLinearGradient(0, -H*0.16, 0, H*0.16);
    mw.addColorStop(0, 'rgba(180,210,255,0)');
    mw.addColorStop(0.5, `rgba(215,225,255,${0.16 * droneT})`);
    mw.addColorStop(1, 'rgba(180,210,255,0)');
    ctx.fillStyle = mw;
    ctx.fillRect(-W, -H*0.16, W*2, H*0.32);
    ctx.restore();

    distantGalaxies.forEach(g => {
      ctx.save();
      ctx.translate(g.x * W, g.y * H);
      ctx.rotate(g.angle + TM * 0.04);
      ctx.globalAlpha = droneT * 0.85;
      const gg = ctx.createRadialGradient(0, 0, 0, 0, 0, g.r);
      gg.addColorStop(0, `hsla(${g.hue}, 90%, 88%, 0.95)`);
      gg.addColorStop(0.4, `hsla(${g.hue}, 80%, 65%, 0.45)`);
      gg.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = gg;
      ctx.beginPath(); ctx.ellipse(0, 0, g.r, g.r*0.38, 0, 0, Math.PI*2); ctx.fill();
      ctx.restore();
    });
    ctx.restore();
  }

  auroraStars.forEach(s => {
    s.a += s.sp;
    const twinkle = (Math.sin(s.a) + 1) / 2;
    const nightVis = (1 - sunrisePhase * 0.72);
    const spaceVis = droneT * 1.0;
    const vis = clamp(Math.max(nightVis * (0.35 + auroraPhase * 0.65), spaceVis), 0, 1);
    const alpha = (0.3 + twinkle * 0.7) * vis;
    if(alpha > 0.02){
      ctx.beginPath();
      ctx.arc(s.x * W, s.y * H, s.r * (1 + droneT * 0.25), 0, Math.PI*2);
      ctx.fillStyle = s.tint;
      ctx.globalAlpha = alpha;
      ctx.fill();
    }
  });
  ctx.globalAlpha = 1;

  const gy = H * 0.75;
  const zoomScale = lerp(1.0, 0.34, droneT);
  const earthCenterY = lerp(H * 0.5, H * 0.76, droneT);
  const atmosphereFade = 1 - smoothstep(0.35, 0.95, droneT);

  ctx.save();
  ctx.translate(W * 0.5, earthCenterY);
  ctx.scale(zoomScale, zoomScale);
  ctx.translate(-W * 0.5, -H * 0.5);

  if(atmosphereFade > 0.01){
    ctx.save();
    ctx.globalAlpha = atmosphereFade;
    const sky = ctx.createLinearGradient(0, 0, 0, gy);
    if(sunrisePhase < 0.01){
      sky.addColorStop(0, `hsl(258, ${lerp(62,78,auroraPhase)|0}%, ${lerp(6,10,auroraPhase)|0}%)`);
      sky.addColorStop(0.5, `hsl(238, ${lerp(55,68,auroraPhase)|0}%, ${lerp(8,14,auroraPhase)|0}%)`);
      sky.addColorStop(1, `hsl(218, ${lerp(45,58,auroraPhase)|0}%, ${lerp(11,19,auroraPhase)|0}%)`);
    } else {
      sky.addColorStop(0, `hsl(${lerp(258, 206, sunrisePhase)|0}, ${lerp(78, 82, sunrisePhase)|0}%, ${lerp(10, 44, sunrisePhase)|0}%)`);
      sky.addColorStop(0.52, `hsl(${lerp(238, 28, sunrisePhase)|0}, ${lerp(68, 88, sunrisePhase)|0}%, ${lerp(14, 58, sunrisePhase)|0}%)`);
      sky.addColorStop(1, `hsl(${lerp(218, 42, sunrisePhase)|0}, ${lerp(58, 95, sunrisePhase)|0}%, ${lerp(19, 74, sunrisePhase)|0}%)`);
    }
    ctx.fillStyle = sky;
    ctx.fillRect(-W, -H, W*3, H*2);
    ctx.restore();
  }

  if(sunrisePhase < 0.55){
    const ma = (1 - sunrisePhase / 0.55) * (1 - droneT * 0.8);
    const mx = W * 0.82, my = H * 0.13;
    ctx.save();
    ctx.globalAlpha = Math.max(0, ma);
    const mg = ctx.createRadialGradient(mx, my, 0, mx, my, 22);
    mg.addColorStop(0, 'rgba(255,249,215,.95)');
    mg.addColorStop(1, 'rgba(255,240,160,.25)');
    ctx.fillStyle = mg;
    ctx.beginPath(); ctx.arc(mx, my, 20, 0, Math.PI*2); ctx.fill();
    ctx.fillStyle = '#090d22';
    ctx.beginPath(); ctx.arc(mx+9, my-2, 17, 0, Math.PI*2); ctx.fill();
    ctx.restore();
  }

  const auroraVis = Math.min(1, p * 2.2) * (1 - sunrisePhase * 0.65) * (1 - droneT * 0.5);
  if(auroraVis > 0.01){
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    const curtains = [
      {hue: 155, sat: 95, light: 58, yBase: H*0.14, amp: 28, speed: 0.75, alpha: 0.36},
      {hue: 185, sat: 92, light: 56, yBase: H*0.19, amp: 34, speed: 0.55, alpha: 0.30},
      {hue: 285, sat: 88, light: 62, yBase: H*0.11, amp: 24, speed: 0.65, alpha: 0.26},
      {hue: 135, sat: 95, light: 54, yBase: H*0.24, amp: 22, speed: 0.90, alpha: 0.28},
    ];
    curtains.forEach((c, idx) => {
      const step = 10;
      for(let x2 = -W*0.2; x2 <= W*1.2; x2 += step){
        const frac = x2 / W;
        const wave = Math.sin(frac * Math.PI * 3.2 + TM * c.speed + idx * 1.4) * c.amp
                   + Math.cos(frac * Math.PI * 5.5 - TM * c.speed * 0.7 + idx) * (c.amp * 0.45);
        const topY = c.yBase + wave;
        const pillarH = H * (0.24 + 0.10 * Math.sin(frac * Math.PI * 4 + TM * 0.8 + idx));
        const shimmer = 0.65 + 0.35 * Math.sin(frac * 18 + TM * 2.2 + idx);
        const ag = ctx.createLinearGradient(x2, topY + pillarH, x2, topY);
        ag.addColorStop(0, `hsla(${c.hue}, ${c.sat}%, ${c.light}%, 0)`);
        ag.addColorStop(0.28, `hsla(${c.hue}, ${c.sat}%, ${c.light}%, ${c.alpha * auroraVis * shimmer})`);
        ag.addColorStop(0.75, `hsla(${(c.hue+25)%360}, ${c.sat}%, ${c.light+10}%, ${c.alpha * 0.55 * auroraVis * shimmer})`);
        ag.addColorStop(1, `hsla(${(c.hue+45)%360}, ${c.sat}%, ${c.light+15}%, 0)`);
        ctx.fillStyle = ag;
        ctx.fillRect(x2, topY, step + 1, pillarH);
      }
    });
    ctx.restore();
  }

  if(sunrisePhase > 0.01){
    const sunX = W * 0.52;
    const sunY = lerp(gy + 34, H * 0.26, sunrisePhase);
    const sunR = lerp(24, 38, sunrisePhase);

    ctx.save();
    const dawnGlow = ctx.createRadialGradient(sunX, sunY, sunR * 0.3, sunX, sunY, W * 0.75);
    dawnGlow.addColorStop(0, `rgba(255, 248, 210, ${0.75 * sunrisePhase})`);
    dawnGlow.addColorStop(0.28, `rgba(255, 195, 95, ${0.42 * sunrisePhase})`);
    dawnGlow.addColorStop(0.62, `rgba(255, 125, 75, ${0.18 * sunrisePhase})`);
    dawnGlow.addColorStop(1, 'rgba(255, 125, 75, 0)');
    ctx.fillStyle = dawnGlow;
    ctx.fillRect(-W, -H, W*3, H*2);

    ctx.globalAlpha = sunrisePhase * 0.65;
    for(let r = 0; r < 16; r++){
      const ang = (r / 16) * Math.PI * 2 + TM * 0.12;
      const r1 = sunR + 8;
      const r2 = sunR + 55 + Math.sin(TM * 1.8 + r) * 12;
      ctx.strokeStyle = 'rgba(255, 236, 165, 0.55)';
      ctx.lineWidth = 2.4;
      ctx.beginPath();
      ctx.moveTo(sunX + Math.cos(ang)*r1, sunY + Math.sin(ang)*r1);
      ctx.lineTo(sunX + Math.cos(ang)*r2, sunY + Math.sin(ang)*r2);
      ctx.stroke();
    }

    ctx.globalAlpha = Math.min(1, sunrisePhase * 1.4);
    const sunCore = ctx.createRadialGradient(sunX, sunY, 0, sunX, sunY, sunR);
    sunCore.addColorStop(0, '#ffffff');
    sunCore.addColorStop(0.65, '#ffe58f');
    sunCore.addColorStop(1, '#ff9f43');
    ctx.fillStyle = sunCore;
    ctx.beginPath(); ctx.arc(sunX, sunY, sunR, 0, Math.PI*2); ctx.fill();
    ctx.restore();
  }

  if(sunrisePhase > 0.15){
    const ca = Math.min(0.85, (sunrisePhase - 0.15) / 0.5) * (1 - droneT * 0.4);
    ctx.save();
    ctx.globalAlpha = ca;
    ctx.fillStyle = 'rgba(255, 224, 178, 0.78)';
    drawCloud(W*0.24 + Math.sin(TM*0.08)*12, H*0.22, 125, 36, ca, 1);
    drawCloud(W*0.76 - Math.cos(TM*0.07)*14, H*0.19, 138, 40, ca, 1);
    ctx.restore();
  }

  const mtnLayers = [
    {night: [245, 45, 11], day: [225, 38, 28], hBase: 0.62, amp: 0.07, freq: 2.4, phase: 0.2},
    {night: [232, 38, 14], day: [205, 36, 24], hBase: 0.67, amp: 0.055, freq: 3.1, phase: 1.4},
    {night: [220, 32, 17], day: [165, 42, 22], hBase: 0.71, amp: 0.04, freq: 3.8, phase: 2.6}
  ];

  mtnLayers.forEach((m, mi) => {
    const mh = lerp(m.night[0], m.day[0], sunrisePhase) | 0;
    const ms = lerp(m.night[1], m.day[1], sunrisePhase) | 0;
    const ml = lerp(m.night[2], m.day[2], sunrisePhase) | 0;
    ctx.fillStyle = `hsl(${mh}, ${ms}%, ${ml}%)`;
    ctx.beginPath();
    ctx.moveTo(-W*0.5, H*1.5);
    for(let xi = -W*0.5; xi <= W*1.5; xi += 10){
      const f = xi / W;
      const my = H * (m.hBase + Math.sin(f * Math.PI * m.freq + m.phase) * m.amp + Math.cos(f * Math.PI * 1.7 + mi) * 0.025);
      ctx.lineTo(xi, my);
    }
    ctx.lineTo(W*1.5, H*1.5);
    ctx.closePath();
    ctx.fill();

    if(sunrisePhase > 0.1){
      ctx.strokeStyle = `rgba(255, 215, 130, ${0.32 * sunrisePhase})`;
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  });

  const gg = ctx.createLinearGradient(0, gy, 0, H*1.3);
  gg.addColorStop(0, `hsl(${lerp(142, 112, sunrisePhase)|0}, ${lerp(24, 58, sunrisePhase)|0}%, ${lerp(11, 32, sunrisePhase)|0}%)`);
  gg.addColorStop(1, `hsl(${lerp(132, 102, sunrisePhase)|0}, ${lerp(18, 46, sunrisePhase)|0}%, ${lerp(7, 18, sunrisePhase)|0}%)`);
  ctx.fillStyle = gg;
  ctx.fillRect(-W*0.5, gy, W*2, H*0.6);

  for(let i=0; i<65; i++){
    const gx = (i/65)*W + Math.sin(i*1.1)*12;
    const gh = (9 + Math.sin(i*1.3)*5) * Math.min(1, p*2.2 + 0.2);
    ctx.strokeStyle = `hsl(${lerp(132,106,sunrisePhase)|0}, 58%, ${lerp(24,36,sunrisePhase)|0}%)`;
    ctx.lineWidth = 1.6;
    ctx.beginPath(); ctx.moveTo(gx, gy);
    ctx.quadraticCurveTo(gx + Math.sin(TM+i*0.4)*4, gy - gh*0.5, gx + Math.sin(TM*0.4+i)*3, gy - gh);
    ctx.stroke();
  }

  hillFlowers.forEach(f => {
    f.stemH = Math.min(f.maxH, f.stemH + 0.4);
    f.bloom = Math.min(1, f.bloom + 0.012);
    ctx.strokeStyle = `hsl(${lerp(140,110,sunrisePhase)|0}, 52%, ${lerp(22,32,sunrisePhase)|0}%)`;
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(f.x, f.y);
    ctx.quadraticCurveTo(f.x + Math.sin(TM+f.phase)*2, f.y - f.stemH*0.5, f.x, f.y - f.stemH);
    ctx.stroke();
    if(f.bloom > 0.3){
      const ba = Math.min(1, (f.bloom - 0.3) / 0.7);
      for(let p2=0; p2<5; p2++){
        const ang = (p2/5)*Math.PI*2;
        const pr = 4.2 * f.size * f.bloom;
        ctx.globalAlpha = ba * 0.92;
        ctx.fillStyle = `hsl(${f.hue}, 82%, 66%)`;
        ctx.beginPath();
        ctx.ellipse(f.x + Math.cos(ang)*pr, f.y - f.stemH + Math.sin(ang)*pr, pr*0.8, pr*0.4, ang, 0, Math.PI*2);
        ctx.fill();
      }
      ctx.fillStyle = `hsl(${f.hue+50}, 85%, 58%)`;
      ctx.beginPath(); ctx.arc(f.x, f.y - f.stemH, 3*f.size*f.bloom, 0, Math.PI*2); ctx.fill();
      ctx.globalAlpha = 1;
    }
  });

  ctx.restore();

  if(droneT > 0.15){
    const earthVis = smoothstep(0.15, 0.85, droneT);
    const globeR = Math.max(W, H) * lerp(1.65, 0.72, droneT);
    const globeY = H * lerp(1.58, 1.18, droneT);

    ctx.save();
    const atmoGlow = ctx.createRadialGradient(W*0.5, globeY, globeR * 0.94, W*0.5, globeY, globeR * 1.12);
    atmoGlow.addColorStop(0, 'rgba(90, 185, 255, 0)');
    atmoGlow.addColorStop(0.45, `rgba(110, 200, 255, ${0.42 * earthVis})`);
    atmoGlow.addColorStop(0.75, `rgba(255, 225, 155, ${0.24 * earthVis})`);
    atmoGlow.addColorStop(1, 'rgba(90, 185, 255, 0)');
    ctx.fillStyle = atmoGlow;
    ctx.beginPath(); ctx.arc(W*0.5, globeY, globeR * 1.12, 0, Math.PI*2); ctx.fill();

    ctx.strokeStyle = `rgba(175, 228, 255, ${0.55 * earthVis})`;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.arc(W*0.5, globeY, globeR, Math.PI * 1.15, Math.PI * 1.85);
    ctx.stroke();
    ctx.restore();
  }
}

// ══════════════════════════════════════════
// SCENE 2 — ASTAGFIRULLAH: Fire Extinguished
// ══════════════════════════════════════════
let raindrops=[], steamPuffs=[];

function drawScene2(p){
  const gy=H*.73, fi=Math.max(0,1-p*.97);
  const sky=ctx.createLinearGradient(0,0,0,gy);
  if(p<.4){ const q=p/.4; sky.addColorStop(0,`rgb(${lerp(8,10,q)|0},${lerp(2,4,q)|0},${lerp(2,4,q)|0})`); sky.addColorStop(.5,`rgb(${lerp(60,35,q)|0},6,3)`); sky.addColorStop(1,`rgb(${lerp(130,70,q)|0},${lerp(22,14,q)|0},4)`); }
  else if(p<.75){ const q=(p-.4)/.35; sky.addColorStop(0,`rgb(${lerp(10,8,q)|0},${lerp(4,16,q)|0},${lerp(4,52,q)|0})`); sky.addColorStop(.5,`rgb(${lerp(35,14,q)|0},${lerp(6,42,q)|0},${lerp(3,95,q)|0})`); sky.addColorStop(1,`rgb(${lerp(70,20,q)|0},${lerp(14,70,q)|0},${lerp(4,145,q)|0})`); }
  else{ const q=(p-.75)/.25; sky.addColorStop(0,`rgb(${lerp(8,18,q)|0},${lerp(16,75,q)|0},${lerp(52,175,q)|0})`); sky.addColorStop(1,`rgb(${lerp(20,50,q)|0},${lerp(70,145,q)|0},${lerp(145,225,q)|0})`); }
  ctx.fillStyle=sky; ctx.fillRect(0,0,W,H);
  if(p>.25){ const ca=Math.min(1,(p-.25)/.3); drawCloud(W*.2,H*.1,100,38,ca,1); drawCloud(W*.62,H*.08,118,42,ca,1); }
  if(fi>.01) drawFire(gy,fi);
  if(p>.07) updateRain(gy,p);
  if(p>.1&&p<.9&&Math.random()<.07*p)
    steamPuffs.push({x:rand(W*.1,W*.9),y:gy-rand(10,30),r:rand(5,15),a:.6,vy:-rand(.5,1.5),vx:rand(-1,1)});
  steamPuffs=steamPuffs.filter(sp=>{ sp.x+=sp.vx; sp.y+=sp.vy; sp.r+=.3; sp.a-=.015; if(sp.a<=0) return false; ctx.globalAlpha=sp.a*.5; ctx.fillStyle='rgba(200,200,200,.5)'; ctx.beginPath(); ctx.arc(sp.x,sp.y,sp.r,0,Math.PI*2); ctx.fill(); return true; });
  ctx.globalAlpha=1;
  const r=lerp(28,25,p)|0,g=lerp(8,110,p)|0,b=lerp(4,20,p)|0;
  const gg=ctx.createLinearGradient(0,gy,0,H);
  gg.addColorStop(0,`rgb(${r},${g},${b})`); gg.addColorStop(1,`rgb(${Math.max(0,r-16)},${Math.max(0,g-16)},${Math.max(0,b-10)})`);
  ctx.fillStyle=gg; ctx.fillRect(0,gy,W,H-gy);
  if(p>.45){ const ga=Math.min(1,(p-.45)/.4); for(let i=0;i<48;i++){ const gx=(i/48)*W+Math.sin(i*.7)*16, gh=(11+Math.sin(i*1.3)*5)*ga; ctx.strokeStyle=`hsl(${100+(i%18)*2},62%,${30+ga*8|0}%)`; ctx.lineWidth=1.8; ctx.globalAlpha=ga; ctx.beginPath(); ctx.moveTo(gx,gy); ctx.quadraticCurveTo(gx+Math.sin(TM+i*.4)*5,gy-gh*.5,gx+Math.sin(TM*.4+i)*3,gy-gh); ctx.stroke(); } ctx.globalAlpha=1; }
  if(p>.85){ const la=(p-.85)/.15, lg=ctx.createLinearGradient(W*.45,0,W*.55,gy); lg.addColorStop(0,`rgba(255,245,200,${.15*la})`); lg.addColorStop(1,'rgba(255,245,200,0)'); ctx.fillStyle=lg; ctx.beginPath(); ctx.moveTo(W*.47,0); ctx.lineTo(W*.53,0); ctx.lineTo(W*.72,gy); ctx.lineTo(W*.28,gy); ctx.fill(); }
}

function drawFire(gy,intensity){
  const fW=W*.88,fX=W*.06,maxH=H*.46,nf=14;
  const gl=ctx.createRadialGradient(W/2,gy,0,W/2,gy,fW*.54);
  gl.addColorStop(0,`rgba(255,70,0,${.32*intensity})`); gl.addColorStop(1,'rgba(255,0,0,0)');
  ctx.fillStyle=gl; ctx.fillRect(0,gy-maxH,W,maxH+10);
  for(let i=0;i<nf;i++){
    const t=i/nf, x=fX+t*fW+Math.sin(TM*1.4+i*.8)*12;
    const baseH=maxH*(.25+.75*Math.sin(Math.PI*t))*intensity;
    const h=baseH*(.68+.32*Math.sin(TM*2.6+i*.9));
    const g1=ctx.createLinearGradient(x,gy,x,gy-h);
    g1.addColorStop(0,`rgba(255,35,0,${.9*intensity})`); g1.addColorStop(.55,`rgba(255,110,0,${.5*intensity})`); g1.addColorStop(1,'rgba(255,180,0,0)');
    ctx.fillStyle=g1; ctx.beginPath(); ctx.moveTo(x-18,gy); ctx.quadraticCurveTo(x-8,gy-h*.55,x+Math.sin(TM+i)*7,gy-h); ctx.quadraticCurveTo(x+8,gy-h*.55,x+18,gy); ctx.fill();
    const ih=h*.57, g2=ctx.createLinearGradient(x,gy,x,gy-ih);
    g2.addColorStop(0,`rgba(255,255,120,${.9*intensity})`); g2.addColorStop(.6,`rgba(255,200,0,${.4*intensity})`); g2.addColorStop(1,'rgba(255,80,0,0)');
    ctx.fillStyle=g2; ctx.beginPath(); ctx.moveTo(x-9,gy); ctx.quadraticCurveTo(x-3,gy-ih*.6,x+Math.sin(TM*1.3+i)*4,gy-ih); ctx.quadraticCurveTo(x+3,gy-ih*.6,x+9,gy); ctx.fill();
  }
  for(let i=0;i<22;i++){ const ex=W*.1+Math.sin(TM*.9+i*.73)*W*.4+(i/22)*W*.8, ey=gy-15-(Math.sin(TM*.7+i)*.5+.5)*maxH*.5*intensity; ctx.beginPath(); ctx.arc(ex%W,ey,1.4,0,Math.PI*2); ctx.fillStyle=`rgba(255,${120+Math.round(Math.sin(TM+i)*80)},0,${.7*intensity})`; ctx.fill(); }
}

function updateRain(gy,p){
  for(let i=0;i<p*5;i++) if(Math.random()<.4) raindrops.push({x:rand(0,W),y:rand(-H*.3,0),speed:rand(9,17),len:rand(10,24),a:rand(.3,.7)});
  ctx.lineWidth=1;
  raindrops=raindrops.filter(d=>{ d.y+=d.speed; ctx.strokeStyle=`rgba(140,200,255,${d.a})`; ctx.globalAlpha=d.a; ctx.beginPath(); ctx.moveTo(d.x,d.y); ctx.lineTo(d.x-1,d.y+d.len); ctx.stroke(); if(d.y+d.len>gy){ctx.globalAlpha=.22;ctx.strokeStyle='rgba(150,210,255,.5)';ctx.beginPath();ctx.arc(d.x,gy,2.5,0,Math.PI*2);ctx.stroke();} return d.y<gy+10; }).slice(-400);
  ctx.globalAlpha=1;
}

// ══════════════════════════════════════════
// SHARED HELPERS
// ══════════════════════════════════════════
function drawCloud(cx,cy,rw,rh,alpha,bright=1){
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.fillStyle = bright > .5 ? 'rgba(255,255,255,.88)' : 'rgba(225,238,255,.78)';
  [[0,0,1,1],[-.24,.12,.68,.82],[.24,.12,.68,.82]].forEach(([dx,dy,sw,sh])=>{
    ctx.beginPath();
    ctx.ellipse(cx+dx*rw, cy+dy*rh, rw*sw*.5, rh*sh*.5, 0, 0, Math.PI*2);
    ctx.fill();
  });
  ctx.restore();
}

// ══════════════════════════════════════════
// TAP FX
// ══════════════════════════════════════════
let tapRipples=[], tapParticles=[];

function triggerFX(x,y){
  const palettes=[[42,54,115],[155,42,210],[200,220,180]];
  const pal=palettes[cur];
  for(let i=0;i<3;i++) setTimeout(()=>tapRipples.push({x,y,r:i*14+12,a:.72-i*.16,hue:pal[i%pal.length]}),i*90);
  for(let i=0;i<10;i++){ const ang=Math.random()*Math.PI*2,spd=rand(1.5,5); tapParticles.push({x,y,vx:Math.cos(ang)*spd,vy:Math.sin(ang)*spd-1.5,r:rand(2,4.5),a:1,hue:pal[Math.floor(Math.random()*pal.length)]}); }

  if(cur===0){
    const d0 = DHIKRS[0];
    const p0 = d0.count / d0.target;
    spawnFood(x,y);

    if(d0.count % 2 === 0 || p0 > 0.65){
      if(animals.length < 24) spawnAnimal();
    }
    if(d0.count % 2 === 0 || p0 > 0.60){
      if(butterflies.length < 18) spawnButterfly();
    }
    if(d0.count >= d0.target){
      ['bird','bird','rabbit','rabbit','kancil','kancil'].forEach(t=>{
        if(animals.length < 28) spawnAnimal(t);
      });
      while(butterflies.length < 16) spawnButterfly();
    }
    if(d0.count % 2 === 0 || d0.count <= 10) spawnFlower0();
  }

  if(cur===1 && DHIKRS[1].count % 2 === 0)
    hillFlowers.push({x:rand(W*.02,W*.98),y:H*.75,hue:Math.round(rand(0,360)),size:rand(.5,1.2),stemH:0,maxH:rand(14,38),bloom:0,phase:rand(0,Math.PI*2)});
}

function drawFX(){
  tapRipples=tapRipples.filter(tr=>{ tr.r+=3.5; tr.a-=.022; if(tr.a<=0) return false; ctx.globalAlpha=tr.a; ctx.strokeStyle=`hsl(${tr.hue},100%,70%)`; ctx.lineWidth=1.8; ctx.beginPath(); ctx.arc(tr.x,tr.y,tr.r,0,Math.PI*2); ctx.stroke(); return true; });
  tapParticles=tapParticles.filter(p=>{ p.x+=p.vx; p.y+=p.vy; p.vy+=.12; p.a-=.024; if(p.a<=0) return false; ctx.globalAlpha=p.a; ctx.fillStyle=`hsl(${p.hue},85%,65%)`; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fill(); return true; });
  ctx.globalAlpha=1;
}

// ══════════════════════════════════════════
// MAIN LOOP
// ══════════════════════════════════════════
function loop(){
  if(appRunning){
    TM+=.016;
    if(subhanFinaleActive && cur === 1){
      subhanDroneProgress = Math.min(1, subhanDroneProgress + 0.011);
    }
    const p=Math.min(1, DHIKRS[cur].count/DHIKRS[cur].target);
    if(cur===0) drawScene0(p);
    else if(cur===1) drawScene1(p);
    else drawScene2(p);
    drawFX();
  }
  requestAnimationFrame(loop);
}
loop();

// ══════════════════════════════════════════
// TAP HANDLER
// ══════════════════════════════════════════
let lastTap=0;
function handleTap(e){
  e.preventDefault();
  checkDayRollover();
  const now=Date.now(); if(now-lastTap<85) return; lastTap=now;
  const d=DHIKRS[cur]; if(d.count>=d.target) return;

  d.count++;
  d.dailyTotal++;
  const completed = d.count >= d.target;
  if(completed) d.sessions++;
  saveDailyData();

  const cx=e.touches?e.touches[0].clientX:e.clientX;
  const cy=e.touches?e.touches[0].clientY:e.clientY;
  triggerFX(cx,cy); playSound(cur); vib(8); updateUI();

  if(completed){
    vib([30,40,30]);
    if(cur === 1){
      subhanFinaleActive = true;
      subhanDroneProgress = 0;
      setTimeout(()=>showSummary(true), 2100);
    } else if(cur === 0){
      setTimeout(()=>showSummary(true), 1150);
    } else {
      setTimeout(()=>showSummary(true), 650);
    }
  }
}
canvas.addEventListener('click',handleTap);
canvas.addEventListener('touchstart',handleTap,{passive:false});

// ══════════════════════════════════════════
// UI FUNCTIONS
// ══════════════════════════════════════════
const RING_C=471.24;
function updateDailyCountersUI(){
  const tx = TXT[lang] || TXT.id;
  const grandTotal = getGrandDailyTotal();
  const locale = LOCALE_MAP[lang] || 'id-ID';
  document.getElementById('dailyTotalBadge').textContent = `${grandTotal.toLocaleString(locale)}×`;
  document.getElementById('landDailyPill').textContent   = tx.land_pill(grandTotal);
}

function updateUI(){
  const d=DHIKRS[cur], p=Math.min(1, d.count/d.target);
  document.getElementById('cNum').textContent=d.count;
  document.getElementById('cOf').textContent=`/ ${d.target}`;
  document.getElementById('rfg').style.strokeDashoffset=RING_C*(1-p);
  document.getElementById('pFill').style.width=(p*100)+'%';
  updateDailyCountersUI();
}

function populateSceneFromProgress(){
  animals=[]; butterflies=[]; foodPellets=[]; sceneFlowers=[]; hillFlowers=[];
  raindrops=[]; steamPuffs=[]; tapRipples=[]; tapParticles=[];
  subhanFinaleActive = false;
  subhanDroneProgress = 0;
  const d = DHIKRS[cur];

  if(cur === 0){
    const flowerCount = Math.min(28, 5 + Math.floor(d.count * 0.7));
    for(let i=0;i<flowerCount;i++) spawnFlower0();

    const animalCount = Math.min(22, 1 + Math.floor(d.count / 2));
    for(let i=0;i<animalCount;i++) spawnAnimal();

    const bfCount = Math.min(16, 1 + Math.floor(d.count / 2));
    for(let i=0;i<bfCount;i++) spawnButterfly();
  } else if(cur === 1){
    const flowerCount = Math.min(24, 5 + Math.floor(d.count / 2));
    hillFlowers=Array.from({length:flowerCount},()=>({
      x:rand(W*.02,W*.98),y:H*.75,hue:Math.round(rand(0,360)),
      size:rand(.5,1.1),stemH:rand(5,20),maxH:rand(14,35),
      bloom:rand(.3,.8),phase:rand(0,Math.PI*2)
    }));
  }
}

function resetSceneEntities(){
  populateSceneFromProgress();
}

function switchDhikr(idx){
  checkDayRollover();
  cur=idx;
  saveDailyData();
  document.querySelectorAll('.tab').forEach((t,i)=>t.classList.toggle('on',i===idx));
  populateSceneFromProgress();
  applyDhikrTexts(); updateUI();
}

function setTarget(t){
  checkDayRollover();
  DHIKRS.forEach(d=>{
    d.target = t;
    if(d.count >= t) d.count = 0;
  });
  saveDailyData();
  document.getElementById('trg33').classList.toggle('on',t===33);
  document.getElementById('trg99').classList.toggle('on',t===99);
  populateSceneFromProgress();
  updateUI();
}

// ══════════════════════════════════════════
// SUMMARY & DAILY RECAP
// ══════════════════════════════════════════
function showSummary(fromCompletion = true){
  checkDayRollover();
  summaryTriggeredByCompletion = !!fromCompletion;
  const tx = TXT[lang] || TXT.id;
  const locale = LOCALE_MAP[lang] || 'id-ID';
  const grandTotal = getGrandDailyTotal();

  document.getElementById('sumTitle').textContent = fromCompletion ? tx.sum_title : tx.sum_title_recap;
  document.getElementById('sumDate').textContent  = getFormattedDate(lang);
  document.getElementById('sumSub').textContent   = tx.sum_sub;
  document.getElementById('gtLabel').textContent  = tx.gt_label;
  document.getElementById('gtSub').textContent    = tx.gt_sub;
  document.getElementById('gtNum').textContent    = `${grandTotal.toLocaleString(locale)}×`;
  document.getElementById('sumBtn').textContent   = fromCompletion ? tx.sum_btn : tx.sum_close;

  const grid=document.getElementById('iGrid');
  grid.innerHTML='';
  tx.impacts.forEach((im,idx)=>{
    const item = DHIKRS[idx];
    const c=document.createElement('div'); c.className='icard';
    c.innerHTML=`
      <span class="iemoji">${im.emoji}</span>
      <div class="iname">${im.name}</div>
      <span class="inum">${item.dailyTotal.toLocaleString(locale)}×</span>
      <div class="isess">${tx.sess_lbl(item.sessions)}</div>
      <div class="idesc">${im.desc}</div>
    `;
    grid.appendChild(c);
  });
  document.getElementById('summary').classList.add('show');
}

function closeSummary(){
  document.getElementById('summary').classList.remove('show');
  if(summaryTriggeredByCompletion){
    const d=DHIKRS[cur];
    d.count=0;
    saveDailyData();
    resetSceneEntities();
    updateUI();
    showToast(`Round ${d.sessions} ✓ 🌟`);
  }
}

function resetTodayCounts(){
  savedDate = getTodayKey();
  DHIKRS.forEach(d => { d.count = 0; d.dailyTotal = 0; d.sessions = 0; });
  saveDailyData();
  resetSceneEntities();
  updateUI();
  document.getElementById('summary').classList.remove('show');
  showToast((TXT[lang] || TXT.id).reset_done);
}

let toastTimer = null;
function showToast(msg){
  const el=document.getElementById('toast');
  el.textContent=msg;
  el.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(()=>el.classList.remove('show'),2800);
}

// ══════════════════════════════════════════
// EVENT BINDINGS
// ══════════════════════════════════════════
document.getElementById('startBtn').addEventListener('click', startApp);
document.getElementById('btnStats').addEventListener('click', ()=>showSummary(false));
document.getElementById('btnVib').addEventListener('click', toggleVib);
document.getElementById('btnSnd').addEventListener('click', toggleSnd);
document.getElementById('btnLang').addEventListener('click', toggleLang);
document.getElementById('btnHome').addEventListener('click', goHome);

document.getElementById('langSelect').addEventListener('change', (e)=>setLang(e.target.value));
document.querySelectorAll('#langGrid .lbtn').forEach(btn => {
  btn.addEventListener('click', ()=>setLang(btn.dataset.lang));
});

document.getElementById('tab0').addEventListener('click', ()=>switchDhikr(0));
document.getElementById('tab1').addEventListener('click', ()=>switchDhikr(1));
document.getElementById('tab2').addEventListener('click', ()=>switchDhikr(2));
document.getElementById('trg33').addEventListener('click', ()=>setTarget(33));
document.getElementById('trg99').addEventListener('click', ()=>setTarget(99));
document.getElementById('sumBtn').addEventListener('click', closeSummary);
document.getElementById('resetTodayBtn').addEventListener('click', resetTodayCounts);
document.getElementById('btnShareWaStory').addEventListener('click', shareToWhatsAppStory);
document.getElementById('btnCopyLink').addEventListener('click', copyShareLink);

document.addEventListener('visibilitychange', ()=>{
  if(!document.hidden) checkDayRollover();
});

// ══════════════════════════════════════════
// INIT
// ══════════════════════════════════════════
loadDailyData();
syncControlButtons();
applyLang();
updateUI();
populateSceneFromProgress();
</script>
</body>
</html>
"""

with open("dhikr-v2_6.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved dhikr-v2_6.html successfully")
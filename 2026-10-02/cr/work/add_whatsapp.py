from pathlib import Path
p=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\servicio-marcaje-laser.html')
s=p.read_text(encoding='utf-8-sig')
s=s.replace('href="tel:989263149"', 'href="tel:+51989263149"')
s=s.replace('<a class="nav-cta" href="tel:+51989263149">Llamar ahora</a>', '<a class="nav-cta" href="https://wa.me/51989263149" target="_blank" rel="noopener">WhatsApp</a>')
s=s.replace('<a class="button" href="tel:+51989263149">Llamar ahora</a>', '<div style="display:flex;gap:9px;flex-wrap:wrap"><a class="button" href="https://wa.me/51989263149" target="_blank" rel="noopener">Escribir por WhatsApp</a><a class="button" style="background:#35383b" href="tel:+51989263149">Llamar</a></div>')
if 'https://wa.me/51989263149' not in s: raise SystemExit('WhatsApp link missing')
p.write_text(s,encoding='utf-8')
print('WhatsApp and phone links updated to +51 989 263 149.')

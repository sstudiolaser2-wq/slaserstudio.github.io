from pathlib import Path
p=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\servicio-marcaje-laser.html')
s=p.read_text(encoding='utf-8-sig')
s=s.replace('<a class="nav-cta" href="#consulta">Consultar mi pieza</a>', '<a class="nav-cta" href="tel:989263149">Llamar ahora</a>')
s=s.replace('<div><h2>¿Tienes otra pieza en mente?</h2><p>Revisamos material, acabado y diseño para decirte si encaja con el servicio.</p></div><a class="button" href="#servicios">Explorar servicios</a>', '<div><h2>¿Tienes otra pieza en mente?</h2><p>Revisamos material, acabado y diseño para decirte si encaja con el servicio.</p><p style="margin-top:8px"><a href="tel:989263149" style="color:#fff;font-weight:700;font-size:15px">989 263 149</a></p></div><a class="button" href="tel:989263149">Llamar ahora</a>')
s=s.replace('<span>Raycus W30 · 30 W</span><span>Compatibilidad sujeta a revisión de cada pieza</span>', '<span>Raycus W30 · 30 W</span><span><a href="tel:989263149">Tel. 989 263 149</a></span>')
if 'tel:989263149' not in s: raise SystemExit('Telephone link missing')
p.write_text(s,encoding='utf-8')
print('Phone number linked in header, final contact block and footer.')

from pathlib import Path
import re
p=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\servicio-marcaje-laser.html')
s=p.read_text(encoding='utf-8-sig')
s=s.replace('.catalog{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px}', '.catalog{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:13px}')
needle='''<article class="service"><img src="laser-hospital.jpg" alt="Bandeja e instrumental metálico con marcas identificativas" loading="lazy"><div class="service-copy"><span class="sector">Hospitales y equipamiento</span><h3>Placas y activos</h3><p>Identificación de bandejas y equipos compatibles, previa revisión de requisitos.</p></div></article>
</div><p class="illustrative">Fotografías ilustrativas, no son encargos realizados por S Studio Láser. No marcamos sobre animales ni ofrecemos certificación sanitaria o marcado de implantes.</p></div></section>'''
replacement='''<article class="service"><img src="laser-hospital.jpg" alt="Bandeja e instrumental metálico con marcas identificativas" loading="lazy"><div class="service-copy"><span class="sector">Hospitales y equipamiento</span><h3>Placas y activos</h3><p>Identificación de bandejas y equipos compatibles, previa revisión de requisitos.</p></div></article>
<article class="service"><img src="laser-premios-deporte.jpg" alt="Copa, medallas y placa metálica de reconocimiento" loading="lazy"><div class="service-copy"><span class="sector">Colegios · deporte · eventos</span><h3>Medallas, copas y trofeos</h3><p>Grabado en medallas metálicas, placas de trofeos y reconocimientos para colegios, clubes, maratones y competiciones.</p></div></article>
</div><div class="more-inline"><b>También podemos valorar:</b> automoción, recambios, herramientas, electrónica, señalética y prototipos.</div><p class="illustrative">Fotografías ilustrativas; muestran ejemplos de aplicación, no encargos realizados por S Studio Láser. No marcamos sobre animales ni ofrecemos certificación sanitaria o marcado de implantes.</p></div></section>'''
if needle not in s: raise SystemExit('Main catalog insertion point not found')
s=s.replace(needle,replacement)
s,n=re.subn(r'<section class="more" id="otros">.*?</section>', '', s, flags=re.S)
if n!=1: raise SystemExit(f'Expected to remove one separate awards section, got {n}')
s=s.replace('.more{background:#1a1c1f;border-block:1px solid #34363a}', '.more-inline{margin-top:14px;padding:12px 14px;background:#202226;border:1px solid #34363a;color:#c4c5c6;font-size:12px}.more-inline b{color:#f5f3f2}')
s=s.replace('.award-panel{display:grid;grid-template-columns:1fr .82fr;gap:22px;align-items:center;margin-top:10px}.award-panel>img{display:block;width:100%;aspect-ratio:4/2.6;object-fit:cover;border:1px solid #45474b}.more-caption{margin-top:13px}@media(max-width:800px){.award-panel{grid-template-columns:1fr 1fr}}@media(max-width:540px){.award-panel{grid-template-columns:1fr}.award-panel>img{aspect-ratio:4/2.6}}', '')
s=s.replace('<a href="#otros">', '<a href="#servicios">')
if 'id="otros"' in s: raise SystemExit('Separate awards section remains')
p.write_text(s,encoding='utf-8')
print('Awards moved into the main services catalog; separate section removed.')

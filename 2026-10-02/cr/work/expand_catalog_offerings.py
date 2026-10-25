from pathlib import Path
p=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\servicio-marcaje-laser.html')
s=p.read_text(encoding='utf-8-sig')
changes={
'<h3>Componentes y trazabilidad</h3><p>Logos, series, lotes, QR y referencias sobre piezas compatibles.</p>':'<h3>Placas y trazabilidad industrial</h3><p>Placas de características para maquinaria, herramientas e instrumental; logotipos, referencias, series, lotes y códigos QR/Data Matrix.</p>',
'<h3>Placas identificativas</h3><p>Nombres, teléfonos e iconos en chapas y accesorios metálicos.</p>':'<h3>Placas y etiquetas de identificación</h3><p>Placas para mascotas con nombre, teléfono o QR, además de etiquetas y pulseras de emergencia en superficies metálicas compatibles.</p>',
'<span class="sector">Escritura y empresa</span><h3>Bolígrafos y regalos</h3><p>Logotipos, nombres y detalles para clientes, equipos y eventos.</p>':'<span class="sector">Regalos · empresa · merchandising</span><h3>Bolígrafos y artículos personalizados</h3><p>Bolígrafos, termos y vasos térmicos, mates y bombillas, encendedores y llaveros metálicos, según material y superficie.</p>',
'<span class="sector">Hostelería</span><h3>Cubiertos y accesorios</h3><p>Personalización de cubertería, abridores y artículos metálicos de mesa.</p>':'<span class="sector">Cocina · hostelería · aventura</span><h3>Cubiertos, cuchillos y navajas</h3><p>Marcaje personalizado en cubertería, cuchillos, navajas, herramientas de aventura y petacas metálicas.</p>',
'<span class="sector">Colegios · deporte · eventos</span><h3>Medallas, copas y trofeos</h3><p>Grabado en medallas metálicas, placas de trofeos y reconocimientos para colegios, clubes, maratones y competiciones.</p>':'<span class="sector">Colegios · deporte · empresa</span><h3>Fotograbado y reconocimientos</h3><p>Fotograbado en metal, placas de homenaje, medallas, copas, trofeos, gafetes y pines corporativos.</p>',
'<div class="more-inline"><b>También podemos valorar:</b> automoción, recambios, herramientas, electrónica, señalética y prototipos.</div>':'<div class="more-inline"><b>También podemos valorar:</b> automoción y recambios, señalética, electrónica, prototipos y series cortas. Cada pieza se revisa según material, acabado y geometría.</div>'
}
for old,new in changes.items():
 if old not in s: raise SystemExit('Expected text not found: '+old[:60])
 s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
print('Added photogravure, memorial plaques, pins, corporate gifts, emergency tags, knives and flasks to main catalog.')

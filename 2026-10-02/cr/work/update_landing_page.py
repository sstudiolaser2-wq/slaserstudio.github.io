from pathlib import Path
import re
p=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\servicio-marcaje-laser.html')
s=p.read_text(encoding='utf-8-sig')
styles='''
.service-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.service-card{border:1px solid #292c30;background:linear-gradient(145deg,#151719,#0d0f11);overflow:hidden}
.service-card.featured{grid-column:1/-1;display:grid;grid-template-columns:1.12fr .88fr;align-items:stretch}
.service-card .photo{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:#111}
.service-card.featured .photo{height:100%;min-height:340px;aspect-ratio:auto}
.service-copy{padding:23px 25px 25px}
.service-label{font-size:10px;color:#ff737b;letter-spacing:.18em;text-transform:uppercase;font-weight:700}
.service-copy h3{font-size:22px;margin:9px 0 9px;letter-spacing:-.02em}
.service-copy p{font-size:13px;color:#b1b3b5;margin:0 0 15px}
.service-tags{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 17px}
.service-tags span{border:1px solid #36393d;border-radius:99px;padding:5px 9px;color:#c6c8c9;font-size:10px}
.service-link{font-size:12px;color:#ff777e;font-weight:700;letter-spacing:.03em}
.service-link:hover{color:#fff}
.illustrative-note{font-size:11px;color:#85898c;margin-top:20px}
.more-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.more-item{background:#111316;border:1px solid #292c30;padding:18px 19px}
.more-item b{font-size:13px;display:block;margin-bottom:5px}
.more-item p{font-size:11px;color:#a8aaac;margin:0}
@media(max-width:850px){.service-card.featured{grid-template-columns:1fr}.service-card.featured .photo{aspect-ratio:4/3;min-height:0}.more-grid{grid-template-columns:1fr 1fr}}
@media(max-width:540px){.service-grid,.more-grid{grid-template-columns:1fr}.service-card.featured{grid-column:auto}.service-copy{padding:20px}.service-copy h3{font-size:20px}}
'''
s=s.replace('.faq{max-width:820px}',styles+'\n.faq{max-width:820px}')
services=''' <section id="servicios"><div class="wrap">
  <div class="section-head"><div class="kicker">Aplicaciones por sector</div><h2>Una pieza, una solución pensada para ella.</h2><p>Presentamos cada aplicación por separado para que puedas ver qué tipo de trabajo podemos valorar. El resultado depende de la pieza, el material y el acabado.</p></div>
  <div class="service-grid">
   <article class="service-card featured"><img class="photo" src="laser-industria.jpg" alt="Componente industrial metálico con código de trazabilidad grabado" loading="lazy"><div class="service-copy"><div class="service-label">Industria · trazabilidad</div><h3>Identificación industrial</h3><p>Marcaje de componentes y piezas metálicas con logotipos, referencias, numeración de serie, lotes y códigos de identificación para inventario y trazabilidad.</p><div class="service-tags"><span>Series y lotes</span><span>QR / Data Matrix</span><span>Logotipos</span></div><a class="service-link" href="#presupuesto">Consultar una pieza industrial →</a></div></article>
   <article class="service-card"><img class="photo" src="laser-joyeria.jpg" alt="Anillo metálico con un grabado decorativo interior" loading="lazy"><div class="service-copy"><div class="service-label">Joyería · complementos</div><h3>Grabado en joyas</h3><p>Iniciales, fechas, símbolos o motivos decorativos en anillos y complementos metálicos. Valoramos el espacio disponible, la aleación y el acabado.</p><div class="service-tags"><span>Anillos</span><span>Pulseras</span><span>Medallas</span></div><a class="service-link" href="#presupuesto">Consultar una joya →</a></div></article>
   <article class="service-card"><img class="photo" src="laser-relojeria.jpg" alt="Reloj metálico con diseño grabado en la tapa trasera" loading="lazy"><div class="service-copy"><div class="service-label">Relojería</div><h3>Personalización de relojes</h3><p>Grabados personales o conmemorativos en tapas y piezas compatibles. Revisamos geometría, acabado y zonas sensibles antes de aceptar el trabajo.</p><div class="service-tags"><span>Tapas traseras</span><span>Fechas</span><span>Dedicatorias</span></div><a class="service-link" href="#presupuesto">Consultar un reloj →</a></div></article>
   <article class="service-card"><img class="photo" src="laser-mascotas.jpg" alt="Placa identificativa metálica para mascota con huella grabada" loading="lazy"><div class="service-copy"><div class="service-label">Mascotas · veterinaria</div><h3>Placas identificativas</h3><p>Placas y accesorios metálicos con nombre, teléfono, icono o datos identificativos. El grabado se realiza en la placa o accesorio, nunca sobre el animal.</p><div class="service-tags"><span>Placas</span><span>Chapas</span><span>Accesorios</span></div><a class="service-link" href="#presupuesto">Consultar placas para mascotas →</a></div></article>
   <article class="service-card"><img class="photo" src="laser-boligrafos.jpg" alt="Bolígrafos metálicos personalizados con grabado decorativo" loading="lazy"><div class="service-copy"><div class="service-label">Escritura · empresa</div><h3>Bolígrafos y regalos corporativos</h3><p>Personalización de bolígrafos metálicos, accesorios de oficina y obsequios con nombres, logotipos o mensajes breves para equipos, eventos y clientes.</p><div class="service-tags"><span>Bolígrafos</span><span>Regalos de empresa</span><span>Eventos</span></div><a class="service-link" href="#presupuesto">Consultar bolígrafos →</a></div></article>
   <article class="service-card"><img class="photo" src="laser-hosteleria.jpg" alt="Cubiertos de acero inoxidable con detalles grabados en los mangos" loading="lazy"><div class="service-copy"><div class="service-label">Hostelería · restauración</div><h3>Cubiertos y accesorios de mesa</h3><p>Logotipo o detalle decorativo en cubiertos, abrebotellas, accesorios de bar y otras piezas metálicas compatibles. Comprobamos el acabado con una muestra cuando conviene.</p><div class="service-tags"><span>Tenedores y cucharas</span><span>Accesorios de bar</span><span>Detalles para eventos</span></div><a class="service-link" href="#presupuesto">Consultar cubertería →</a></div></article>
   <article class="service-card"><img class="photo" src="laser-hospital.jpg" alt="Bandeja e instrumental reutilizable metálico con marcas de identificación" loading="lazy"><div class="service-copy"><div class="service-label">Hospitales · equipamiento</div><h3>Identificación de activos y material</h3><p>Placas de equipos, bandejas y utensilios metálicos compatibles. Revisamos el material, el protocolo del centro y los requisitos de trazabilidad; no ofrecemos certificación sanitaria ni marcado de implantes.</p><div class="service-tags"><span>Placas de equipo</span><span>Bandejas</span><span>Identificación</span></div><a class="service-link" href="#presupuesto">Consultar equipamiento →</a></div></article>
  </div>
  <p class="illustrative-note">Las fotografías son ilustrativas y muestran ejemplos de aplicación; no representan encargos ya realizados por S Studio Láser.</p>
 </div></section>
 <section id="sectores" class="dark-section"><div class="wrap"><div class="section-head"><div class="kicker">Y muchas más aplicaciones</div><h2>Cuéntanos qué pieza tienes.</h2><p>También valoramos proyectos para otros sectores, siempre que el material y la superficie sean compatibles con láser de fibra.</p></div><div class="more-grid">
  <article class="more-item"><b>Automoción y recambios</b><p>Referencias, identificación y marca en componentes metálicos compatibles.</p></article>
  <article class="more-item"><b>Herramientas y talleres</b><p>Nombre, logotipo, numeración o identificación en herramientas y utillaje.</p></article>
  <article class="more-item"><b>Electrónica y carcasas</b><p>Marcaje de modelos, códigos o identificadores sobre superficies aptas.</p></article>
  <article class="more-item"><b>Placas y señalética</b><p>Placas metálicas de identificación, inventario, puertas y maquinaria.</p></article>
  <article class="more-item"><b>Premios y eventos</b><p>Personalización de placas, trofeos y artículos metálicos conmemorativos.</p></article>
  <article class="more-item"><b>Prototipos y pequeñas series</b><p>Pruebas de diseño y lotes cortos antes de plantear una producción mayor.</p></article>
 </div></div></section>
'''
s,n=re.subn(r' <section id="servicios">.*? <section><div class="wrap split">',services+' <section><div class="wrap split">',s,flags=re.S)
if n!=1: raise SystemExit(f'Expected one services/sectors block; replaced {n}')
p.write_text(s,encoding='utf-8')
print('Updated service catalog and styles.')

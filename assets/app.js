/* Música Brasileira · interações: menu, "se você gosta de", filtros de artistas e músicas */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // menu
  var mb = $('#menuBtn'), nav = $('#siteNav');
  if (mb && nav) mb.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    mb.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // submenus do topo: clique abre/fecha (hover também abre no desktop via CSS)
  var groupsN = $$('.nav-g');
  groupsN.forEach(function (g) {
    var b = g.querySelector('.nav-btn');
    b.addEventListener('click', function (ev) {
      ev.stopPropagation();
      var open = !g.classList.contains('open');
      groupsN.forEach(function (x) { x.classList.remove('open'); x.querySelector('.nav-btn').setAttribute('aria-expanded', 'false'); });
      if (open) { g.classList.add('open'); b.setAttribute('aria-expanded', 'true'); }
    });
  });
  document.addEventListener('click', function (ev) { if (!ev.target.closest('.nav-g')) groupsN.forEach(function (x) { x.classList.remove('open'); x.querySelector('.nav-btn').setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') groupsN.forEach(function (x) { x.classList.remove('open'); x.querySelector('.nav-btn').setAttribute('aria-expanded', 'false'); }); });

  // "se você gosta de…" → destaca famílias
  var likeGrid = $('#likeGrid'), famGrid = $('#famGrid');
  if (likeGrid && famGrid) {
    var cards = $$('.fcard', famGrid);
    likeGrid.addEventListener('click', function (ev) {
      var b = ev.target.closest('.like-btn'); if (!b) return;
      var on = b.getAttribute('aria-pressed') === 'true';
      $$('.like-btn', likeGrid).forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      cards.forEach(function (c) { c.classList.remove('dim', 'hit'); });
      if (on) return;
      b.setAttribute('aria-pressed', 'true');
      var fams = b.getAttribute('data-fams').split(' ');
      cards.forEach(function (c) { c.classList.add(fams.indexOf(c.getAttribute('data-fam')) >= 0 ? 'hit' : 'dim'); });
      famGrid.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });
  }

  // diretório de artistas
  var agrid = $('#agrid');
  if (agrid) {
    var cards2 = $$('.acard', agrid), q = $('#q'), fFam = $('#fFam'), fType = $('#fType'), fTier = $('#fTier'), fDec = $('#fDec'), fTag = $('#fTag'), fSort = $('#fSort'), count = $('#count'), noneMsg = $('#noneMsg');
    var params = new URLSearchParams(location.search);
    if (params.get('f')) fFam.value = params.get('f');
    if (params.get('t')) fTag.value = params.get('t');
    if (params.get('q')) q.value = params.get('q');
    var norm = function (s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
    cards2.forEach(function (c) { c._s = norm(c.getAttribute('data-search')); c._n = norm(c.getAttribute('data-name')); });
    function apply() {
      var qq = norm(q.value.trim()), fam = fFam.value, ty = fType.value, ti = fTier.value, de = fDec.value, tg = fTag.value, n = 0;
      cards2.forEach(function (c) {
        var ok = (!fam || c.getAttribute('data-f') === fam) && (!ty || c.getAttribute('data-type') === ty) && (!ti || c.getAttribute('data-tier') === ti) &&
          (!de || c.getAttribute('data-dec') === de) && (!tg || (' ' + c.getAttribute('data-tags') + ' ').indexOf(' ' + tg + ' ') >= 0) && (!qq || c._s.indexOf(qq) >= 0);
        c.hidden = !ok; if (ok) n++;
      });
      count.textContent = n; noneMsg.hidden = n > 0;
      var s = fSort.value;
      if (s !== 'code') {
        var sorted = cards2.slice().sort(function (a, b) {
          if (s === 'name') return a._n < b._n ? -1 : 1;
          if (s === 'year') return (+a.getAttribute('data-year') || 9999) - (+b.getAttribute('data-year') || 9999) || (a._n < b._n ? -1 : 1);
          return (+a.getAttribute('data-tierord')) - (+b.getAttribute('data-tierord')) || (a._n < b._n ? -1 : 1);
        });
        sorted.forEach(function (c) { agrid.appendChild(c); });
      } else cards2.forEach(function (c) { agrid.appendChild(c); });
      var p = new URLSearchParams(); if (fam) p.set('f', fam); if (tg) p.set('t', tg); if (q.value.trim()) p.set('q', q.value.trim());
      history.replaceState(null, '', location.pathname + (p.toString() ? '?' + p : '') + location.hash);
    }
    [q, fFam, fType, fTier, fDec, fTag, fSort].forEach(function (el) { el.addEventListener('input', apply); el.addEventListener('change', apply); });
    $('#fReset').addEventListener('click', function () { q.value = ''; [fFam, fType, fTier, fDec, fTag].forEach(function (s) { s.value = ''; }); fSort.value = 'code'; apply(); });
    apply();
    if (location.hash) { var tgt = document.getElementById(location.hash.slice(1)); if (tgt) { tgt.hidden = false; setTimeout(function () { tgt.scrollIntoView({ block: 'center' }); tgt.style.outline = '3px solid var(--acid)'; }, 60); } }
  }

  // linha do tempo das músicas
  var sl = $('#songlist');
  if (sl) {
    var songs = $$('.song', sl), heads = $$('.yhead', sl), sq = $('#sq'), gsel = $('#gsel'), tabs = $('#decTabs'), scount = $('#scount');
    var g = '', dec = '';
    var norm2 = function (s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
    songs.forEach(function (s) { s._s = norm2(s.getAttribute('data-search')); });
    function applyS() {
      var qq = norm2(sq.value.trim()), n = 0, byYear = {};
      songs.forEach(function (s) {
        var ok = (!g || s.getAttribute('data-g') === g) && (!dec || s.getAttribute('data-dec') === dec) && (!qq || s._s.indexOf(qq) >= 0);
        s.hidden = !ok; if (ok) { n++; byYear[s.previousYear] = true; }
      });
      heads.forEach(function (h) { h.hidden = !byYear[h.getAttribute('data-year')]; });
      scount.textContent = n;
    }
    var cur = null; $$('li', sl).forEach(function (li) { if (li.classList.contains('yhead')) cur = li.getAttribute('data-year'); else li.previousYear = cur; });
    sq.addEventListener('input', applyS);
    gsel.addEventListener('change', function () { g = gsel.value; applyS(); });
    var sp = new URLSearchParams(location.search); if (sp.get('g')) { gsel.value = sp.get('g'); g = gsel.value; applyS(); }
    tabs.addEventListener('click', function (ev) { var b = ev.target.closest('button'); if (!b) return; dec = b.getAttribute('data-dec'); $$('button', tabs).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); applyS(); });
  }

  // discos essenciais: gênero, década e busca
  var al = $('#alist');
  if (al) {
    var albs = $$('.album', al), dheads = $$('.dhead', al), aq = $('#aq'), agsel = $('#agsel'), atabs = $('#adecTabs'), acount = $('#acount');
    var ag = '', adec = '';
    var nrm = function (s) { return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(); };
    albs.forEach(function (x) { x._s = nrm(x.getAttribute('data-search')); });
    function applyA() {
      var qq = nrm(aq.value.trim()), n = 0, seen = {};
      albs.forEach(function (x) {
        var ok = (!ag || x.getAttribute('data-g') === ag) && (!adec || x.getAttribute('data-dec') === adec) && (!qq || x._s.indexOf(qq) >= 0);
        x.hidden = !ok; if (ok) { n++; seen[x.getAttribute('data-dec')] = 1; }
      });
      dheads.forEach(function (h) { h.hidden = !seen[h.getAttribute('data-dec')]; });
      acount.textContent = n;
    }
    aq.addEventListener('input', applyA);
    agsel.addEventListener('change', function () { ag = agsel.value; applyA(); });
    atabs.addEventListener('click', function (ev) { var b = ev.target.closest('button'); if (!b) return; adec = b.getAttribute('data-dec'); $$('button', atabs).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); applyA(); });
    var ap = new URLSearchParams(location.search); if (ap.get('g')) { agsel.value = ap.get('g'); ag = agsel.value; applyA(); }
  }

  // índice "Nesta página": barra fixa com as seções da página
  (function () {
    var main = $('#main'); if (!main) return;
    var hs = $$('section.sec-in > h2, section.sec > .wrap > h2', main).filter(function (h) { return !h.closest('.gcard, .card, .acard'); });
    if (hs.length < 3) return;
    var en = document.documentElement.lang === 'en';
    var used = {};
    var links = hs.map(function (h) {
      var sec = h.parentElement.closest('section') || h;
      var label = ((h.childNodes[0] && h.childNodes[0].textContent) || h.textContent).trim();
      var id = sec.id || ('s-' + label.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
      while (used[id]) { id += '-2'; }
      used[id] = 1; sec.id = id;
      return { id: id, label: label, el: sec };
    });
    var title = en ? 'On this page' : 'Nesta página';
    var nav = document.createElement('nav');
    nav.className = 'toc'; nav.setAttribute('aria-label', title);
    nav.innerHTML = '<div class="wrap"><span class="toc-l">' + title + '</span><div class="toc-s">' +
      links.map(function (l) { return '<a href="#' + l.id + '">' + l.label.replace(/</g, '&lt;') + '</a>'; }).join('') + '</div></div>';
    var top = $('.fam-head, .hero', main), ph = $('.page-head', main);
    if (top) { top.parentNode.insertBefore(nav, top.nextSibling); }
    else if (ph) { ph.parentNode.insertBefore(nav, ph.nextSibling); }
    else { main.insertBefore(nav, main.firstChild); }
    var as = $$('a', nav);
    if ('IntersectionObserver' in window) {
      var io2 = new IntersectionObserver(function (es) {
        es.forEach(function (ent) {
          if (!ent.isIntersecting) return;
          as.forEach(function (x) {
            var on = x.getAttribute('href') === '#' + ent.target.id;
            x.classList.toggle('on', on);
            if (on) { x.parentNode.scrollTo({ left: x.offsetLeft - 40, behavior: 'smooth' }); }
          });
        });
      }, { rootMargin: '-35% 0px -60% 0px' });
      links.forEach(function (l) { io2.observe(l.el); });
    }
  })();

  // revelação ao rolar, contadores e mapa animado
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets = $$('.sec h2, .sec .lead, .like-btn, .fcard, .door, .stat, .gcard, .sub, .card, .mcard, .term, .album, .page-head, .sec-in h2, .songs li, .acard, .tablewrap').slice(0, 90);
  if (!reduce && 'IntersectionObserver' in window) {
    var vh = window.innerHeight || 800;
    targets.forEach(function (el, i) {
      el.classList.add('reveal'); el.style.transitionDelay = ((i % 6) * 60) + 'ms';
      if (el.getBoundingClientRect().top < vh * 1.05) requestAnimationFrame(function () { el.classList.add('in'); });
    });
    var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }); }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (el) { io.observe(el); });
    setTimeout(function () { if (!$('.reveal.in')) targets.forEach(function (el) { el.classList.add('in'); }); }, 2500);
    var maps = $$('.gmap');
    if (maps.length) { var mo = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); mo.unobserve(en.target); } }); }, { threshold: 0.2 }); maps.forEach(function (m) { mo.observe(m); }); }
    var counters = $$('[data-count]');
    if (counters.length) {
      var co = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (!en.isIntersecting) return; co.unobserve(en.target);
          var el = en.target, end = +el.getAttribute('data-count'), t0 = performance.now(), dur = 1400;
          var loc = document.documentElement.lang === 'en' ? 'en-US' : 'pt-BR';
          (function step(now) { var k = Math.min(1, (now - t0) / dur); k = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(end * k).toLocaleString(loc); if (k < 1) requestAnimationFrame(step); })(t0);
        });
      }, { threshold: 0.5 });
      counters.forEach(function (c) { co.observe(c); });
    }
  } else { $$('.gmap').forEach(function (m) { m.classList.add('in'); }); }

})();

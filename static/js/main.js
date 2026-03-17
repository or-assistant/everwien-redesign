/* ============================================
   Everwien — Main JavaScript
   Sonnenschutz & Raumdesign seit 1880
   ============================================ */
(function () {
  'use strict';

  var lang = window.__EVERWIEN_LANG__ || {};

  /* -----------------------------------------------
     1. Dark Mode Toggle
     ----------------------------------------------- */
  var themeToggle = document.getElementById('theme-toggle');

  function getPreferredTheme() {
    var stored = localStorage.getItem('theme');
    if (stored === 'dark' || stored === 'light') return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (themeToggle) {
      var isDark = theme === 'dark';
      var sunIcon = themeToggle.querySelector('.theme-toggle__sun');
      var moonIcon = themeToggle.querySelector('.theme-toggle__moon');
      if (sunIcon) sunIcon.style.display = isDark ? 'none' : 'block';
      if (moonIcon) moonIcon.style.display = isDark ? 'block' : 'none';
      themeToggle.setAttribute('aria-label', isDark ? 'Helles Design aktivieren' : 'Dunkles Design aktivieren');
    }
  }

  // Apply on load (complements the inline script in <head> that prevents FOUC)
  applyTheme(getPreferredTheme());

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var current = document.documentElement.getAttribute('data-theme') || 'light';
      applyTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  // React to OS-level changes when no explicit preference is stored
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
    if (!localStorage.getItem('theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });

  /* -----------------------------------------------
     2. Scroll Progress Bar
     ----------------------------------------------- */
  var scrollProgress = document.getElementById('scroll-progress');
  var scrollTicking = false;

  function updateScrollProgress() {
    if (!scrollProgress) return;
    var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = docHeight > 0 ? (window.scrollY / docHeight) * 100 : 0;
    scrollProgress.style.width = scrolled + '%';
    scrollTicking = false;
  }

  /* -----------------------------------------------
     3. Back-to-Top Button
     ----------------------------------------------- */
  var backToTop = document.getElementById('back-to-top');
  var backToTopTicking = false;

  function updateBackToTop() {
    if (!backToTop) return;
    backToTop.classList.toggle('visible', window.scrollY > 300);
    backToTopTicking = false;
  }

  if (backToTop) {
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* Combined scroll handler for progress bar + back-to-top */
  window.addEventListener('scroll', function () {
    if (!scrollTicking) {
      scrollTicking = true;
      requestAnimationFrame(updateScrollProgress);
    }
    if (!backToTopTicking) {
      backToTopTicking = true;
      requestAnimationFrame(updateBackToTop);
    }
  }, { passive: true });

  // Initial state
  updateScrollProgress();
  updateBackToTop();

  /* -----------------------------------------------
     4. Sticky Nav scroll effect
     ----------------------------------------------- */
  var nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', function () {
      nav.classList.toggle('scrolled', window.scrollY > 20);
    }, { passive: true });
  }

  /* -----------------------------------------------
     5. Mobile Menu
     ----------------------------------------------- */
  var hamburger = document.querySelector('.nav__hamburger');
  var mobileNav = document.querySelector('.nav__mobile');
  var overlay = document.querySelector('.nav__overlay');

  function closeMobile() {
    if (hamburger) {
      hamburger.classList.remove('active');
      hamburger.setAttribute('aria-expanded', 'false');
    }
    if (mobileNav) mobileNav.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (hamburger) {
    hamburger.addEventListener('click', function () {
      var isOpen = mobileNav.classList.contains('open');
      if (isOpen) {
        closeMobile();
      } else {
        hamburger.classList.add('active');
        hamburger.setAttribute('aria-expanded', 'true');
        mobileNav.classList.add('open');
        overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  }
  if (overlay) overlay.addEventListener('click', closeMobile);
  if (mobileNav) {
    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeMobile);
    });
  }

  /* -----------------------------------------------
     6. FAQ Accordion
     ----------------------------------------------- */
  document.querySelectorAll('.faq-item__question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var answer = item.querySelector('.faq-item__answer');
      var isActive = item.classList.contains('active');

      // Close all others in same container
      var container = item.closest('.faq-list, .faq-category, .section');
      if (container) {
        container.querySelectorAll('.faq-item.active').forEach(function (other) {
          if (other !== item) {
            other.classList.remove('active');
            other.querySelector('.faq-item__answer').style.maxHeight = '0';
          }
        });
      }

      if (isActive) {
        item.classList.remove('active');
        answer.style.maxHeight = '0';
      } else {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  /* -----------------------------------------------
     7. Intersection Observer fade-in
     ----------------------------------------------- */
  var fadeEls = document.querySelectorAll('.fade-in');
  if (fadeEls.length && 'IntersectionObserver' in window) {
    var fadeObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          fadeObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    fadeEls.forEach(function (el) { fadeObserver.observe(el); });
  } else {
    fadeEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* -----------------------------------------------
     8. Interactive Product Cards (Accordion)
     ----------------------------------------------- */
  document.querySelectorAll('.product-card').forEach(function (card) {
    card.addEventListener('click', function () {
      var grid = card.closest('.product-grid');
      var isExpanded = card.classList.contains('product-card--expanded');
      var details = card.querySelector('.product-card__details');

      // Close all other cards in the same grid
      if (grid) {
        grid.querySelectorAll('.product-card--expanded').forEach(function (other) {
          if (other !== card) {
            other.classList.remove('product-card--expanded');
            var otherDetails = other.querySelector('.product-card__details');
            if (otherDetails) otherDetails.style.maxHeight = '0';
          }
        });
      }

      if (isExpanded) {
        card.classList.remove('product-card--expanded');
        if (details) details.style.maxHeight = '0';
      } else {
        card.classList.add('product-card--expanded');
        if (details) details.style.maxHeight = details.scrollHeight + 'px';
      }
    });

    // Prevent links inside cards from triggering card toggle
    card.querySelectorAll('a, button').forEach(function (inner) {
      inner.addEventListener('click', function (e) {
        e.stopPropagation();
      });
    });
  });

  /* -----------------------------------------------
     9. Gallery Lightbox
     ----------------------------------------------- */
  var lightboxOverlay = null;
  var lightboxImg = null;

  function createLightbox() {
    lightboxOverlay = document.createElement('div');
    lightboxOverlay.className = 'lightbox-overlay';
    lightboxOverlay.setAttribute('role', 'dialog');
    lightboxOverlay.setAttribute('aria-label', 'Bildvorschau');
    lightboxOverlay.style.cssText =
      'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.88);' +
      'display:flex;align-items:center;justify-content:center;z-index:10000;cursor:zoom-out;' +
      'opacity:0;transition:opacity .3s ease;';

    lightboxImg = document.createElement('img');
    lightboxImg.className = 'lightbox-overlay__img';
    lightboxImg.style.cssText =
      'max-width:90vw;max-height:90vh;border-radius:8px;box-shadow:0 8px 40px rgba(0,0,0,.5);' +
      'transform:scale(.92);transition:transform .3s ease;cursor:default;';

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox-overlay__close';
    closeBtn.setAttribute('aria-label', 'Schließen');
    closeBtn.innerHTML = '&times;';
    closeBtn.style.cssText =
      'position:absolute;top:20px;right:24px;background:none;border:none;' +
      'color:#fff;font-size:36px;cursor:pointer;line-height:1;padding:8px;z-index:10001;';

    lightboxOverlay.appendChild(lightboxImg);
    lightboxOverlay.appendChild(closeBtn);
    document.body.appendChild(lightboxOverlay);

    // Close on overlay click (but not image click)
    lightboxOverlay.addEventListener('click', function (e) {
      if (e.target === lightboxOverlay || e.target === closeBtn) {
        closeLightbox();
      }
    });

    lightboxImg.addEventListener('click', function (e) {
      e.stopPropagation();
    });
  }

  function openLightbox(src, alt) {
    if (!lightboxOverlay) createLightbox();
    lightboxImg.src = src;
    lightboxImg.alt = alt || '';
    lightboxOverlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    // Trigger transition
    requestAnimationFrame(function () {
      lightboxOverlay.style.opacity = '1';
      lightboxImg.style.transform = 'scale(1)';
    });
  }

  function closeLightbox() {
    if (!lightboxOverlay) return;
    lightboxOverlay.style.opacity = '0';
    lightboxImg.style.transform = 'scale(.92)';
    document.body.style.overflow = '';
    setTimeout(function () {
      lightboxOverlay.style.display = 'none';
      lightboxImg.src = '';
    }, 300);
  }

  document.querySelectorAll('.gallery-item img').forEach(function (img) {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', function () {
      // Use data-full attribute for high-res, otherwise the img src
      var fullSrc = img.getAttribute('data-full') || img.src;
      openLightbox(fullSrc, img.alt);
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeLightbox();
  });

  /* -----------------------------------------------
     10. Footer Rotating Sayings
     ----------------------------------------------- */
  var footerSaying = document.getElementById('footer-saying');

  if (footerSaying && lang.footer && Array.isArray(lang.footer.sayings) && lang.footer.sayings.length) {
    var sayings = lang.footer.sayings;
    var currentSayingIndex = -1;

    function showRandomSaying() {
      var idx;
      // Avoid repeating the same saying twice
      if (sayings.length > 1) {
        do { idx = Math.floor(Math.random() * sayings.length); } while (idx === currentSayingIndex);
      } else {
        idx = 0;
      }
      currentSayingIndex = idx;

      // Fade out
      footerSaying.style.opacity = '0';
      setTimeout(function () {
        footerSaying.textContent = sayings[idx];
        // Fade in
        footerSaying.style.opacity = '1';
      }, 400);
    }

    footerSaying.style.transition = 'opacity .4s ease';
    showRandomSaying();
    setInterval(showRandomSaying, 8000);
  }

  /* -----------------------------------------------
     11. Inline Form Validation Helpers
     ----------------------------------------------- */
  var CHECKMARK_SVG =
    '<svg class="form-check" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6B7F5E" stroke-width="3">' +
    '<path d="M5 13l4 4L19 7"/></svg>';

  var SUCCESS_SVG =
    '<div class="form-success-animation">' +
    '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#6B7F5E" stroke-width="2">' +
    '<circle cx="12" cy="12" r="10" stroke-dasharray="63" stroke-dashoffset="63"><animate attributeName="stroke-dashoffset" to="0" dur=".5s" fill="freeze"/></circle>' +
    '<path d="M7 13l3 3 7-7" stroke-dasharray="20" stroke-dashoffset="20"><animate attributeName="stroke-dashoffset" to="0" dur=".3s" begin=".5s" fill="freeze"/></path>' +
    '</svg></div>';

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  function isValidPhone(value) {
    return /^[+\d\s\-/()]{6,}$/.test(value.trim());
  }

  function validateField(input) {
    var group = input.closest('.form-group');
    if (!group) return true;

    // Remove previous status
    group.classList.remove('invalid', 'valid');
    var existingCheck = group.querySelector('.form-check');
    if (existingCheck) existingCheck.remove();
    var existingError = group.querySelector('.form-error');
    if (existingError) existingError.remove();

    var value = input.type === 'checkbox' ? input.checked : input.value.trim();
    var isRequired = input.hasAttribute('required');
    var isValid = true;
    var errorMsg = '';

    // Required check
    if (isRequired && !value) {
      isValid = false;
      errorMsg = 'Dieses Feld ist erforderlich.';
    }

    // Type-specific checks
    if (isValid && value) {
      if (input.type === 'email' && !isValidEmail(input.value)) {
        isValid = false;
        errorMsg = 'Bitte geben Sie eine gültige E-Mail-Adresse ein.';
      } else if (input.type === 'tel' && !isValidPhone(input.value)) {
        isValid = false;
        errorMsg = 'Bitte geben Sie eine gültige Telefonnummer ein.';
      }
    }

    if (!isValid) {
      group.classList.add('invalid');
      var errorEl = document.createElement('span');
      errorEl.className = 'form-error';
      errorEl.textContent = errorMsg;
      errorEl.style.cssText = 'color:#c0392b;font-size:.82rem;display:block;overflow:hidden;max-height:0;transition:max-height .3s ease;';
      group.appendChild(errorEl);
      // Animate error reveal
      requestAnimationFrame(function () {
        errorEl.style.maxHeight = '40px';
      });
    } else if (value) {
      group.classList.add('valid');
      group.insertAdjacentHTML('beforeend', CHECKMARK_SVG);
    }

    return isValid;
  }

  // Attach real-time blur validation to all form fields
  document.querySelectorAll('form .form-group input, form .form-group textarea, form .form-group select').forEach(function (input) {
    input.addEventListener('blur', function () {
      validateField(input);
    });
    // Clear error on focus
    input.addEventListener('focus', function () {
      var group = input.closest('.form-group');
      if (group) {
        group.classList.remove('invalid');
        var err = group.querySelector('.form-error');
        if (err) err.remove();
      }
    });
  });

  /* -----------------------------------------------
     12. Contact Form Validation & Submission
     ----------------------------------------------- */
  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = true;

      // Reset
      contactForm.querySelectorAll('.form-group').forEach(function (g) {
        g.classList.remove('invalid', 'valid');
        var check = g.querySelector('.form-check');
        if (check) check.remove();
        var err = g.querySelector('.form-error');
        if (err) err.remove();
      });

      // Validate required fields
      contactForm.querySelectorAll('[required]').forEach(function (input) {
        if (!validateField(input)) valid = false;
      });

      // Email check
      var email = contactForm.querySelector('[type="email"]');
      if (email && email.value && !isValidEmail(email.value)) {
        var emailGroup = email.closest('.form-group');
        emailGroup.classList.add('invalid');
        valid = false;
      }

      // Privacy checkbox
      var privacy = contactForm.querySelector('#privacy');
      if (privacy && !privacy.checked) {
        var privGroup = privacy.closest('.form-group');
        privGroup.classList.add('invalid');
        valid = false;
      }

      if (valid) {
        var btn = contactForm.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.innerHTML = SUCCESS_SVG + ' Nachricht gesendet!';
        btn.style.background = '#6B7F5E';
        setTimeout(function () {
          contactForm.reset();
          btn.textContent = 'Nachricht senden';
          btn.disabled = false;
          btn.style.background = '';
          // Clear valid states
          contactForm.querySelectorAll('.form-group').forEach(function (g) {
            g.classList.remove('valid');
            var check = g.querySelector('.form-check');
            if (check) check.remove();
          });
        }, 3000);
      }
    });
  }

  /* -----------------------------------------------
     13. Karriere Form Validation & Submission
     ----------------------------------------------- */
  var karriereForm = document.getElementById('karriere-form');
  if (karriereForm) {
    karriereForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = true;

      karriereForm.querySelectorAll('.form-group').forEach(function (g) {
        g.classList.remove('invalid', 'valid');
        var check = g.querySelector('.form-check');
        if (check) check.remove();
        var err = g.querySelector('.form-error');
        if (err) err.remove();
      });

      karriereForm.querySelectorAll('[required]').forEach(function (input) {
        if (!validateField(input)) valid = false;
      });

      if (valid) {
        var btn = karriereForm.querySelector('button[type="submit"]');
        btn.disabled = true;
        btn.innerHTML = SUCCESS_SVG + ' Bewerbung gesendet!';
        btn.style.background = '#6B7F5E';
        setTimeout(function () {
          karriereForm.reset();
          btn.textContent = 'Bewerbung absenden';
          btn.disabled = false;
          btn.style.background = '';
          karriereForm.querySelectorAll('.form-group').forEach(function (g) {
            g.classList.remove('valid');
            var check = g.querySelector('.form-check');
            if (check) check.remove();
          });
        }, 3000);
      }
    });
  }

  /* -----------------------------------------------
     14. Team Accordion
     ----------------------------------------------- */
  document.querySelectorAll('.team-category__header').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var category = btn.closest('.team-category');
      var body = category.querySelector('.team-category__body');
      var isActive = btn.classList.contains('active');

      // Close all others
      var accordion = btn.closest('.team-accordion');
      if (accordion) {
        accordion.querySelectorAll('.team-category__header.active').forEach(function (other) {
          if (other !== btn) {
            other.classList.remove('active');
            other.setAttribute('aria-expanded', 'false');
            other.closest('.team-category').querySelector('.team-category__body').style.maxHeight = '0';
          }
        });
      }

      if (isActive) {
        btn.classList.remove('active');
        btn.setAttribute('aria-expanded', 'false');
        body.style.maxHeight = '0';
      } else {
        btn.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
        body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });

  /* -----------------------------------------------
     15. Smooth Scroll for Anchor Links
     ----------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = anchor.getAttribute('href');
      if (href === '#') return;
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
